__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/6/7
"""
    Description:
    Fetching Shell Variables
In Python, the surrounding shell environment becomes a simple preset object, not spe-
cial syntax. Indexing  os.environ by the desired shell variable’s name string (e.g.,
os.environ['USER'] ) is the moral equivalent of adding a dollar sign before a variable
name in most Unix shells (e.g.,  $USER ), using surrounding percent signs on DOS
( %USER% ), and calling  getenv("USER") in a C program. Let’s start up an interactive session
to experiment (run in Python 3.1 on a Windows 7 laptop):
        
"""

import os
from pprint import pprint

pprint(os.environ.keys())
pprint(list(os.environ.keys()))
pprint(os.environ["PYTHONPATH"])
for srcdir in os.environ['PYTHONPATH'].split(os.pathsep):
    print(srcdir)
import sys

pprint(sys.path[:3])
