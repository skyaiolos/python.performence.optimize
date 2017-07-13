"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/7/13
import bisect
from python_performance_analysis.timer import Timer
from python_performance_optimize_skill.bsearch import bsearch

# bisect.bisect_left(a, k)

#  性能测试
with Timer() as t:
    a = range(1000 * 1000)
    for i in range(1000 * 1000):
        k = 100
        bisect.bisect_left(a, k)  # or bsearch(a,k)
print(" = > bisect.bisect_left: %s s" % t.secs)

with Timer() as t:
    a = range(1000 * 1000)
    for i in range(1000 * 1000):
        k = 100
        bisect.bisect_right(a, k)  # or bsearch(a,k)
print(" = > bisect.bisect_right: %s s" % t.secs)

with Timer() as t:
    a = range(1000 * 1000)
    for i in range(1000 * 1000):
        k = 100
        bsearch(a, k)
print(" = > bsearch: %s s" % t.secs)
# = > bisect: 9.703113555908203 s

# = > bsearch: 18.800233602523804 s
