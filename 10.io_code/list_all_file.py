import os
# -*- coding: utf-8 -*-


#0.输入查找关键字
def get_filename():
    filename = input('请输入需要查找的文件名:') 
    if  False == isinstance(filename,str):
        print('您输入的文件名格式有误，请重新输入')
        get_filename()
    return filename

#1.遍历所有文件夹
def __findfile__(dir,filename,l = []):
    file_list = os.listdir(dir)
    for file in file_list:
        path = os.path.join(dir, file)
        if os.path.isdir(path):
            __findfile__(path,filename,l)
        if os.path.isfile(path):
            if filename in os.path.split(path)[1]:
               l.append(os.path.relpath(path))

def findfile(dir, filename):
    l = []
    __findfile__(dir,filename,l)              
    return l         
               
res = findfile(os.path.abspath('.'),get_filename())

for i in res:
    print(i)
#2.如果是文件夹,进入文件夹寻找文件

#3.如果是文件查看是符合条件


from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
