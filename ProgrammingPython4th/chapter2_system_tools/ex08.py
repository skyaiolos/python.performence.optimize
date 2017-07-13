"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/6
import os

data = os.path.split(r'C:\temp\data.txt')
print(data)
# ('C:\\temp', 'data.txt')

join_data = os.path.join(r'c:\temp', 'test', 'output.txt')
print(join_data)
# c:\temp\test\output.txt

name = r'C:\temp\data.txt'
print(os.path.dirname(name), os.path.basename(name))
# C:\temp	data.txt

name = '/home/lutz/temp/data.txt'
print(os.path.dirname(name), os.path.basename(name))
# /home/lutz/temp data.txt

split_text = os.path.splitext(r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw')
print(split_text)
# ('C:\\PP4thEd\\Examples\\PP4E\\PyDemos', '.pyw')

print(os.sep)

pathname = r'C:\PP4thEd\Examples\PP4E\PyDemos.pyw'
print(os.path.split(pathname))
# ('C:\\PP4thEd\\Examples\\PP4E', 'PyDemos.pyw')
print(pathname.split(os.sep))
# ['C:', 'PP4thEd', 'Examples', 'PP4E', 'PyDemos.pyw']

print(os.path.join(*pathname.split(os.sep)))
# C:PP4thEd\Examples\PP4E\PyDemos.pyw


