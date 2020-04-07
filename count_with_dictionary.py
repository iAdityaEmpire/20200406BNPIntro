#!/usr/bin/env python

food_counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()

        if food not in food_counts:
            food_counts[food] = 0

        food_counts[food] += 1

        # food_counts[food] = food_counts[food] + 1

print(food_counts)

