# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Created by Jianguo on 2017/6/7
"""
    Description:
        Command-Line Arguments
The  sys module is also where Python makes available the words typed on the command
that is used to start a Python script. These words are usually referred to as command-
line arguments and show up in  sys.argv , a built-in list of strings. C programmers may
notice its similarity to the C  argv array (an array of C strings). It’s not much to look at
interactively, because no command-line arguments are passed to start up Python in this
mode:
"""
import sys

print(sys.argv)
