"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/4
import traceback, sys


def grail(x):
    raise TypeError('already got one')


try:
    grail('arthur')

except:
    exc_info = sys.exc_info()
    print(exc_info[0])
    print(exc_info[1])
    traceback.print_tb(exc_info[2])
