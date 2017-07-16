__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Created by Jianguo on 2017/7/11
"""
    Description:
        Time 的封装。
        time.time()的封装使用：
        __enter__ 和 __exit__ 配合with 关键字使用        
"""

import time


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    # __enter__ and __exit__ 配合 with 使用 , with 调用调出。
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:  # print log ON-OFF , if 1 will print the log.
            print('elapsed time : %f ms' % self.msecs)
