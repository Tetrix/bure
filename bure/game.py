"""Main loop and scene flow: menu -> levels -> victory."""

from __future__ import annotations

import random

import pygame

from . import assets
from .audio import Audio
from .difficulty import BY_KEY, DEFAULT, Difficulty
from .effects import Shake
from .levels import LEVELS
from .menu import Menu
from .progress import Progress
from .session import LevelSession, Outcome
from .settings import BANNER_SECONDS, FPS, SCREEN_SIZE, TITLE, WHITE

MENU, PLAYING, BANNER, VICTORY = "menu", "playing", "banner", "victory"


class Game:
    def __init__(self, start_level: int | None = None, seed: int | None = None,
                 difficulty: str | None = None) -> None:
        assets.clear_cache()
        pygame.mixer.pre_init(22050, -16, 1, 512)
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(pygame.image.load(str(assets.RESOURCES / "bure.png")))
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.frame = pygame.Surface(SCREEN_SIZE)  # drawn into, then shaken onto screen
        pygame.mouse.set_visible(False)
        self.clock = pygame.time.Clock()
        self.rng = random.Random(seed)
        self.audio = Audio()
        self.shake = Shake()

        self.progress = Progress.load()
        self.difficulty: Difficulty = BY_KEY.get(difficulty or self.progress.difficulty, DEFAULT)
        self.menu = Menu(self.progress, self.difficulty)

        self.win_banner = assets.image("bugara.png", (600, 300))
        self.lose_banner = assets.image("game-over.png")
        self.banner = None
        self.banner_time = 0.0
        self.after_banner = None
        self.paused = False
        self.level_index = 0
        self.session: LevelSession | None = None
        self.state = MENU
        if start_level is not None:
            self.start(start_level, self.difficulty)

    # -- flow -------------------------------------------------------------

    def start(self, level: int, difficulty: Difficulty) -> None:
        self.difficulty = difficulty
        if self.progress.difficulty != difficulty.key:
            self.progress.difficulty = difficulty.key
            self.progress.save()
        self.level_index = level - 1
        self._restart_level()

    def _restart_level(self) -> None:
        self.session = LevelSession(LEVELS[self.level_index], self.rng, self.difficulty)
        self.paused = False
        self.state = PLAYING

    def _next_level(self) -> None:
        if self.level_index + 1 >= len(LEVELS):
            self.state = VICTORY
            return
        self.level_index += 1
        self._restart_level()

    def _show_banner(self, surface, then) -> None:
        self.banner = surface
        self.banner_time = BANNER_SECONDS
        self.after_banner = then
        self.state = BANNER

    def _to_menu(self) -> None:
        self.menu.level = min(self.level_index + 1, self.progress.unlocked)
        self.state = MENU

    # -- input ------------------------------------------------------------

    def handle_event(self, event) -> bool:
        """Return False when the game should quit."""
        if event.type == pygame.QUIT:
            return False
        if event.type != pygame.KEYDOWN:
            return True
        key = event.key
        if key == pygame.K_m:
            self.audio.toggle_mute()
            return True

        if self.state == MENU:
            action = self.menu.handle_key(key)
            if action == "quit":
                return False
            if action == "move":
                self.audio.play("click")
            elif isinstance(action, tuple):
                self.audio.play("click")
                _, level, difficulty = action
                self.start(level, difficulty)
        elif self.state == PLAYING:
            if key == pygame.K_ESCAPE:
                self._to_menu()
            elif key == pygame.K_p:
                self.paused = not self.paused
            elif key in (pygame.K_BACKSPACE, pygame.K_u) and not self.paused:
                self.session.undo()
        elif self.state == BANNER and key == pygame.K_ESCAPE:
            self._to_menu()
        elif self.state == VICTORY and key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_ESCAPE):
            self.level_index = 0
            self._to_menu()
        return True

    # -- update -----------------------------------------------------------

    def step(self, dt: float) -> None:
        self.shake.update(dt)
        if self.state == BANNER:
            self.banner_time -= dt
            if self.banner_time <= 0:
                self.banner = None
                self.after_banner()
            return
        if self.state != PLAYING or self.paused:
            return

        outcome = self.session.update(dt, pygame.key.get_pressed())
        for event in self.session.events:
            self.audio.play(event)
            if event == "hit":
                self.shake.start(0.3, 8)
        self.session.events.clear()

        if outcome is Outcome.WON:
            self.audio.play("win")
            self.progress.unlock(self.level_index + 2)
            self._show_banner(self.win_banner, self._next_level)
        elif outcome is Outcome.LOST:
            self.audio.play("lose")
            self.shake.start(0.35, 10)
            self._show_banner(self.lose_banner, self._restart_level)

    # -- draw -------------------------------------------------------------

    def draw(self) -> None:
        if self.state == MENU:
            self.menu.draw(self.screen)
        else:
            self.session.draw(self.frame)
            if self.banner is not None:
                self.frame.blit(self.banner, self.banner.get_rect(center=(400, 260)))
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.frame, self.shake.offset)
            if self.paused:
                self._message("Paused",
                              "P: continue    Backspace: undo last number    Esc: menu")
            elif self.state == VICTORY:
                self._message(f"You beat all {len(LEVELS)} levels on {self.difficulty.name}!",
                              "Press Enter to return to the menu")
        pygame.display.flip()

    def _message(self, title: str, subtitle: str) -> None:
        big = assets.font("goall.otf", 44).render(title, True, WHITE)
        small = assets.font("goall.otf", 24).render(subtitle, True, WHITE)
        center = self.screen.get_rect().center
        r1 = big.get_rect(center=(center[0], center[1] - 20))
        r2 = small.get_rect(center=(center[0], center[1] + 30))
        box = r1.union(r2).inflate(50, 36)
        backdrop = pygame.Surface(box.size, pygame.SRCALPHA)
        backdrop.fill((0, 0, 0, 180))
        self.screen.blit(backdrop, box)
        self.screen.blit(big, r1)
        self.screen.blit(small, r2)

    # -- loop -------------------------------------------------------------

    def run(self, max_frames: int | None = None) -> None:
        frames = 0
        running = True
        while running:
            # Cap dt so dragging the window doesn't teleport everything.
            dt = min(self.clock.tick(FPS) / 1000.0, 0.1)
            for event in pygame.event.get():
                running = self.handle_event(event) and running
            self.step(dt)
            self.draw()
            frames += 1
            if max_frames is not None and frames >= max_frames:
                break
        assets.clear_cache()
        pygame.quit()
