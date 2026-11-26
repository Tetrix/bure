"""Game objects: the player, spinning wheels/stars, number pickups, hazards."""

from __future__ import annotations

import math

import pygame

from . import assets
from .levels import HazardSpec, RingSpec, SpinnerSpec
from .settings import (PLAYER_MAX_POS, PLAYER_SIZE, PLAYER_START, SCREEN_HEIGHT,
                       SCREEN_WIDTH, WHITE)

PICKUP_COOLDOWN = 1.2  # seconds a returned number can't be picked up again


def masks_overlap(a_mask: pygame.Mask, a_rect: pygame.Rect,
                  b_mask: pygame.Mask, b_rect: pygame.Rect) -> bool:
    """Pixel-perfect collision test, with a cheap bounding-box check first."""
    if not a_rect.colliderect(b_rect):
        return False
    return a_mask.overlap(b_mask, (b_rect.x - a_rect.x, b_rect.y - a_rect.y)) is not None


def _bounce(pos: pygame.Vector2, velocity: pygame.Vector2, size, top: int = 0) -> None:
    """Keep ``pos`` inside the screen, reversing ``velocity`` at the edges."""
    max_x = SCREEN_WIDTH - size[0]
    max_y = SCREEN_HEIGHT - size[1]
    if not 0 <= pos.x <= max_x:
        velocity.x = -velocity.x
        pos.x = min(max(pos.x, 0), max_x)
    if not top <= pos.y <= max_y:
        velocity.y = -velocity.y
        pos.y = min(max(pos.y, top), max_y)


class Player:
    def __init__(self, speed: float) -> None:
        self.image = assets.image("penguin.png", PLAYER_SIZE)
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.Vector2(PLAYER_START)
        self.speed = speed

    @property
    def rect(self) -> pygame.Rect:
        return self.image.get_rect(topleft=(round(self.pos.x), round(self.pos.y)))

    def update(self, dt: float, keys) -> None:
        direction = pygame.Vector2(
            (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a]),
            (keys[pygame.K_DOWN] or keys[pygame.K_s]) - (keys[pygame.K_UP] or keys[pygame.K_w]),
        )
        if direction.length_squared() > 1:
            direction.normalize_ip()  # diagonal moves aren't faster
        self.pos += direction * self.speed * dt
        self.pos.x = min(max(self.pos.x, 0), PLAYER_MAX_POS[0])
        self.pos.y = min(max(self.pos.y, 0), PLAYER_MAX_POS[1])

    def draw(self, screen: pygame.Surface, visible: bool = True) -> None:
        if visible:
            screen.blit(self.image, self.rect)

    def touches(self, mask: pygame.Mask, rect: pygame.Rect) -> bool:
        return masks_overlap(self.mask, self.rect, mask, rect)


class Spinner:
    """A wheel or star rotating around its centre.

    Deadly spinners use a slightly smaller copy of the picture as their hitbox
    (``hitbox_scale``), so near-misses at the star tips feel fair.
    """

    def __init__(self, spec: SpinnerSpec, speed_scale: float = 1.0,
                 hitbox_scale: float = 1.0) -> None:
        self.spec = spec
        self.speed = spec.speed * speed_scale
        self.base = assets.image(spec.image, spec.size)
        if hitbox_scale < 1.0:
            w, h = spec.size
            self.hit_base = pygame.transform.smoothscale(
                self.base, (round(w * hitbox_scale), round(h * hitbox_scale)))
        else:
            self.hit_base = self.base
        self.angle = 0.0
        self._rotate()

    def _rotate(self) -> None:
        self.image = pygame.transform.rotate(self.base, self.angle)
        self.rect = self.image.get_rect(center=self.spec.center)
        self._hitbox = None  # built lazily, only when the player is close

    def hitbox(self) -> tuple[pygame.Mask, pygame.Rect]:
        if self._hitbox is None:
            surf = (self.image if self.hit_base is self.base
                    else pygame.transform.rotate(self.hit_base, self.angle))
            self._hitbox = (pygame.mask.from_surface(surf),
                            surf.get_rect(center=self.spec.center))
        return self._hitbox

    def touches(self, player: Player) -> bool:
        if not player.rect.colliderect(self.rect):
            return False
        return player.touches(*self.hitbox())

    def update(self, dt: float) -> None:
        self.angle = (self.angle + self.speed * dt) % 360
        self._rotate()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)


class Pickup:
    """Something the player collects for its value."""

    def __init__(self, value: int, image: pygame.Surface) -> None:
        self.value = value
        self.image = image
        self.faded = image.copy()
        self.faded.set_alpha(80)
        self.mask = pygame.mask.from_surface(image)
        self.rect = image.get_rect()
        self.collected = False
        self.cooldown = 0.0

    @property
    def available(self) -> bool:
        return not self.collected and self.cooldown <= 0

    def release(self) -> None:
        """Put the pickup back into play after a short cooldown."""
        self.collected = False
        self.cooldown = PICKUP_COOLDOWN

    def tick(self, dt: float) -> None:
        if self.cooldown > 0:
            self.cooldown -= dt

    def draw(self, screen: pygame.Surface, remaining: int | None = None) -> None:
        """``remaining`` (hints mode) = how much is still needed."""
        if self.collected:
            return
        if self.cooldown > 0:
            screen.blit(self.faded, self.rect)
            return
        if remaining is not None:
            if self.value == remaining:
                pygame.draw.circle(screen, WHITE, self.rect.center, self.rect.width // 2 + 4)
            elif self.value > remaining:
                screen.blit(self.faded, self.rect)
                return
        screen.blit(self.image, self.rect)


class NumberPickup(Pickup):
    def __init__(self, value: int, angle: float) -> None:
        super().__init__(value, assets.digit(value))
        self.angle = angle


class Ring:
    """A group of numbers orbiting a shared centre point."""

    def __init__(self, spec: RingSpec, speed_scale: float = 1.0) -> None:
        self.spec = spec
        self.speed = spec.speed * speed_scale
        self.pickups = [NumberPickup(value, angle) for value, angle in spec.slots]
        self.update(0)

    def update(self, dt: float) -> None:
        cx, cy = self.spec.center
        r = self.spec.radius
        for p in self.pickups:
            p.tick(dt)
            p.angle = (p.angle + self.speed * dt) % 360
            rad = math.radians(p.angle)
            # As in the original, the orbit point is the image's top-left corner.
            p.rect.topleft = (round(cx + math.cos(rad) * r), round(cy + math.sin(rad) * r))


def _bubble_image(value: int) -> pygame.Surface:
    radius = 24
    surf = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
    pygame.draw.circle(surf, (200, 40, 60), (radius, radius), radius)
    pygame.draw.circle(surf, WHITE, (radius, radius), radius, 3)
    text = assets.font("goall.otf", 30).render(str(value), True, WHITE)
    surf.blit(text, text.get_rect(center=(radius, radius + 1)))
    return surf


class MinusBubble(Pickup):
    """A slowly drifting negative number; grabbing it lowers the sum."""

    def __init__(self, value: int, start, velocity) -> None:
        assert value < 0
        super().__init__(value, _bubble_image(value))
        self.pos = pygame.Vector2(start)
        self.velocity = pygame.Vector2(velocity)
        self.rect.topleft = start

    def update(self, dt: float) -> None:
        self.tick(dt)
        self.pos += self.velocity * dt
        _bounce(self.pos, self.velocity, self.rect.size, top=100)
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))


class Hazard:
    """The bouncing "danger" sprite from level 10 onward."""

    def __init__(self, spec: HazardSpec, speed_scale: float = 1.0) -> None:
        self.image = assets.image("danger/danger.png", (spec.size, spec.size))
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.Vector2(spec.start)
        self.velocity = pygame.Vector2(spec.velocity) * speed_scale

    @property
    def rect(self) -> pygame.Rect:
        return self.image.get_rect(topleft=(round(self.pos.x), round(self.pos.y)))

    def touches(self, player: Player) -> bool:
        return player.touches(self.mask, self.rect)

    def update(self, dt: float) -> None:
        self.pos += self.velocity * dt
        _bounce(self.pos, self.velocity, self.image.get_size())

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect)
