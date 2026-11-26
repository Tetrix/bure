"""One attempt at one level: the rules of the game live here."""

from __future__ import annotations

import enum
import random

import pygame

from . import assets
from .difficulty import DEFAULT, Difficulty
from .effects import Popup
from .entities import Hazard, MinusBubble, Pickup, Player, Ring, Spinner
from .hud import Hud
from .levels import LevelSpec
from .settings import SCREEN_SIZE, WHITE

INVULNERABLE_SECONDS = 1.5
UNDO_TIME_COST = 2.0
GOOD = (120, 255, 140)
BAD = (255, 110, 110)


class Outcome(enum.Enum):
    WON = "won"
    LOST = "lost"


def judge(total: int, target: int) -> Outcome | None:
    """Classic rule: hitting the target exactly wins, going over loses."""
    if total == target:
        return Outcome.WON
    if total > target:
        return Outcome.LOST
    return None


# Where minus bubbles start and how they drift (levels 6+; two from level 12).
_BUBBLE_PATHS = [((380, 500), (70, -50)), ((520, 140), (-60, 45))]


class LevelSession:
    def __init__(self, spec: LevelSpec, rng: random.Random,
                 difficulty: Difficulty = DEFAULT) -> None:
        d = self.difficulty = difficulty
        self.spec = spec
        self.target = rng.randint(*spec.target_range)
        self.time_left = float(round(spec.time_limit * d.time_scale))
        self.lives = d.lives
        self.invulnerable = 0.0

        self.background = assets.image(spec.theme.background, SCREEN_SIZE)
        self.spinners = [Spinner(s, d.speed_scale, d.hitbox_scale if s.deadly else 1.0)
                         for s in spec.spinners]
        self.rings = [Ring(r, d.speed_scale) for r in spec.rings]
        self.hazards = [Hazard(h, d.speed_scale) for h in spec.hazards]
        self.bubbles: list[MinusBubble] = []
        if d.minus_bubbles and spec.number >= 6:
            count = 1 if spec.number < 12 else 2
            for start, velocity in _BUBBLE_PATHS[:count]:
                v = pygame.Vector2(velocity) * d.speed_scale
                self.bubbles.append(MinusBubble(-rng.randint(1, 5), start, v))
        self.player = Player(d.player_speed)

        self.collected: list[Pickup] = []
        self.popups: list[Popup] = []
        self.events: list[str] = []  # "pickup", "bust", "hit", ... for sound/shake
        self.hud = Hud(spec.number, self.target, spec.theme.color, spec.uses_teens, d.name)

    # -- state --------------------------------------------------------------

    @property
    def total(self) -> int:
        return sum(p.value for p in self.collected)

    @property
    def remaining(self) -> int:
        return self.target - self.total

    def pickups(self):
        for ring in self.rings:
            yield from ring.pickups
        yield from self.bubbles

    def _popup(self, text: str, pos, color=WHITE, size: int = 28) -> None:
        self.popups.append(Popup(text, pos, color, size))

    # -- actions ------------------------------------------------------------

    def undo(self) -> bool:
        """Give back the most recently collected number (costs a little time)."""
        if not self.difficulty.forgiving or not self.collected:
            return False
        pickup = self.collected.pop()
        pickup.release()
        self.time_left -= UNDO_TIME_COST
        self._popup(f"Undo {pickup.value:+d}", self.player.rect.center, WHITE, 24)
        self.events.append("undo")
        return True

    # -- update -------------------------------------------------------------

    def update(self, dt: float, keys) -> Outcome | None:
        self.time_left -= dt
        self.invulnerable = max(0.0, self.invulnerable - dt)
        self.player.update(dt, keys)
        for obj in (*self.spinners, *self.rings, *self.hazards, *self.bubbles, *self.popups):
            obj.update(dt)
        self.popups = [p for p in self.popups if p.alive]

        for p in self.pickups():
            if p.available and self.player.touches(p.mask, p.rect):
                p.collected = True
                self.collected.append(p)
                self._popup(f"{p.value:+d}", p.rect.center, GOOD if p.value > 0 else BAD)
                self.events.append("pickup" if p.value > 0 else "minus")

        if self.total > self.target:
            if not self.difficulty.forgiving:
                return Outcome.LOST
            while self.total > self.target and self.collected:
                self.collected.pop().release()
            self._popup("Too much!", self.player.rect.center, BAD, 34)
            self.events.append("bust")

        if self.total == self.target:
            return Outcome.WON

        if self.invulnerable <= 0:
            deadly = [s for s in self.spinners if s.spec.deadly] + self.hazards
            if any(d.touches(self.player) for d in deadly):
                self.lives -= 1
                if self.lives <= 0:
                    return Outcome.LOST
                self.invulnerable = INVULNERABLE_SECONDS
                left = f"{self.lives} {'life' if self.lives == 1 else 'lives'} left"
                self._popup(f"Ouch! {left}", self.player.rect.center, BAD, 28)
                self.events.append("hit")

        if self.time_left <= 0:
            return Outcome.LOST
        return None

    # -- draw ---------------------------------------------------------------

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.background, (0, 0))
        for spinner in self.spinners:
            spinner.draw(screen)
        for hazard in self.hazards:
            hazard.draw(screen)
        hint = self.remaining if self.difficulty.hints else None
        for p in self.pickups():
            p.draw(screen, hint)
        # Blink while invulnerable.
        visible = self.invulnerable <= 0 or int(self.invulnerable * 10) % 2 == 0
        self.player.draw(screen, visible)
        for popup in self.popups:
            popup.draw(screen)
        self.hud.draw(screen, self.total, self.remaining,
                      {p.value for p in self.collected}, self.time_left,
                      self.lives, self.difficulty.lives)
