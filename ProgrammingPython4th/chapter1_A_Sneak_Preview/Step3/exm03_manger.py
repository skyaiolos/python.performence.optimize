"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/3
from person import Person
from manager import Manager

bob = Person(name='Bob Smith', age=42, pay=10000)
sue = Person(name='Sue Jones', age=45, pay=20000)
tom = Person(name='Tom Doe', age=55, pay=30000)
db = [bob, sue, tom]
for obj in db:
    obj.giveRaise(.10)
for obj in db:
    print(obj.lastName(), '=>', obj.pay)

# Smith => 11000.0
# Jones => 22000.0
# Doe => 33000.0