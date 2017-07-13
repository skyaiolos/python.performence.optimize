"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/3
from person_start import Person

bob = Person('Bob Smith', 42)
sue = Person('Sue Jones', 45, 40000)

people = [bob, sue]  # a "database" list
for person in people:
    print(person.name, person.pay)
# Bob Smith 0
# Sue Jones 40000

x = [(person.name, person.pay) for person in people]
print(x)
# [('Bob Smith', 0), ('Sue Jones', 40000)]
age_than45 = [rec.name for rec in people if rec.age >= 45]
print(age_than45)
# ['Sue Jones']

# pythonic style
age = [(rec.age * 2 if rec.age >= 45 else rec.age) for rec in people]
print(age)
# [42, 90]
