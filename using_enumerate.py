#!/usr/bin/env python

cities = ['Buffalo', 'Albany', 'Poughkeepsie', 'Troy', 'Long Island City', 'Schenectady', 'Westchester', 'New Pfaltz', 'Saratoga', 'Elmyra', 'Corning']

for city in cities:
    # city = next(cities)    (more or less...)
    print(city)
print('-' * 60)


for i, city in enumerate(cities):
    print(i, city)
print()

print(list(enumerate(cities)), '\n')

e = enumerate(cities)
print(e)
print("round 1")
for i, city in e:
    print(i, city)

print("round 2")
for i, city in e:
    print(i, city)
print()

r = reversed(cities)
print(r)
for city in r:
    print(city)
print()

r = reversed(cities)
reversed_cities = list(r)

