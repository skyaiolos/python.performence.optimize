"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"


# Create by Jianguo on 2017/7/14
oldlist = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
newlist = []
for word in oldlist:
    newlist.append(word.upper())

print(newlist)

newlist = map(lambda x: x.upper(), oldlist)
print(newlist)

newlist = [s.upper() for s in oldlist]
print(newlist)
