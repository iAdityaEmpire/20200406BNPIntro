#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    pass

mary_in = open('DATA/mary.txt')

print(mary_in)

x = 5    #   x = int(5)

print(type(x), type(mary_in))

class Dog:
    def bark(self):
        print("Woof! Woof!")


d = Dog()
print(type(d))

d.bark()

d2 = Dog()
d2.bark()
