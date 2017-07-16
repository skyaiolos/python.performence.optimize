"""
#  Script Description:
    1. 避免重复计算
        效率差，太多的重复计算

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
    while i < (arg1 * arg2):
        if i % min(arg1, arg2) == 0:
            return i
        i += max(arg1, arg2)

    return (arg1 * arg2)


with Timer() as t:
    low = lowest_common_multiplier(41391237, 2830338)

print("= > None optimize: %s s" % t.secs)
print(low)
# = > None optimize: 1.5256857872009277 s


# CMD 里产看性能 ：
# python -m cProfile lcm_test0.py
