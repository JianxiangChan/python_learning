#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

for ch in 'ABC':
    print(ch)

from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

for i,value in enumerate(['A','B','C']):
    print(i,value)

for x,y in [(1,2),(2,4),(3,9)]:
    print(x,y)

def findMinAndMax(L):
    if len(L):
        min_num = L[0]
        max_num = L[0]
        for value in L:
            if value > max_num:
                max_num = value;
            if value < min_num:
                min_num = value;
    else:
        min_num = None
        max_num = None
    return (min_num,max_num)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

