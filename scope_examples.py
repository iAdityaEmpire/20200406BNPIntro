#!/usr/bin/env python

x = 100   # global variables

actor = "Chris Hemsworth"  # global

def spam():
    print("In spam(): x is", x)
    actor = "Liam Hemsworth"   # local variable

spam()

print("In main: actor is:", actor)



