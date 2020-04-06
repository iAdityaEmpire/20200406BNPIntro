#!/usr/bin/env python

s1 = "spam\n"
#  \n \t \r \b \f
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'''spam\n'''

print("Guido's the BDFL of Python")
print('Guido is the "BDFL" of Python')

print('''Guido's the "BDFL" of Python''')
print()

path = r'c:\Users\RobertG\Desktop\py3bnpintro'

actor = "Chris Hemsworth"

print(actor)
print(len(actor))   #  actor.__len__()
# print(actor.__len__())  # don't do this
print(actor.upper())
print(actor.lower())
print(actor.count('h'))
print(actor.count('H'))
print(actor.lower().count('h'))

print(actor.startswith('Chris'))
print(actor.startswith('Liam'))

s = "            Guido Van Rossum              "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")

s = "gxgghhhxxhiGuido Van Rossumhhgxxissvvaa"
print("|" + s.lstrip("gxhisva") + "|")
print("|" + s.rstrip("gxhisva") + "|")
print("|" + s.strip("gxhisva") + "|")

print(s.strip('ghxisva').replace('a', 'A'))
print(s.strip('ghxisva').replace('a', ''))
print(s.strip('ghxisva').replace('a', 'a').replace('i', 'I').replace('u', 'X'))

print(actor.replace('Chris', 'Liam'))

record = 'fee*fi*fo*fum'
fields = record.split('*')
print(fields)

data = "red 5 Manhattan"
print(data.split())

# foo = 1234456
#
# foo.replace(3, 5)
