#!/usr/bin/env python
from carddeck import CardDeck

class JokerDeck(CardDeck):

    def _make_cards(self):
        super()._make_cards()  # call parent class's method
        self._cards.append('1-Joker')
        self._cards.append('2-Joker')


