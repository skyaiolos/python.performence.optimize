# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/5/31
"""
    Description:
    Lists of dictionaries
Regardless of how we code them, we still need to collect our dictionary-based records
into a database; a list does the trick again, as long as we don’t require access by key at
the top level:        
"""

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

print(bob, sue, sep='\n')

people = [bob, sue]
print(people)
for person in people:
    print(person['name'], person['pay'], sep=',')

# Bob Smith,30000
# Sue Jones,40000

for person in people:
    if person['name'] == 'Sue Jones':
        print(person['name'], person['pay'], sep=':')
# Sue Jones:40000

names = [person['name'] for person in people]
print(names)
name_list = list(map((lambda x: x['name']), people))
print(name_list)

total_pay = sum(person['pay'] for person in people)
print(total_pay)
sum(person['pay'] for person in people)
# 70000
name_less45 = [rec['name'] for rec in people if rec['age'] >= 45]
print(name_less45)
# ['Sue Jones']
age_ = [(rec['age'] * 2 if rec['age'] >= 45 else rec['age'] - 2) for rec in people]
print(age_)
# [40, 90]
G = (rec['name'] for rec in people if rec['age'] >= 45)
print(G)
print(next(G))
# <generator object <genexpr> at 0x03A233C0>
# Sue Jones

G = ((rec['age'] * 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print("--next(G)--")
print(next(G))
print("G.__next__()")
print(G.__next__())
for person in people:
    print(person['name'].split()[-1])  # last name
    person['pay'] *= 1.10  # a 10% raise

for person in people: print(person['pay'])
