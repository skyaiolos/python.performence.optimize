"""
#  Script Description:


"""
__author__ = "爱的彼岸(QQ:3124724)"
__copyright__ = "Copyright 2017,3124724@qq.com"

# Create by Jianguo on 2017/6/6
import subprocess

sub_all = subprocess.call('python helloshell.py')  # roughly like os.system()
print(sub_all)

sub_all = subprocess.call('cmd /C "type helloshell.py"')  # built-in shell cmd
print(sub_all)

sub_all = subprocess.call('type helloshell.py', shell=True)  # alternative for built-ins
print(sub_all)

pipe = subprocess.Popen('python helloshell.py', stdout=subprocess.PIPE)

print("----pipe.communicate()")
print(pipe.communicate())
print(pipe.returncode)
pipe = subprocess.Popen('python helloshell.py', stdout=subprocess.PIPE)

print("------------pipe.stdout.read()")
print(pipe.stdout.read())
print(pipe.wait())
