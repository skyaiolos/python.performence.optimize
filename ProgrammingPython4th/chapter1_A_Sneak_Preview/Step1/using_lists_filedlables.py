#!/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/5/31
"""
    Description:
        Step 1: Representing Records
        Using Lists - Field labels
"""

NAME, AGE, PAY = range(3)  # 0, 1, and 2
bob = ['Bob Smith', 42, 10000]
print(bob[NAME])
print(PAY, bob[PAY])
# Bob Smith
# 2 10000


bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
for person in people:
    print(person[0][1], person[2][1])
# Bob Smith 10000
# Sue Jones 20000
for person in people:
    for (name, value) in person:
        if name == 'name':
            print(value)

print("-----we can code a fetcher function to do the job for us")

def field(record, label):
    for (fname, fvalue) in record:
        if fname == label:
            return fvalue

print(field(bob, 'name'))
print(field(bob, 'age'))
print(field(bob, 'pay'))

for rec in people:
    print(field(rec, 'age'))

    # Bob Smith
    # 42
    # 10000
    # 42
    # 45
