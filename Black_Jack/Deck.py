from Card.py import *
from random import randint


class Deck:
    suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']

    def __init__(self):
         self.cards = []
         self.build()

    def build(self):
         for suit in Deck.suits:
             for value in range(1, 12):
                 self._cards.append(Card(suit, value))

    def show(self):
         for card in self._cards:
             card.show()

    def shuffle(self):
         for i in range(len(self._cards)-1, 0, -1):
             rand = random.randint(0, i)
             self._cards[i], self._cards[rand] = self._cards[rand], self._cards[rand

    def draw(self):
        if self._cards:
            return self._cards.pop()