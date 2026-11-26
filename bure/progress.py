"""Saves which levels are unlocked and the last chosen difficulty."""

from __future__ import annotations

import json
import os
from pathlib import Path

from .levels import LEVELS


def save_path() -> Path:
    if "BURE_SAVE_FILE" in os.environ:
        return Path(os.environ["BURE_SAVE_FILE"])
    if os.name == "nt":
        base = Path(os.environ.get("APPDATA", Path.home()))
    else:
        base = Path(os.environ.get("XDG_DATA_HOME", Path.home() / ".local" / "share"))
    return base / "bure" / "progress.json"


class Progress:
    def __init__(self, unlocked: int = 1, difficulty: str = "normal") -> None:
        self.unlocked = unlocked
        self.difficulty = difficulty

    @classmethod
    def load(cls) -> "Progress":
        try:
            data = json.loads(save_path().read_text())
            unlocked = int(data.get("unlocked", 1))
            return cls(min(max(unlocked, 1), len(LEVELS)), str(data.get("difficulty", "normal")))
        except (OSError, ValueError, TypeError, AttributeError):
            return cls()

    def save(self) -> None:
        path = save_path()
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"unlocked": self.unlocked, "difficulty": self.difficulty}))
        except OSError:
            pass  # not being able to save progress shouldn't crash the game

    def unlock(self, level: int) -> None:
        if level > self.unlocked:
            self.unlocked = min(level, len(LEVELS))
            self.save()
