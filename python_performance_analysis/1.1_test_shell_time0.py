__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Created by Jianguo on 2017/7/11
"""
    Description:
        #test_shell_time0.py    - 程序重计算的。
    结论：
        1. real !=user+sys
        2. real 和 user + sys的值越是接近，证明程序越重计算，反之说明程序重I/O
"""

rs = 0
for i in range(100 * 100):
    rs += i
print(rs)
# time python test_shell_time0.py

# 49995000
#
# real    0m0.184s
# user    0m0.000s
# sys     0m0.015s
