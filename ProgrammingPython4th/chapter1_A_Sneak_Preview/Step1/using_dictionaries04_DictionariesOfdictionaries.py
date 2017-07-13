# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/5/31
"""
    Description:
    Dictionaries of dictionaries
One last twist on our people database: we can get a little more mileage out of diction-
aries here by using one to represent the database itself. That is, we can use a dictionary
of dictionaries—the outer dictionary is the database, and the nested dictionaries are
the records within it. Rather than a simple list of records, a dictionary-based database
allows us to store and retrieve records by symbolic key:
        
"""
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)
# {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}

db = {}
db['bob'] = bob
db['sue'] = sue
bob_name = db['bob']['name']
print(bob_name)
# Bob Smith
sue_pay = db['sue']['pay'] + 10000
# 50000
print(sue_pay)
print(db)
from pprint import pprint

pprint(db)

for key in db:
    print(key, '=>', db[key]['name'])
# bob => Bob Smith
# sue => Sue Jones

for key in db:
    print(key, '=>', db[key]['pay'])

# bob => 30000
# sue => 40000

for key in db:
    print(db[key]['name'])
    db[key]['pay'] *= 1.10
    print(db[key]['name'].split()[-1], db[key]['pay'], sep=': ')

# Bob Smith
# Smith:33000.0
# Sue Jones
# Jones:44000.0
print('---To visit all records, either index by key as you go:')
for recode in db.values():
    print(recode['pay'])
    print(recode['name'])
# 33000.0
# Bob Smith
# 44000.0
# Sue Jones
x = [db[key]['name'] for key in db]
print(x)