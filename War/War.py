"""This is my file for my game of War!"""

import random
import itertools

suits= ['heart', spade, diamond, club]
values = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'Joker', 'Queen', 'King', 'Ace']
len(suits)
len(value)
cards_in_deck = suits + value

class Card():
    """docstring for Cards."""
    def __init__(self, suits, values):
        self.suits = suit
        self.values = value

    def __str__(self):
        return "%s of %s" % (self.suit, self.value)

class Deck():
    """docstring for Deck."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def shuffle(self):
        deck_len = len(self.deck) - 1
        for i in range(deck_len, 0, -1):
            ran = random.randint(0, i)
            if ran == i:
                continue
            self.deck[i], self.deck[ran] = self.deck[ran], self.deck[i]
        return self.deck

    def getCut(self):

    def __str__(self):
        return card
