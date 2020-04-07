#!/usr/bin/env python
from pprint import pprint

d1 = dict()
d2 = {'123': "Bob", "456": "Anit"}
d3 = {}

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['MCI'])
print("MCI" in airports)
print("LGA" in airports)
print("JFK" in airports)
print("EWR" in airports)

airports['JFK'] = 'Kennedy'
airports['LGA'] = 'LaGuardia'

print(airports, '\n')

print(len(airports))
print(airports.keys(), '\n')
print(airports.values(), '\n')

#for   KEY,   VALUE in  DICT.items():
for abbr, name in airports.items():
    print(abbr, name)
print()

print(list(airports.items()), '\n')


airport_abbrs = ['MCI', 'RDU', 'LAX', 'SEA', 'PDX', 'LGA']

for abbr in airport_abbrs:
    print(abbr, airports.get(abbr, "NOT FOUND"))
print()

del airports['ABQ']

pprint(airports)


