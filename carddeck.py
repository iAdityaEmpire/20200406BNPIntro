#!/usr/bin/env python
import random


class CardDeck(object):   # inherits from 'object'
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._make_cards()

    #  getters & setters    accessors & mutators

    def _make_cards(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = "{}-{}".format(rank, suit)
                self._cards.append(card)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop(0)

    @property
    def cards(self):
        return self._cards

    @property  # decorator
    def dealer(self):  # getter property
        return self._dealer.title()

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    def __len__(self):
        return len(self._cards)


    def __str__(self):  # "dunder str" method
        my_type = type(self)
        my_name = my_type.__name__
        return "{}({},{})".format(my_name, self.dealer, len(self))
