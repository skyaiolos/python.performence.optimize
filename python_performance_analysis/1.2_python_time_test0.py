__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/12
"""
    Description:
        使用Timer
"""

from python_performance_analysis.timer import Timer
from redis import Redis

rdb = Redis()

with Timer() as t:  # with , 会调用 __enter__ 函数。with 执行完 会执行__exit__ 函数。
    rdb.lpush("foo", "bar")
print("=> elasped lpush: %s s" % t.secs)

with Timer() as t:
    print(rdb.lpop("foo"))
print("=> elasped lpop: %s s" % t.secs)

# => elasped lpush: 1.043999991035 s
# bar
# => elasped lpop: 0.00100016593933 s