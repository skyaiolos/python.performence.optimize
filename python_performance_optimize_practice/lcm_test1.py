"""
#  Script Description:
    1. 避免重复计算
        优化后， 没有重复计算。在循环外提前计算，不要重复计算的。

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/7/15
from python_performance_analysis.timer import Timer


def lowest_common_multiplier(arg1, arg2):
    """
    最小公倍数
    """
    i = max(arg1, arg2)
    j = arg1 * arg2
    _max = i
    _min = min(arg1, arg2)
    # while i < (arg1 * arg2):
    while i < j:
        # if i % min(arg1, arg2) == 0:
        if i % _min == 0:
            return i
        # i += max(arg1, arg2)
        i += _max
    # return arg1 * arg2
    return j


with Timer() as t:
    low = lowest_common_multiplier(41391237, 2830338)

print("= > after optimize : %s s" % t.secs)
print(low)
# = > after optimize : 0.49259209632873535 s
# 39050396982702

# after optimize again:
# = > after optimize : 0.45901989936828613 s
# 39050396982702


# CMD 里产看性能 ：
# python -m cProfile lcm_test1.py
