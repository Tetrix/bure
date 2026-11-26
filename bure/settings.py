"""Global constants: window, timing, layout and asset locations."""

from pathlib import Path

TITLE = "BURE"
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 50

RESOURCES = Path(__file__).resolve().parent / "resources"
HUD_FONT = RESOURCES / "fonts" / "goall.otf"

# How long the "level complete" / "game over" banners stay on screen.
BANNER_SECONDS = 1.0

# Player
PLAYER_SIZE = (35, 35)
PLAYER_START = (100, 100)
# Furthest top-left position the player may reach (keeps the timer row free).
PLAYER_MAX_POS = (SCREEN_WIDTH - PLAYER_SIZE[0], 545)

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
