__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/12
"""
    Description:
        memory profiler in python file
"""
from memory_profiler import profile


@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a


if __name__ == '__main__':
    my_func()
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     13     27.0 MiB      0.0 MiB   @profile
#     14                             def my_func():
#     15     30.8 MiB      3.8 MiB       a = [1] * (10 ** 6)
#     16    107.1 MiB     76.3 MiB       b = [2] * (2 * 10 ** 7)
#     17     30.8 MiB    -76.3 MiB       del b
#     18     30.8 MiB      0.0 MiB       return a