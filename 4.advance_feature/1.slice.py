#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael','Sarah','Tracy','Bob','Jack']

print(L[0:3]) #Here is the use of slice
print(L[-2:-1]) #-1 is the last one

L = list(range(100))
print(L)
print('L[0:10:2]',L[0:10:2])

print('Tuple and string also can be used by slice')

def trim(s):
    print(s,'!')
    if not isinstance(s,str):
        raise('error input type')
    elif '' == s:
        return s;
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')


a = ['a']
print(a[1:])
print(a[1:1])
print(a[-1:-1])
print(a[0:0])
print(a[0:])
