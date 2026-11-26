"""Short-lived visual effects: floating text and screen shake."""

from __future__ import annotations

import random

import pygame

from . import assets


class Popup:
    """Text that floats upward and fades out, e.g. "+7" or "Too much!"."""

    LIFETIME = 0.9
    RISE = 45  # pixels over its lifetime

    def __init__(self, text: str, pos, color, size: int = 28) -> None:
        # Ubuntu has "+" and "!" glyphs; the HUD font doesn't.
        font = assets.font("ubuntu.ttf", size)
        text_surf = font.render(text, True, color)
        outline = font.render(text, True, (20, 20, 30))
        w, h = text_surf.get_size()
        self.surface = pygame.Surface((w + 4, h + 4), pygame.SRCALPHA)
        for dx, dy in ((0, 0), (4, 0), (0, 4), (4, 4), (2, 0), (0, 2), (4, 2), (2, 4)):
            self.surface.blit(outline, (dx, dy))  # dark outline for contrast
        self.surface.blit(text_surf, (2, 2))
        half = self.surface.get_width() // 2 + 4
        self.x = min(max(pos[0], half), 800 - half)
        self.y = max(pos[1], 30)
        self.age = 0.0

    @property
    def alive(self) -> bool:
        return self.age < self.LIFETIME

    def update(self, dt: float) -> None:
        self.age += dt

    def draw(self, screen: pygame.Surface) -> None:
        t = self.age / self.LIFETIME
        self.surface.set_alpha(round(255 * (1 - t * t)))
        rect = self.surface.get_rect(center=(self.x, self.y - self.RISE * t))
        screen.blit(self.surface, rect)


class Shake:
    def __init__(self) -> None:
        self.time = 0.0
        self.strength = 0

    def start(self, seconds: float = 0.3, strength: int = 8) -> None:
        self.time, self.strength = seconds, strength

    def update(self, dt: float) -> None:
        self.time = max(0.0, self.time - dt)

    @property
    def offset(self) -> tuple[int, int]:
        if self.time <= 0:
            return (0, 0)
        s = self.strength
        return (random.randint(-s, s), random.randint(-s, s))
