#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def now():
    print('2015-5-21')

f = now

print(f.__name__)
print(now.__name__)

def log(func):
    def wrapper(*args, **kw):
        print('call %s():'% func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2015-5-20')

now()

import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():'% (text,func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('excute')
def now():
    print('2015-05-20')

now() #name is wrapper



print(now.__name__)

#work
import functools
import time


def metric(fn):
    def wrapper(*args,**kw):
        start = time.time()
        res = fn(*args,**kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end-start))
        return res
    return wrapper
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


    
