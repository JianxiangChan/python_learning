#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#use of map
def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6])
#map return Iterator
#so print(r) is errot
for x in r:
    print(x)

print(list(r))

r = map(str,[1,2,3,4,5,6])

print(list(r))

from functools import reduce

def add(x,y):
    return x+y

def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))

print(reduce(add,[1,3,5,7,9]))

def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'7':7,'9':9}
    return digits[s]
print(reduce(fn,map(char2num,'12579')))

def str2int(s):
    return reduce(lambda x, y: x*10+y,map(char2num,s))

print(str2int('12345'))

def normalize(name):
    if len(name) == 0:
        raise('error type')
    name0 = str.upper(name[0])
    if len(name) == 1:
        return name0
    name1 = str.lower(name[1:])
    return name0+name1

L1 = ['adam','LISA','barT']
L2 = list(map(normalize,L1))
print(L2)

def prod(L):
    if len(L) == 0:
        raise('error type')
    if len(L) == 1:
        return L[0]
    return reduce(lambda x, y: x*y, L)

print(prod([1,3,5,7]))

digital = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def char2int(s):
    return digital[s]
    
def fn(x = 0,y = 0):
  return x*10 +y

def str2float(s):
    return reduce(fn,map(char2int,s[:s.index('.')])) + reduce(fn,map(char2int,s[(s.index('.')+1):]))/(10**(len(s)-1-s.index('.')))

print(str2float('123.456'))
print(str2float('1.456'))





