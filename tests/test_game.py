import random

import pygame
import pytest

from bure.difficulty import BY_KEY, DIFFICULTIES
from bure.game import Game
from bure.levels import LEVELS
from bure.progress import Progress
from bure.session import LevelSession, Outcome, judge

EASY, NORMAL, CLASSIC = BY_KEY["easy"], BY_KEY["normal"], BY_KEY["classic"]


@pytest.fixture(autouse=True)
def game():
    g = Game(seed=1)  # initialises pygame and a display for the sessions
    yield g
    pygame.quit()


class NoKeys:
    def __getitem__(self, key):
        return False


def session(level=1, difficulty=NORMAL, seed=0):
    s = LevelSession(LEVELS[level - 1], random.Random(seed), difficulty)
    s.spinners = [sp for sp in s.spinners if not sp.spec.deadly]  # no accidental hits
    s.hazards = []
    return s


def grab(s, value):
    """Teleport onto the first available pickup with ``value`` and step once."""
    p = next(p for p in s.pickups() if p.value == value and p.available)
    s.player.pos.update(p.rect.topleft)
    return s.update(0, NoKeys())


def test_judge():
    assert judge(10, 20) is None
    assert judge(20, 20) is Outcome.WON
    assert judge(21, 20) is Outcome.LOST


@pytest.mark.parametrize("difficulty", DIFFICULTIES, ids=lambda d: d.key)
def test_targets_and_time(difficulty):
    for spec in LEVELS:
        s = LevelSession(spec, random.Random(0), difficulty)
        assert spec.target_range[0] <= s.target <= spec.target_range[1]
        assert s.time_left == round(spec.time_limit * difficulty.time_scale)
        assert s.lives == difficulty.lives


def test_exact_target_wins():
    s = session()
    s.target = 9
    assert grab(s, 9) is Outcome.WON


def test_overshoot_gives_number_back_in_normal():
    s = session()
    s.target = 10
    assert grab(s, 9) is None
    assert grab(s, 5) is None  # 14 > 10: the 5 is returned
    assert s.total == 9
    assert "bust" in s.events
    returned = next(p for p in s.pickups() if p.value == 5)
    assert not returned.collected and not returned.available  # cooling down


def test_overshoot_loses_in_classic():
    s = session(difficulty=CLASSIC)
    s.target = 10
    grab(s, 9)
    assert grab(s, 5) is Outcome.LOST


def test_undo():
    s = session()
    s.target = 30
    grab(s, 7)
    before = s.time_left
    assert s.undo()
    assert s.total == 0 and s.time_left == before - 2
    assert not session(difficulty=CLASSIC).undo()


def test_star_costs_a_life_then_brief_invulnerability():
    s = LevelSession(LEVELS[0], random.Random(0), NORMAL)
    star = next(sp for sp in s.spinners if sp.spec.deadly)
    s.player.pos.update(star.rect.center)
    assert s.update(0, NoKeys()) is None
    assert s.lives == NORMAL.lives - 1 and s.invulnerable > 0
    assert s.update(0, NoKeys()) is None  # still invulnerable: no second hit
    assert s.lives == NORMAL.lives - 1


def test_last_life_loses():
    s = LevelSession(LEVELS[0], random.Random(0), CLASSIC)
    star = next(sp for sp in s.spinners if sp.spec.deadly)
    s.player.pos.update(star.rect.center)
    assert s.update(0, NoKeys()) is Outcome.LOST


def test_timeout_loses():
    s = session()
    s.player.pos.update(0, 545)
    outcome = None
    for _ in range(60 * 50):
        outcome = s.update(1 / 50, NoKeys())
        if outcome:
            break
    assert outcome is Outcome.LOST and s.time_left <= 0


def test_minus_bubbles():
    assert not session(5).bubbles
    assert len(session(6).bubbles) == 1
    assert len(session(12).bubbles) == 2
    assert not session(12, CLASSIC).bubbles
    s = session(6)
    s.target = 50
    grab(s, 9)
    bubble = s.bubbles[0]
    s.player.pos.update(bubble.rect.topleft)
    s.update(0, NoKeys())
    assert s.total == 9 + bubble.value


def test_winning_unlocks_next_level(game):
    game.start(1, NORMAL)
    game.session.target = 9
    game.session.spinners = []
    p = next(p for p in game.session.pickups() if p.value == 9)
    game.session.player.pos.update(p.rect.topleft)
    game.step(0)
    assert game.progress.unlocked >= 2
    assert Progress.load().unlocked >= 2  # saved to disk
    game.step(2.0)  # banner finishes
    assert game.level_index == 1


def test_menu_starts_game(game):
    assert game.state == "menu"
    enter = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
    game.handle_event(enter)
    assert game.state == "playing"


@pytest.mark.parametrize("difficulty", [d.key for d in DIFFICULTIES])
@pytest.mark.parametrize("level", range(1, 18))
def test_every_level_runs(level, difficulty):
    pygame.quit()
    Game(start_level=level, seed=level, difficulty=difficulty).run(max_frames=40)
