"""The text overlay shown while playing."""

from __future__ import annotations

import math

import pygame

from . import assets
from .settings import BLACK

DANGER_RED = (235, 60, 60)
HEART_RED = (230, 50, 80)


def draw_heart(screen: pygame.Surface, center, size: int, color) -> None:
    x, y = center
    r = size // 4
    pygame.draw.circle(screen, color, (x - r, y - r // 2), r)
    pygame.draw.circle(screen, color, (x + r, y - r // 2), r)
    pygame.draw.polygon(screen, color, [(x - 2 * r, y - r // 3), (x + 2 * r, y - r // 3), (x, y + 2 * r)])


class Hud:
    """Renders the HUD, re-rendering a piece of text only when it changes."""

    STRIP_SHORT = "|  1 2 3 4 5 6 7 8 9 "
    STRIP_LONG = "|  1 2 3 4 5 6 7 8 9 11 12 13 14 15 16 17 18 19 |"

    def __init__(self, level_number: int, target: int, color, uses_teens: bool,
                 difficulty_name: str) -> None:
        self.color = color
        self.small = assets.font("goall.otf", 30)
        self.big = assets.font("goall.otf", 60)
        self._cache: dict[tuple, pygame.Surface] = {}

        self.static = [
            (self._text("The number you need to get is: "), (10, 10)),
            (self._text(str(target)), (435, 10)),
            (self._text("Level: "), (650, 10)),
            (self._text(str(level_number)), (735, 10)),
            (self._text("The sum"), (650, 470)),
            (self._text("Time left: "), (50, 550)),
            (assets.font("goall.otf", 22).render(difficulty_name, True, color), (690, 570)),
        ]
        # Lay out the number strip token by token so collected numbers can be
        # blacked out exactly where they sit in the full string.
        strip = self.STRIP_LONG if uses_teens else self.STRIP_SHORT
        parts = strip.split(" ")
        self.strip = []
        for i, token in enumerate(parts):
            if token:
                prefix = " ".join(parts[:i]) + (" " if i else "")
                self.strip.append((token, 50 + self.small.size(prefix)[0]))

    def _text(self, text: str, color=None, font=None) -> pygame.Surface:
        color = color or self.color
        font = font or self.small
        key = (text, color, id(font))
        if key not in self._cache:
            self._cache[key] = font.render(text, True, color)
        return self._cache[key]

    def draw(self, screen, total: int, remaining: int, collected: set[int],
             time_left: float, lives: int, max_lives: int) -> None:
        for surface, pos in self.static:
            screen.blit(surface, pos)
        for token, x in self.strip:
            color = BLACK if token.isdigit() and int(token) in collected else self.color
            screen.blit(self._text(token, color), (x, 60))

        screen.blit(self._text(f"Still need: {remaining}"), (600, 430))
        screen.blit(self._text(str(total), font=self.big), (680, 500))

        seconds = max(0, math.ceil(time_left))
        timer_color = DANGER_RED if seconds <= 5 else self.color
        screen.blit(self._text(str(seconds), timer_color), (200, 550))

        if max_lives > 1:
            for i in range(max_lives):
                color = HEART_RED if i < lives else (90, 90, 90)
                draw_heart(screen, (330 + i * 34, 568), 26, color)
