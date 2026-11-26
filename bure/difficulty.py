"""Difficulty modes."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Difficulty:
    key: str
    name: str
    description: str
    lives: int
    time_scale: float  # multiplies each level's time limit
    speed_scale: float  # multiplies spin, orbit and hazard speeds
    player_speed: float  # pixels per second
    forgiving: bool  # going over the target gives the number back; undo allowed
    hints: bool  # highlight numbers that finish / would overshoot the target
    minus_bubbles: bool  # floating negative numbers from level 6 on
    hitbox_scale: float  # star hitbox size relative to the picture


DIFFICULTIES: tuple[Difficulty, ...] = (
    Difficulty("easy", "Easy", "5 lives, extra time, slower stars, hints",
               lives=5, time_scale=1.4, speed_scale=0.75, player_speed=230,
               forgiving=True, hints=True, minus_bubbles=True, hitbox_scale=0.8),
    Difficulty("normal", "Normal", "3 lives, going over gives the number back",
               lives=3, time_scale=1.0, speed_scale=1.0, player_speed=220,
               forgiving=True, hints=False, minus_bubbles=True, hitbox_scale=0.85),
    Difficulty("classic", "Classic", "The original 2015 rules: one touch and you restart",
               lives=1, time_scale=0.4, speed_scale=1.0, player_speed=170,
               forgiving=False, hints=False, minus_bubbles=False, hitbox_scale=1.0),
)

BY_KEY = {d.key: d for d in DIFFICULTIES}
DEFAULT = BY_KEY["normal"]
