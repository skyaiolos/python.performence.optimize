__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/12
"""
    Description:
       测量一段代码的运行时间，在python内可以直接使用timeit.
"""
import timeit

print(timeit.timeit("x = range(100)"))
# 0.4969555045947493
