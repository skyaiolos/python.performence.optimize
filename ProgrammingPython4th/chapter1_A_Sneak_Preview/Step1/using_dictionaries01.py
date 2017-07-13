# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/5/31
"""
    Description:
    Using Dictionaries
The list-based record representations in the prior section work, though not without
some cost in terms of performance required to search for field names (assuming you
need to care about milliseconds and such). But if you already know some Python, you
also know that there are more efficient and convenient ways to associate property
names and values. The built-in dictionary object is a natural:
        
"""
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

print(bob['name'], sue['pay'], sep=',')
# Bob Smith,40000

print(bob['name'].split()[-1])
# Smith

sue['pay'] *= 1.10
print(sue['pay'])
# 44000.0

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob, sue, sep="\n")
# {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
# {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
sue = {}

print(sue)
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
sue['job'] = 'hdw'
print(sue)

print("-----lise(zip())------")
names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
n_v = list(zip(names, values))
print(n_v)
print()
print("-----dict(zip())------")
fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, "?")
print(record)
