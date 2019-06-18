# -*- coding: utf-8 -*-

import os

print(os.name)
if 'nt' != os.name:  #unspport in windows
    print(os.uname)

print(os.environ)

print(os.environ.get('PATH'))

print(os.path.abspath('.'))
current_path = os.path.abspath('.')

new_path = os.path.join(current_path, 'testdir') #不要直接拼接字符，不然不同操
                                                     #作系统不兼容
file_path = os.path.join(current_path, 'test.txt')
print(file_path,'file path')
os.path.splitext(current_path)

if True != os.path.exists('testdir'):    
    os.mkdir(new_path)

os.rmdir(new_path)

print(os.path.split(file_path))

if True == os.path.exists('test.txt'):    #存在test.txt
    os.rename('test.txt','test.py')
else:
    file = open('test.txt','w')
    file.close()
    os.rename('test.txt','test.py')
    
os.remove('test.py')

#list all dir
print([x for x in os.listdir('.') if os.path.isdir(x)])

#list all *.py files [0] filename [1] file type
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

