"""
#  Script Description:
    多线程Demo

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/7/15
# from python_performance_optimize_practice.timer import Timer

import threading
import time


def compute():
    for i in range(10000):
        rs = 0
        for i in range(1000):
            rs += i


def mysleep():
    time.sleep(1)


def test(func):
    print(func.__name__)
    with Timer() as t:
        for i in range(10):
            func()

    print("=> single thread 10 times : %s s" % t.secs)

    with Timer() as t:
        thread_list = []
        for i in range(10):
            th = threading.Thread(target=func, args=())
            th.start()
            thread_list.append(th)

        for th in thread_list:
            th.join()
    print("=> multiple threads 1 time : %s s" % t.secs)
    print()


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


if __name__ == '__main__':
    test(compute)
    test(mysleep)
    #
    # compute
    # => single thread 10 times : 12.967560529708862 s
    # => multiple threads 1 time : 11.162601709365845 s
    # mysleep
    # => single thread 10 times : 10.004865169525146 s
    # => multiple threads 1 time : 1.0101795196533203 s
