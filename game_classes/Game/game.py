"""The class game shows the layout of the game and represents the rules of the game."""
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class Game:
    """Methods used for layouts and rules."""

    def __init__(self):
        """Init by creating instances of Game class."""
        self._header = "***************************\n" + "--- Welcome to pig dice ---\n" + "***************************"
        self._turn = 1
        self._start_menu = "Enter 1 for one player game\nEnter 2 for two players game"
        self._option_menu = '''Press 1 to change name
Press 2 to quit game\nPress 3 to roll\nPress 4 to cheat\n'''
        self._difficulty_menu = '''Enter (e) for easy mode and (h) for hard mode: '''

    def header(self):
        """Return the instance variable 'header'."""
        return self._header

    def end_game(self, name, high_score):
        """Print the name of the winning player and their score."""
        print(f"The winner is {name}, and your score is {high_score}")

    def set_turn(self, new_turn):
        """Set turn of the player."""
        self._turn = new_turn

    def get_turn(self):
        """Get turn of the player."""
        return self._turn

    def get_startmenu(self):
        """Start menu is returned."""
        return self._start_menu

    def get_optionmenu(self):
        """Option menu is returned and displayed."""
        return self._option_menu

    def get_difficultymenu(self):
        """Sifficulty menu is obtained for optional gameplay."""
        return self._difficulty_menu

    def get_rules(self):
        """Rules are returned to be displayed in the game."""
        return """1. Players take turns with a die.
2. On a player’s turn he/she can roll a die as many times as they like.
3. If a roll is a 2, 3, 4, 5, or 6, the player adds that many points to their score for the turn.
4. A player may choose to end their turn at any time and “bank” their points.
5. If a player rolls a 1, they lose all their unbanked points and their turn is over."""
