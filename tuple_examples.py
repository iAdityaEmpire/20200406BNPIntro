#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(person)
print(person[0])

x = """
struct person {
   char *fname;
   char *lname;
   int age;
   Date *date;
};

"""

# list-of-variables = any-iterable

first_name, last_name, product, dob = person
print(first_name, last_name)


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

p = people[0]
print(p)
first_name, last_name, product, dob = people[0]
print(first_name, last_name, '\n')

# for person in people:
#     first_name, last_name, product, dob = person


for first_name, last_name, *product, dob in people:
    # first_name, last_name, product, dob = people[0]
    # first_name, last_name, product, dob =people[1]
    # ...
    print(first_name, last_name, product)
print()

values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z, '\n')

x, *y, z = values
print(x, y, z, '\n')

*x, y, z = values
print(x, y, z, '\n')

stuff = [('a', 5), ('m', 16), ('r', 10)]

for letter, number in stuff:
    print(letter * number)
print()




