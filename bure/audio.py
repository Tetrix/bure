"""Tiny synthesized sound effects (no sound files needed).

If no audio device is available the game simply stays silent.
"""

from __future__ import annotations

import math
from array import array

import pygame

# name -> list of (frequency Hz, seconds, waveform)
_SOUNDS = {
    "pickup": [(880, 0.05, "sine"), (1320, 0.08, "sine")],
    "minus": [(660, 0.05, "sine"), (440, 0.08, "sine")],
    "undo": [(600, 0.05, "sine"), (400, 0.07, "sine")],
    "bust": [(220, 0.10, "square"), (165, 0.18, "square")],
    "hit": [(140, 0.22, "square")],
    "win": [(523, 0.09, "sine"), (659, 0.09, "sine"), (784, 0.09, "sine"), (1047, 0.25, "sine")],
    "lose": [(392, 0.14, "square"), (330, 0.14, "square"), (262, 0.30, "square")],
    "click": [(700, 0.035, "sine")],
}
_VOLUME = 0.25


def _synth(notes, rate: int, channels: int) -> array:
    samples = array("h")
    for freq, seconds, wave in notes:
        n = int(rate * seconds)
        for i in range(n):
            phase = math.sin(2 * math.pi * freq * i / rate)
            value = phase if wave == "sine" else (1.0 if phase >= 0 else -1.0) * 0.5
            envelope = min(1.0, i / (rate * 0.005)) * (1 - i / n)  # quick attack, fade out
            sample = int(32767 * _VOLUME * value * envelope)
            samples.extend([sample] * channels)
    return samples


class Audio:
    def __init__(self) -> None:
        self.sounds: dict[str, pygame.mixer.Sound] = {}
        self.muted = False
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            rate, size, channels = pygame.mixer.get_init()
            if abs(size) != 16:
                return
            for name, notes in _SOUNDS.items():
                self.sounds[name] = pygame.mixer.Sound(buffer=_synth(notes, rate, channels).tobytes())
        except (pygame.error, TypeError):
            self.sounds = {}

    def play(self, name: str) -> None:
        if not self.muted and name in self.sounds:
            self.sounds[name].play()

    def toggle_mute(self) -> None:
        self.muted = not self.muted
