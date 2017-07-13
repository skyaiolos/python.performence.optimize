__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/12
"""
    Description:
        pip install line_profiler
        命令行调用：
            python kernprof.py -l -v 1.5_line_profiler_test.py
"""
from memory_profiler import profile

@profile
def line_profiler():
    rs = 0
    for i in range(100 * 100):
        rs += i
    print(rs)


if __name__ == '__main__':
    line_profiler()
# In CMD:
# python "C:\Program Files (x86)\Python36-32\Lib\site-packages\kernprof.py" -l -v 1.5_line_profiler_test.py

# 49995000
# Wrote profile results to 1.5_line_profiler_test.py.lprof
# Timer unit: 3.84965e-07 s
#
# Total time: 0.0146548 s
# File: 1.5_line_profiler_test.py
# Function: line_profiler at line 14
#
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     14                                           @profile
#     15                                           def line_profiler():
#     16         1            6      6.0      0.0      rs = 0
#     17     10001        17475      1.7     45.9      for i in range(100 * 100):
#     18     10000        20191      2.0     53.0          rs += i
#     19         1          396    396.0      1.0      print(rs)
