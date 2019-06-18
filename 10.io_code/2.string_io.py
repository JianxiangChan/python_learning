# -*- coding: utf-8 -*-

from io import StringIO
from io import BytesIO

f = StringIO()

f.write('hello')

f.write(' ')

f.write('world')

print(f.getvalue())


f = StringIO('Hello!\nHi!\nGoodbye!\n')

while True:
    s = f.readline()
    if s == '':
        break
    print(s)

f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')

print(f.read())  #ptr 已经移动
f.seek(-2,2)        #para1: offset para2: 0文件开头 1相对于当前的位置 2文件末尾
print(f.read())
f.seek(-2,1)        #para1: offset para2: 0文件开头 1相对于当前的位置 2文件末尾
print(f.read())
f.seek(3,0)        #para1: offset para2: 0文件开头 1相对于当前的位置 2文件末尾
print(f.read())