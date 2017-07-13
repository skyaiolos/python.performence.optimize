__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/12
"""
    Description:
        memory profiler
"""

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    my_func()

# python -m memory_profiler 2.1_memory_profiler_test0.py


# Line #    Mem usage    Increment   Line Contents
# ================================================
#     11   27.082 MiB    0.000 MiB   @profile
#     12                             def my_func():
#     13   30.898 MiB    3.816 MiB       a = [1] * (10 ** 6)
#     14  107.195 MiB   76.297 MiB       b = [2] * (2 * 10 ** 7)
#     15   30.898 MiB  -76.297 MiB       del b
#     16   30.898 MiB    0.000 MiB       return a

# mprof 基于时间的内存测量
# python mprof run 2.1_memory_profiler_test0.py