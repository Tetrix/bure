"""Loads images and fonts once and hands out cached copies."""

from __future__ import annotations

from functools import lru_cache

import pygame

from .settings import RESOURCES


@lru_cache(maxsize=None)
def image(name: str, size: tuple[int, int] | None = None) -> pygame.Surface:
    """Load ``resources/<name>``, optionally scaled, keeping its alpha channel."""
    surface = pygame.image.load(str(RESOURCES / name)).convert_alpha()
    if size is not None:
        surface = pygame.transform.smoothscale(surface, size)
    return surface


@lru_cache(maxsize=None)
def font(name: str, size: int) -> pygame.font.Font:
    return pygame.font.Font(str(RESOURCES / "fonts" / name), size)


def digit(value: int) -> pygame.Surface:
    return image(f"digits/{value}.png")


def clear_cache() -> None:
    """Drop cached surfaces/fonts (they become invalid after ``pygame.quit()``)."""
    image.cache_clear()
    font.cache_clear()
