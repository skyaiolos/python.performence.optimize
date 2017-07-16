"""
#  Script Description:
    进程池

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/7/15

import multiprocessing
g_inputq = multiprocessing.JoinableQueue(QUEUEMAXSIZE)
g_outputq = multiprocessing.JoinableQueue(QUEUEMAXSIZE)

# 初始化进程池
for i in range(0,POOLSIZE):
    t= multiprocessing.Process(target=Distribute,args=(g_inputq,g_outputq))
    t.daemon =True
    t.start()

