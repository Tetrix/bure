import pytest

from bure.levels import LEVELS
from bure.settings import RESOURCES


def reachable_sums(values):
    sums = {0}
    for v in values:
        sums |= {s + v for s in sums}
    return sums


def test_seventeen_levels_numbered_in_order():
    assert [lvl.number for lvl in LEVELS] == list(range(1, 18))


@pytest.mark.parametrize("level", LEVELS, ids=lambda l: f"level{l.number}")
def test_every_target_is_reachable(level):
    lo, hi = level.target_range
    sums = reachable_sums(level.values)
    missing = [t for t in range(lo, hi + 1) if t not in sums]
    assert not missing, f"level {level.number} cannot reach {missing}"


@pytest.mark.parametrize("level", LEVELS, ids=lambda l: f"level{l.number}")
def test_assets_exist(level):
    paths = [level.theme.background] + [s.image for s in level.spinners]
    paths += [f"digits/{v}.png" for v in level.values]
    for p in paths:
        assert (RESOURCES / p).is_file(), p


def test_every_level_has_a_deadly_star():
    assert all(any(s.deadly for s in lvl.spinners) for lvl in LEVELS)
