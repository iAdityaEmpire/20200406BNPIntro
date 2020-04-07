#!/usr/bin/env python
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitlist.txt', 'w') as fruitlist_out:
    for fruit in fruits:
        fruitlist_out.write("{}\n".format(fruit))

with open('DATA/mary.txt') as mary_in:
    with open('mary_upper.txt', 'w') as mary_out:
        for line in mary_in:
            if line.startswith('M'):
                mary_out.write(line.upper())
