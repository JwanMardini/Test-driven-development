"""The intelligence class represents the CPU as a player. The class is inherited from Player class."""
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Player.player import Player


class Intelligence(Player):
    """Methods for the CPU to function."""

    def __init__(self, mode, score) -> None:
        """Init a mode instance of Intelligence Class."""
        super().__init__("CPU", score)
        self._mode = mode

    def get_mode(self):
        """Mode instance is returned."""
        return self._mode

    def set_score(self, new_score):
        """Score for the CPU player is set."""
        self._score = new_score

    def get_score(self):
        """Score for the CPU player is returned."""
        return self._score
