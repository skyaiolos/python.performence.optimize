__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/14
"""
    Description:
        排序，快速排序 
        对应的库函数 ： 排序， sorted
        
"""
from python_performance_analysis.timer import Timer


def quick_sort(lists, left, right):
    # 快速排序
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]

    lists[right] = key
    quick_sort(list, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


lists = [6, 4, 2, 1, 7, 8, 9, 3, 0, 5]
# with Timer() as t:
#     quick_sort(lists, lists[-2], lists[3])
#
# print("=>quick sort: %s s" % t.secs)
with Timer() as t:
    rs = sorted(lists)
    print(rs)
print("=>sorted: %s s" % t.secs)
