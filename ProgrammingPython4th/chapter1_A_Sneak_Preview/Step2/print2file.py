"""
#  Script Description:
    Print string in to file

"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/3
# File name ->

dbfilename = 'print2file.txt'
with open(dbfilename, 'w', encoding='utf-8') as f:
    print("First , print string into specific file ")
    print("First , print string into specific file ", file=f)
