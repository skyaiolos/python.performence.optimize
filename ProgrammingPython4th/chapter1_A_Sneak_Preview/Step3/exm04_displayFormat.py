"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

from person import Person


# Create by Jianguo on 2017/6/3
class Manager(Person):
    def __init__(self, name, age, pay, job):
        Person.__init__(self, name, age, pay, 'manager')

    def __str__(self):
        return '<%s => %s => %s>' % (self.__class__.__name__, self.name, self.job)


tom = Manager(name='Tom Jones', age=50, pay=50000, job='manager')
print(tom)
