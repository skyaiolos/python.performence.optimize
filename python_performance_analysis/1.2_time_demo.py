__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/13
"""
    Description:
        1.2 Python 自带模块 time.
"""
import time

print(time.time())
print(time.asctime(time.localtime(time.time())))
print(time.asctime(time.localtime(0)))

# 1499925837.7778068
# Thu Jul 13 14:03:57 2017
# Thu Jan  1 08:00:00 1970

# time.time() 的简单应用
import time
t0 = time.time()

def doSomething(): pass

t1 = time.time()
print(t1 - t0)
