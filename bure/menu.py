"""Title screen: choose difficulty and starting level."""

from __future__ import annotations

import pygame

from . import assets
from .difficulty import DIFFICULTIES, Difficulty
from .levels import LEVELS
from .progress import Progress
from .settings import SCREEN_SIZE, WHITE

ACCENT = (255, 214, 90)
MUTED = (190, 200, 220)


class Menu:
    ROWS = ("difficulty", "level", "play", "quit")

    def __init__(self, progress: Progress, difficulty: Difficulty) -> None:
        self.progress = progress
        self.diff_index = DIFFICULTIES.index(difficulty)
        self.level = progress.unlocked
        self.row = self.ROWS.index("play")

    @property
    def difficulty(self) -> Difficulty:
        return DIFFICULTIES[self.diff_index]

    def handle_key(self, key: int):
        """Returns ("start", level, difficulty), "quit", "move" or None."""
        row = self.ROWS[self.row]
        if key in (pygame.K_UP, pygame.K_w):
            self.row = (self.row - 1) % len(self.ROWS)
            return "move"
        if key in (pygame.K_DOWN, pygame.K_s):
            self.row = (self.row + 1) % len(self.ROWS)
            return "move"
        if key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_a, pygame.K_d):
            step = -1 if key in (pygame.K_LEFT, pygame.K_a) else 1
            if row == "difficulty":
                self.diff_index = (self.diff_index + step) % len(DIFFICULTIES)
                return "move"
            if row == "level":
                self.level = min(max(self.level + step, 1), self.progress.unlocked)
                return "move"
        if key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE):
            return "quit" if row == "quit" else ("start", self.level, self.difficulty)
        if key == pygame.K_ESCAPE:
            return "quit"
        return None

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(assets.image("level1/bg_lvl1.png", SCREEN_SIZE), (0, 0))
        shade = pygame.Surface(SCREEN_SIZE, pygame.SRCALPHA)
        shade.fill((0, 0, 20, 120))
        screen.blit(shade, (0, 0))

        cx = SCREEN_SIZE[0] // 2
        self._center(screen, "BURE", 110, ACCENT, 95)
        self._center(screen, "Collect numbers that add up to the target", 28, MUTED, 175)
        penguin = assets.image("penguin.png", (70, 70))
        screen.blit(penguin, penguin.get_rect(center=(cx + 170, 100)))

        rows = {
            "difficulty": (f"Difficulty:  {self.difficulty.name}", 255, True),
            "level": (f"Start at level:  {self.level}", 355, True),
            "play": ("Play", 450, False),
            "quit": ("Quit", 510, False),
        }
        for i, name in enumerate(self.ROWS):
            text, y, adjustable = rows[name]
            selected = i == self.row
            rect = self._center(screen, text, 40, ACCENT if selected else WHITE, y)
            if selected:
                # The HUD font has no < > glyphs, so draw the arrows.
                left, right = ("<", ">") if adjustable else (">", "<")
                self._arrow(screen, rect.left - 28, rect.centery, left)
                self._arrow(screen, rect.right + 28, rect.centery, right)

        self._center(screen, self.difficulty.description, 26, MUTED, 297)
        self._center(screen, f"Levels unlocked: {self.progress.unlocked} of {len(LEVELS)}",
                     24, MUTED, 395)
        self._center(screen, "Arrows / WASD: choose    Enter: select    M: mute    Esc: quit",
                     22, MUTED, 565)

    @staticmethod
    def _arrow(screen, x, y, direction) -> None:
        d = -1 if direction == "<" else 1
        pygame.draw.polygon(screen, ACCENT, [(x - 9 * d, y - 11), (x - 9 * d, y + 11), (x + 9 * d, y)])

    @staticmethod
    def _center(screen, text, size, color, y) -> pygame.Rect:
        surface = assets.font("goall.otf", size).render(text, True, color)
        rect = surface.get_rect(center=(SCREEN_SIZE[0] // 2, y))
        screen.blit(surface, rect)
        return rect
