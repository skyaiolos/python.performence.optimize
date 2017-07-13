"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/4
line = 'aaa\nbbb\nccc\n'

print(line.split('\n'))

print(line.splitlines())
mystr = 'xxxSPAMXXX'
my_find = mystr.find('SPAM')
print(my_find)
mystr = 'xxaaxxaa'
my_replace = mystr.replace('aa', 'SPAM')
print(my_replace)
print('SPAM' in my_replace)

mystr = '\t  Ni\n'
my_str = mystr.strip()
mystr_ = mystr.rsplit()

print(my_str, mystr_, sep='\n')

mystr = 'SHRUBBERY'
print(mystr.lower())
print(mystr.isalnum())
print(mystr.isdigit())
import string

print(string.ascii_lowercase)
print(string.whitespace)
mystr = 'aaa,bbb,ccc'
print(mystr.split(','))
mystr = 'a b\nc\nd'
print(mystr.split())
delim = 'NI'
delim = delim.join(['aaa', 'bbb', 'ccc'])
print(delim)
str = ' '.join(['A', 'dead', 'parrot'])
print(str)
