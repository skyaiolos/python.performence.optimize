"""
#  Script Description:
    推荐 simplejson 来解析json , 比较优化的库


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/7/15
import json
# from .timer import Timer
import sys
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


with Timer() as t:
    for i in range(10):
        json.loads(open(sys.path[0] + "//test.json").read())

import simplejson

with Timer() as t:
    for i in range(10):
        simplejson.loads(open(sys.path[0] + "//test.json").read())

print("simplejson loads %s s " % t.secs)
