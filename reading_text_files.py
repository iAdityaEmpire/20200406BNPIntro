#!/usr/bin/env python

# with open(FILENAME) as FILE_OBJ:
#     pass
junk = ['a', 'b', 'c']
for j in junk:
    print(j)
print()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:  # calls mary_in.readline() until end of file
        # print(raw_line)  #   "raw line\n" + "\n"
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()  # read entire file into one string
    print("raw:")
    print(repr(contents))
    print("normal:")
    print(contents)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/numeric_data.txt') as num_in:
    data = [int(line) for line in num_in]
    print(data)
print('-' * 60)

