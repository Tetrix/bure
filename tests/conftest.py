import os
import tempfile

os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
os.environ.setdefault("SDL_AUDIODRIVER", "dummy")
os.environ.setdefault("PYGAME_HIDE_SUPPORT_PROMPT", "1")
# Never touch the player's real save file.
os.environ["BURE_SAVE_FILE"] = os.path.join(tempfile.mkdtemp(), "progress.json")
