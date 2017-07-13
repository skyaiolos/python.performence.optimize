import os, sys

print('my os.getcwd =>', os.getcwd())  # show my cwd execution dir 双击启动时是脚本所在目录，但是命令行
# 却是执行脚本时的目录
print('my sys.path  =>', sys.path[:6])  # show first 6 import paths 第一个是脚本所在目录
input()  # wait for keypress if clicked
