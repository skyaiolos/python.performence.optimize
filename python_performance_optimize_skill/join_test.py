__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/14
"""
    Description:
        
"""
from python_performance_analysis.timer import Timer

jlist_long = ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"]
jlist_short = ["a", "b"]
MAX_RANGE = 10 * 1000 * 1000


def test_join0():
    for i in range(MAX_RANGE):
        rs = "a" + "b"


def test_join1():
    for i in range(MAX_RANGE):
        rs = "".join(jlist_short)


def test_join2():
    for i in range(MAX_RANGE):
        rs = jlist_long[0] + jlist_long[1] + jlist_long[2] + jlist_long[3] + jlist_long[4] + jlist_long[5] + jlist_long[
            6] + \
             jlist_long[7] + jlist_long[8] + jlist_long[9]


def test_join3():
    for i in range(MAX_RANGE):
        rs = "".join(jlist_long)


with Timer() as t:
    test_join0()
print("join0: %s s" % t.secs)

with Timer() as t:
    test_join1()
print("join1: %s s" % t.secs)

with Timer() as t:
    test_join2()
print("join2: %s s" % t.secs)

with Timer() as t:
    test_join3()
print("join3: %s s" % t.secs)

# join0: 0.49297475814819336 s
# join1: 2.7630317211151123 s
# join2: 13.5156409740448 s
#
# join3: 4.42188572883606 s
