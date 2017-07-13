"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/6
import os

print(os.system('dir /B'))
print(os.system('type more.py'))
print(os.system('type fail.py'))
print('-' * 30)
print(open('more.py').read())
print("text".center(30, '-'))
text = os.popen('type more.py').read()
print(text)
listing = os.popen('dir /B').readlines()
print(listing)
