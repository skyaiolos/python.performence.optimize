__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/11
"""
    Description:
        #test_shell_time1.py   - 程序重I/O
    结论：
        1. real !=user+sys
        2. real 和 user + sys的值越是接近，证明程序越重计算，反之说明程序重I/O
"""

from time import *
sleep(2)

# real    0m2.110s
# user    0m0.000s
# sys     0m0.015s

