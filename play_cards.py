#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("annE")

print(d1)
print(type(d1))

d2 = CardDeck("lisa")

a = d1
b = str(d1)
print(b)

print(d1.dealer)
print(d2.dealer)

# print(d1.get_dealer())

print(d2.dealer)
print(d1.dealer)

d1.dealer = "Steve"

print(d1.dealer)

d1.shuffle()
print(d1.cards)
print()

for _ in range(7):
    print(d1.draw())
print()

print(d1.get_ranks())
print(CardDeck.get_ranks())


j1 = JokerDeck("Bob")
j2 = JokerDeck("Jimmy")

print(j1)
print(j1.dealer)
j1.shuffle()
print(j1.cards)

print(d1, j1)

print(len(d1))
print(len(j1))
