#!/usr/bin/env python
import sys
print(sys.version)

i1 = 123
i2 = 42203985029385029385203850285
i3 = 1_000_000

print(i3)
print(1_2_3)

i4 = 0x100
i5 = 0b100
i6 = 0o100

print(i4, i5, i6)
print()

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.0093e15

a = 23
b = 9

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # floored division
print(a ** b)
print(a % b)

a += 2  # a = a + 2
a /= 5   # a = a / 5
a *= 20  # etc etc
print(a)

# not implemented:
# a++   a--
# ++a  --a

# PEMDAS

m = "1234"

print(m * 3)

print('-' * 60)

mm = int(m)   # int mm = new int(m);
print(mm)
print(mm * 3)

#  int() float() str() bool()   list() tuple() dict() set()

x = int(123)
print(x * 10)

d = "DEAD_BEEF"
print(int(d, 16))

print(int('   123      '))

x = 5
y = "Humphrey Bogart"
z = 99.99

#       ' '   ' '   '\n'
print(x,    y,    z)

print(x, y, z, sep='/')
print(x, y, z, sep='*')
print(x, y, z, sep=', ')
print(x, y, z, sep='')

print(x)
print(y)
print(z)
print(x, end='/')
print(y, end='*')
print(z)
print()

result = 29 / 9

print(result)

actor = "Tom Hanks"
city = "Hollywood"

print("{:.2f}".format(result))
print("{0:.2f}".format(result))

#    0  1  2   auto-numbered
#  "{} {} {}".format(v0, v1, v2)
#  "{0} {1} {2}".format(v0, v1, v2)
print("{}".format(result))
print("{:09.3f}".format(result))

print("{} {} {}".format('a', 'b', 'c'))
print("{0} {1} {2}".format('a', 'b', 'c'))
print("{1} {2} {0} {2} {0}".format('a', 'b', 'c'))

print(actor, "lives in", city)
print("{} lives in {}".format(actor, city))
print(f"{actor} lives in {city}")

print(f"{result:.2f}")







