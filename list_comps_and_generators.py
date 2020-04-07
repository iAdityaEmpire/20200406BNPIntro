#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

#    [EXPR for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

all_food = ['spam', 'spam', 'ham', 'spam', 'spam', 'spam', 'eggs', 'spam']

good_food = [food for food in all_food if food != 'spam']
print("good_food:", good_food, '\n')

good_food = []
for food in all_food:
    if food != 'spam':
        good_food.append(food)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [round(n / 15, 2) for n in nums]
print("n1:", n1, '\n')


all_food = ['spam', 'spam', 'ham', 'spam', 'spam', 'spam', 'eggs', 'spam']

good_food = [f.upper() for f in all_food if f != 'spam']
print("good_food:", good_food, '\n')

fgen = (f.upper() for f in fruits)
print(fgen)

fruits.append("marionberry")

for fruit in fgen:
    print(fruit)
print()

