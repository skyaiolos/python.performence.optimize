__author__ = "Jianguo Jin (jinjianguosky@hotmail.com)"

# !/usr/bin/python3
# -*- coding:utf-8 -*-  
# Created by Jianguo on 2017/7/12
"""
    Description:
        cProfile 自Python2.5 以来就是标准版Python 解释器默认的性能分析器，
"""
import cProfile
import re


def test():
    for j in range(10):
        for i in range(10 ** 6):
            re.compile("foo|bar")


cProfile.run('test()')

# 20000198 function calls(20000193 primitive calls) in 14.081 seconds

# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    4.459    4.459   14.081   14.081 1.4_cprofiler_inpy.py:14(test)
#         1    0.000    0.000   14.081   14.081 <string>:1(<module>)
#         4    0.000    0.000    0.000    0.000 enum.py:265(__call__)
#         4    0.000    0.000    0.000    0.000 enum.py:515(__new__)
#         2    0.000    0.000    0.000    0.000 enum.py:801(__and__)
#  10000000    3.771    0.000    9.622    0.000 re.py:231(compile)
#  10000000    5.850    0.000    5.851    0.000 re.py:286(_compile)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:223(_compile_charset)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:250(_optimize_charset)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:414(_get_literal_prefix)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:441(_get_charset_prefix)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:482(_compile_info)
#         2    0.000    0.000    0.000    0.000 sre_compile.py:539(isstring)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:542(_code)
#         1    0.000    0.000    0.000    0.000 sre_compile.py:557(compile)
#       3/1    0.000    0.000    0.000    0.000 sre_compile.py:64(_compile)
#         3    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
#         5    0.000    0.000    0.000    0.000 sre_parse.py:159(__len__)
#        12    0.000    0.000    0.000    0.000 sre_parse.py:163(__getitem__)
#         7    0.000    0.000    0.000    0.000 sre_parse.py:171(append)
#       3/1    0.000    0.000    0.000    0.000 sre_parse.py:173(getwidth)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:223(__init__)
#         8    0.000    0.000    0.000    0.000 sre_parse.py:232(__next)
#         2    0.000    0.000    0.000    0.000 sre_parse.py:248(match)
#         6    0.000    0.000    0.000    0.000 sre_parse.py:253(get)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:285(tell)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:407(_parse_sub)
#         2    0.000    0.000    0.000    0.000 sre_parse.py:469(_parse)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
#         2    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:829(fix_flags)
#         1    0.000    0.000    0.000    0.000 sre_parse.py:845(parse)
#         1    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
#         1    0.000    0.000   14.081   14.081 {built-in method builtins.exec}
#        19    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
#     25/24    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
#         9    0.000    0.000    0.000    0.000 {built-in method builtins.min}
#         6    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
#        48    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         5    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
#         1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}

