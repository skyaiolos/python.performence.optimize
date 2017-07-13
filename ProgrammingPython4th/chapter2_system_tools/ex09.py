"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/6
import os

os.chdir(r'C:\Users')
print(os.getcwd())
# C:\Users

print(os.path.abspath(''))
# C:\Users
print(os.path.abspath('temp'))
# C:\Users\temp
print(os.path.abspath(r'PP4E\dev'))
# C:\Users\PP4E\dev
print(os.path.abspath('.'))
print(os.path.abspath('..'))

print(os.path.abspath(r'..\examples'))
# C:\examples
print(os.path.abspath(r'C:\\PP4thEd\\chapters'))
