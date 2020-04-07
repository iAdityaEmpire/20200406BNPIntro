#!/usr/bin/env python

list1 = list()
list2 = ['a', 'b', 'c']
list3 = []
print(len(list1), len(list2), len(list3), '\n')

cities = "Albany Poughkeepsie Troy Schenectady".split()

print(cities, '\n')

cities.append("Westchester")
cities.append("New Pfaltz")
print(cities, '\n')

cities.insert(0, "Buffalo")
cities.insert(4, "Long Island City")

print(cities, '\n')

more_cities = ['Saratoga', 'Elmyra', 'Corning']

cities.extend(more_cities)

print(cities[8])

print(cities, '\n')

print(cities[0], cities[5], cities[-1], '\n')


a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]

spam = []
spam.append(a)
spam.append(b)
spam.append(c)

print(spam, '\n')
print(spam[0])
print(spam[2][2])
print(spam[0][-1])
print(spam[-2][-1])

print(cities, '\n')

del cities[7]
print(cities, '\n')

cities.remove('Elmyra')
print(cities, '\n')

print("Troy" in cities)
print("Rome" in cities)
print()

print(cities, '\n')

actor = "Chris Hemsworth"
print(len(actor), actor[0], actor[-1], '\n')

c = cities.pop()
print(c)
print(cities, '\n')

c = cities.pop(3)
print(c)
print(cities, '\n')

cities.append("Rome")
cities.append("Rochester")
cities.append("Ithaca")

print(cities, '\n')

c1 = cities[0:4]   # start at 0, go up to BUT NOT INCLUDING 4
print("c1:", c1, '\n')

c2 = cities[3:9]
print("c2:", c2, '\n')

print(actor[0:5], actor[6:9], actor[-5:])

print(cities[:4], '\n')
print(cities[6:], '\n')

for city in cities:
    # city = cities[0]
    # city = cities[1]
    # city = cities[2]
    # ...
    print(city)
print()

# for VAR, ... in ITERABLE:
#     ....

for city in cities[:5]:
    print(city)
print()

for char in actor:
    print(char, end='/')
print('\n\n')

for city in cities:
    print(city)
print()

for city in reversed(cities):
    print(city)
print()

# what really happens in a 'for' loop
# it = iter(cities)
# while True:
#     try:
#         city = next(it)
#         print(city)
#     except StopIteration:
#         break
# print()





