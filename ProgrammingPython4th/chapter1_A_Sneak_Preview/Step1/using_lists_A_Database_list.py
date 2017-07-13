#!/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/5/31
"""
    Description:
        Step 1: Representing Records
        Using Lists - A database list
"""
bob = ['Bob Smith', 42, 30000, 'software']

sue = ['Sue Jones', 45, 50000, 'hardware']

print(bob[0], sue[2])
# Bob,Smith 40000
# Bob_smith = bob[0].split(',')

Bob_smith = bob[0].split(' ')
print(Bob_smith)
# ['Bob', 'Smith']

smith = bob[0].split(' ')[0]
print(smith)
# Bob

people = [bob, sue]
print(people)
# [['Bob Smith', 42, 30000, 'software'], ['Sue Jones', 45, 40000, 'hardware']]

for person in people:
    print(person)
# ['Bob Smith', 42, 30000, 'software']
# ['Sue Jones', 45, 50000, 'hardware']

print(people[1][0])
# Sue Jones
print('------------------------------')
for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20  # give each a 20% raise

for person in people:
    print(person[2])
print("as list comprehensions, maps, and generator ")
pays = [person[2] for person in people]
print(pays)
print('----map()----')
pays = map((lambda x: x[2]), people)  # ditto (map is a generator in 3.X)
print(pays)
print(list(pays))
# <map object at 0x035217B0>
# [36000.0, 60000.0]
total = sum(person[2] for person in people)
print(total)
# 96000.0
print("----To add a record to the database, the usual list operations, such as  append and  extend ,will suffice----:")
people.append(['Tom', 50, 0, None])
print(len(people))
# 3
print(people[-1][0])
# Tom
