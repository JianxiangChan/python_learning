#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#string and bytes
print('包含中文的str')
print(ord('A'))
print(ord('中'))
print(chr(66))
'ABC'.encode('ascii')
#error example:中文can not encode in ascii
#'中文'.encode('ascii')
b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')

#use of len
len(b'abc')
len('中文')

#printf
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d' % ('Michael' , 100000))

print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)
print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明',17.25))