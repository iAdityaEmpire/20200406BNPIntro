#!/usr/bin/env python

value = 56

if value > 75:
    print("wombat")
    print("quokka")
    if value > 60:
        print("blue-ringed octopus")
elif value > 50:   # elif == else if
    print("wallaby")
    print("kookaburra")
else:
    print("kangaroo")
    print("platypus")

print("Done.")

# numbers
#  0 is false, non-0 is true

# things with a length  (str, list, tuple, bytes, dict, set, etc)
#  len(0) is false, len(0) != 0  is true

#  A ? B : C


# B if A else C

mode = 'DEBUG'

color = 'red' if mode == 'DEBUG' else 'blue'

#  == != > < >= <=

#  and or not

if (value > 50) and (value < 100):
    print("whoo-hoo")

if (value < 10) or (value > 50):
    print('whoooooooo')
















