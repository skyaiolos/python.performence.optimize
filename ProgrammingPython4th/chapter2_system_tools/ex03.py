"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/4
file = open('spam.txt', 'w')
file.write(('spam' * 5) + '\n')

file.close()

file = open('spam.txt', 'r')
text = file.read()
print(text)
