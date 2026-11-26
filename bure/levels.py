"""Level definitions.

Every level is plain data: which spinning wheels/stars are on screen, which
numbers orbit where, what bouncing hazards exist, the time limit and the range
the random target sum is drawn from.  The original game had one hand-copied
200-line function per level; the numbers below are taken from those functions
so the levels play the same way.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field

# The original code advanced each number's orbit by a fixed amount *per frame*
# at 50 FPS, using an angle step of (2 * 3.14) / 7.2 radians per unit.
# These helpers convert those values to frame-rate independent degrees.
_ORIGINAL_UNIT_DEG = math.degrees((2 * 3.14) / 7.2)
_ORIGINAL_FPS = 50

# Spinners rotated at (multiplier * -50) degrees per second.
_BASE_SPIN = -50.0


def _orbit_speed(per_frame: float) -> float:
    """Degrees per second for an original per-frame orbit increment."""
    return per_frame * _ORIGINAL_UNIT_DEG * _ORIGINAL_FPS


def _phase(units: float) -> float:
    """Starting angle (degrees) for an original orbit phase value."""
    return (units * _ORIGINAL_UNIT_DEG) % 360


@dataclass(frozen=True)
class Theme:
    background: str
    wheel: str
    star: str  # used by the single-wheel levels
    big_star: str
    small_star: str
    color: tuple[int, int, int]


THEMES = {
    1: Theme("level1/bg_lvl1.png", "level1/wheel.png", "level1/star.png",
             "level1/star.png", "level1/star.png", (157, 186, 236)),
    2: Theme("level2/bg_lv2.png", "level2/wheel.png", "level2/big_star.png",
             "level2/big_star.png", "level2/small_star.png", (95, 172, 93)),
    3: Theme("level3/bg_lv3.png", "level3/wheel.png", "level3/big_star.png",
             "level3/big_star.png", "level3/small_star.png", (249, 198, 218)),
}


@dataclass(frozen=True)
class SpinnerSpec:
    """A rotating image. Deadly spinners (the stars) end the level on touch."""
    image: str
    size: tuple[int, int]
    center: tuple[int, int]
    speed: float  # degrees per second
    deadly: bool


@dataclass(frozen=True)
class RingSpec:
    """Numbers orbiting a common centre. ``slots`` holds (value, start angle)."""
    center: tuple[int, int]
    radius: int
    speed: float  # degrees per second
    slots: tuple[tuple[int, float], ...]


@dataclass(frozen=True)
class HazardSpec:
    """A sprite bouncing off the screen edges."""
    start: tuple[float, float]
    velocity: tuple[float, float]
    size: int = 60


@dataclass(frozen=True)
class LevelSpec:
    number: int
    theme: Theme
    target_range: tuple[int, int]
    time_limit: float
    spinners: tuple[SpinnerSpec, ...]
    rings: tuple[RingSpec, ...]
    hazards: tuple[HazardSpec, ...] = field(default=())

    @property
    def values(self) -> list[int]:
        return sorted(v for ring in self.rings for v, _ in ring.slots)

    @property
    def uses_teens(self) -> bool:
        return any(v > 9 for v in self.values)


# --------------------------------------------------------------------------
# Levels 1-5: one wheel, one star, the numbers 1-9 on a single ring.
# --------------------------------------------------------------------------

_SINGLE_RING_SLOTS = tuple(
    (value, _phase(units)) for value, units in [
        (1, 26200000), (2, 10000000), (3, 31600000), (4, 15400000),
        (5, 28900000), (6, 12700000), (7, 18100000), (8, 23500000),
        (9, 20800000),
    ]
)

def _single(number, target, time_limit, star_spin, orbit, wheel_size=470):
    theme = THEMES[1]
    return LevelSpec(
        number=number,
        theme=theme,
        target_range=target,
        time_limit=time_limit,
        spinners=(
            SpinnerSpec(theme.wheel, (wheel_size, wheel_size), (450, 300),
                        _BASE_SPIN, deadly=False),
            SpinnerSpec(theme.star, (470, 470), (447, 302),
                        star_spin * _BASE_SPIN, deadly=True),
        ),
        rings=(RingSpec((420, 280), 150, _orbit_speed(orbit), _SINGLE_RING_SLOTS),),
    )


# --------------------------------------------------------------------------
# Levels 6-17: two wheels with a star each; numbers 1-19 on two rings.
# Each ring has a few fixed numbers plus three that change per level.
# --------------------------------------------------------------------------

def _double(number, theme_id, target, spin, inner, outer, inner_orbit,
            outer_orbit, wheel_sizes=(365, 250), hazards=()):
    """``spin`` = (big wheel, big star, small star, small wheel) multipliers.
    ``inner``/``outer`` = the three level-specific numbers on each ring."""
    theme = THEMES[theme_id]
    big_wheel, big_star, small_star, small_wheel = spin
    a, b, c = inner
    inner_slots = ((2, 1), (a, 2), (4, 3), (5, 4), (b, 6), (8, 5), (c, 0))
    a, b, c = outer
    outer_slots = ((a, 0.9), (12, 11.1), (b, 16.7), (c, 19.8), (19, 21.2))
    return LevelSpec(
        number=number,
        theme=theme,
        target_range=target,
        time_limit=DOUBLE_RING_TIME,
        spinners=(
            SpinnerSpec(theme.wheel, (wheel_sizes[0],) * 2, (257, 360),
                        big_wheel * _BASE_SPIN, deadly=False),
            SpinnerSpec(theme.wheel, (wheel_sizes[1],) * 2, (620, 250),
                        small_wheel * _BASE_SPIN, deadly=False),
            SpinnerSpec(theme.big_star, (350, 350), (257, 360),
                        big_star * _BASE_SPIN, deadly=True),
            SpinnerSpec(theme.small_star, (220, 250), (620, 250),
                        small_star * _BASE_SPIN, deadly=True),
        ),
        rings=(
            RingSpec((235, 340), 110, _orbit_speed(inner_orbit),
                     tuple((v, _phase(u)) for v, u in inner_slots)),
            RingSpec((600, 232), 70, _orbit_speed(outer_orbit),
                     tuple((v, _phase(u)) for v, u in outer_slots)),
        ),
        hazards=tuple(hazards),
    )


# Seconds per attempt on levels 6-17 (the original game gave only 10).
DOUBLE_RING_TIME = 25

_BIG = (385, 270)
_ONE_HAZARD = (HazardSpec((200, 200), (333, 370)),)
_TWO_HAZARDS = (HazardSpec((200, 200), (333, 370)),
                HazardSpec((700, 200), (-333, -370)))

LEVELS: tuple[LevelSpec, ...] = (
    _single(1, (20, 30), 30, 0.45, -0.023),
    _single(2, (20, 30), 30, 0.6, +0.043),
    _single(3, (30, 40), 25, 0.8, -0.027),
    _single(4, (30, 40), 25, 1.0, +0.033),
    _single(5, (40, 44), 25, 0.9, -0.035, wheel_size=650),
    _double(6, 2, (46, 60), (1.0, 1.0, 0.7, 1.0), (3, 7, 9), (1, 14, 6), 0.02, 0.033),
    _double(7, 2, (50, 70), (1.0, 0.9, 0.8, 1.5), (13, 17, 11), (1, 14, 6), 0.022, -0.030),
    _double(8, 2, (48, 58), (1.0, 1.1, 0.7, 1.5), (3, 15, 9), (17, 11, 1), -0.033, 0.026),
    _double(9, 2, (50, 60), (1.0, 1.3, 1.0, 1.5), (1, 7, 11), (14, 3, 6), -0.03, -0.03),
    _double(10, 2, (60, 70), (1.0, 1.1, 0.9, 1.5), (16, 15, 1), (17, 11, 18), 0.033, 0.033,
            _BIG, _ONE_HAZARD),
    _double(11, 2, (50, 60), (1.2, 1.1, 1.1, 1.5), (13, 15, 9), (7, 3, 1), 0.035, -0.030,
            _BIG, _ONE_HAZARD),
    _double(12, 2, (60, 70), (1.2, 1.1, 1.0, 1.5), (17, 15, 11), (7, 13, 8), -0.043, 0.033,
            _BIG, _ONE_HAZARD),
    _double(13, 2, (70, 80), (1.1, 1.1, 1.1, 1.5), (13, 15, 19), (18, 11, 17), -0.043, -0.033,
            _BIG, _ONE_HAZARD),
    _double(14, 2, (50, 70), (1.0, 1.1, 1.0, 1.5), (1, 15, 17), (9, 16, 18), 0.043, 0.033,
            _BIG, (HazardSpec((200, 200), (333, 370), size=50),)),
    _double(15, 3, (60, 80), (1.1, 1.1, 1.1, 1.5), (13, 15, 14), (18, 11, 17), 0.033, -0.033,
            _BIG, _TWO_HAZARDS),
    _double(16, 3, (80, 90), (1.1, 1.1, 1.1, 1.5), (13, 15, 14), (18, 11, 17), -0.043, 0.033,
            _BIG, _TWO_HAZARDS),
    _double(17, 3, (80, 90), (1.0, 1.1, 1.1, 1.5), (13, 15, 14), (18, 11, 17), -0.043, -0.033,
            _BIG, _TWO_HAZARDS),
)
