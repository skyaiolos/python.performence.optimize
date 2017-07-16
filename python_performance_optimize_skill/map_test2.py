"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"
# Create by Jianguo on 2017/7/14

from python_performance_analysis.timer import Timer

MAX = 2000000

oldlist = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']

with Timer() as t:
    for i in range(MAX):
        for word in oldlist:
            newlist = []
            newlist.append(word.upper())

print("for: %s s" % t.secs)

with Timer() as t:
    for i in range(MAX):
        newlist = map(lambda x: x.upper(), oldlist)
print("map: %s s" % t.secs)

with Timer() as t:
    for i in range(MAX):
        newlist = [s.upper() for s in oldlist]
print("List: %s s" % t.secs)
# for: 9.448789119720459 s
# map: 1.4591295719146729 s
# List: 5.977842807769775 s
