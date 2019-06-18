#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_odd(n):
    return n%2 == 1
print(list(filter(is_odd,[1,2,4,6,9,10,15])))

def not_empty(s):
    return s and s.strip()  #'  ' this should be see as empty
print(list(filter(not_empty,['a','','B ',None, ' C','    '])))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0  #return a func, not good code

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

def _nature_num():
    n = 0;
    yield n;
    while True:
        n = n + 1
        yield n

def _is_palindrome(n):
    return n == int(str(n)[::-1]) #reverse all

def palindrome():
    return filter(_is_palindrome,_nature_num())

for n in palindrome():
    if n < 1000:
        print(n)
    else:
        break



    

