__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/12
"""
    Description:
       使用列表推导可以提高性能。
       列表推导
       字典推导
       集合推导
       
            newlist =[s.upper() for s in oldlist]
"""
# 带if 语句的列表推到。
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
newlist = []
for name in names:
    if len(name) > 3:
        newlist.append(name.upper())
print(newlist)

# 利用列表推导优化
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
newlist = [name.upper() for name in names if len(name) > 3]
print(newlist)

# 字典推导
strings = ['import ', 'is', 'with', 'if', 'file', 'exception']
D = {key: val for val, key in enumerate(strings)}
print(D)

# 集合推导
strings = ['a', 'is', 'with', 'if', 'file', 'exception']
S = {len(s) for s in strings if len(s) >= 1}
print(S)
print(set(S))  # set 没有重复项
