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


bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'job': ['software', 'writing'],
        'pay': (40000, 50000)}

print(bob2['name'])
# {'first': 'Bob', 'last': 'Smith'}

print(bob2['name']['last'])
# Smith

print(bob2['pay'][1])
# 50000
for job in bob2['job']: print(job)
# software
# writing
print(bob2['job'][-1])
# writing
bob2['job'].append('janitor')
print(bob2)
# {'name': {'first': 'Bob', 'last': 'Smith'}, 'age': 42, 'job': ['software', 'writing', 'janitor'], 'pay': (40000, 50000)}
