#!/usr/bin/env python

import re
from random import randint


class HangedMan():
    def __init__(self):
        self.word_list = ["car", "pillow", "phone", "spider",
                          "human", "see", "pity", "pun", "hardy",
                          "engine", "frame", "turntable", "scheme",
                          "echo", "barring", "fat", "a", "target", "mileage"]
        self.chosen = self.word_list[randint(0, len(self.word_list) - 1)]
        self.chances = 6

    def check_word(self, word, other_word):
        """Check if the words are alike.
        Returns: True if they are alike, false otherwise."""

        return word.upper() == other_word.upper()

    def check_letter(self, letter, word):
        """Check the occurrences of a letter in a word.
        Returns: a list with the index of occurrences."""

        return [m.start() for m in re.finditer(letter, word)]

    def start_game(self):
        """Starts the game."""

        print("Welcome to The Hanged Man Game")
        print("I'm thinking in a word right now. You have %d chances to guess." % self.chances)
        input_word = "_" * len(self.chosen)
        self.play(input_word)

    def win_screen(self):
        """Prints a winning screen."""

        print("Great, you guessed the word. It's '%s'." % self.chosen)

    def lose_screen(self):
        """Prints a game over screen."""

        print("Sorry, you lost. The word it's '%s'." % self.chosen)

    def play(self, input_word):
        """Play the game. It uses recursion, instead of a loop."""

        print("Guess the missing letters")
        print(" ".join(input_word))
        input_text = input("Which letter shall be? ")
        if len(input_text) == 0:
            input_text = ' '
        letter = input_text[0]
        check = self.check_letter(letter, self.chosen)

        if len(check) == 0:
            print("You guessed wrong.")
            self.chances -= 1
            if self.chances == 0:
                print("You have no chances.")
                self.lose_screen()
            else:
                print("You have %d chances." % self.chances)
                self.play(input_word)
        else:
            print("Fine. The word has that letter")
            input_word = list(input_word)
            for n in check:
                input_word[n] = letter
            input_word = ''.join(input_word)
            self.play(input_word)

        if self.check_word(input_word, self.chosen):
            self.win_screen()


if __name__ == '__main__':
    game = HangedMan()
    game.start_game()
