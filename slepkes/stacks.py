from constants import *
from random import shuffle

class Stack(Rect):

    def __init__(self, topleft):
        self.topleft = topleft
        self.cards = []
        Rect.__init__(self, topleft, CARDSIZE)
        self.origin = None

    def append_cards(self, cardlist):
        self.cards += cardlist

    def empty(self):
        del self.cards[:]

    def reverse(self):
        cards = []
        for c in reversed(self.cards):
            cards.append(c)

        self.cards = cards

    def cover_all(self):
        for c in self.cards:
            if not c.covered:
                c.cover()

    def uncover(self):
        try:
            self.cards[-1].uncover()
        except:
            pass

    def shuffle(self):
        shuffle(self.cards)

class Suit_Stack(Stack):

    def __init__(self, topleft, suit):
        Stack.__init__(self, topleft)
        self.suit = suit
        self.boardmark = load_image(SPRITES_PATH, "slot.png", True)

class Stock(Stack):

    def __init__(self, topleft):
        Stack.__init__(self, topleft) # inherit from Stack class
        self.empty_boardmark = load_image(SPRITES_PATH, "stock_empty.png", True)
        self.boardmark = load_image(SPRITES_PATH, "stock_boardmark.png", True)
