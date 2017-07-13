"""
#  Script Description:
Let’s step back for a moment and consider how far we’ve come. At this point, we’ve
created a database of records: the shelve, as well as per-record pickle file approaches
of the prior section suffice for basic data storage tasks. As is, our records are represented
as simple dictionaries, which provide easier-to-understand access to fields than do lists
(by key, rather than by position). Dictionaries, however, still have some limitations that
may become more critical as our program grows over time.
For one thing, there is no central place for us to collect record processing logic. Ex-
tracting last names and giving raises, for instance, can be accomplished with code like
the following:

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/3
import shelve

db = shelve.open('people-shelve', 'r')
bob = db['bob']
print(bob)
bob_name = bob['name'].split()[-1]
print(bob_name)
# {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
# Smith
sue = db['sue']
print(sue['pay'])
sue['pay'] *= 1.25
print(f"The pay * 1.25 = {sue['pay']} for sue")
db['sue'] = sue
db.close()

# 60000.0
# The pay * 1.25 = 75000.0 for sue
