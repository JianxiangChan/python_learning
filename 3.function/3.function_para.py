#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x, n = 2):
    s = 1
    while n > 0:
	    n = n - 1
	    s = s*x
    return s

print(power(2))
print(power(2,4))

def enroll(name, gender, age=6, city='Beijing'):
    print('name:',name)
    print('gneder:',gender)
    print('age:',age)
    print('city:',city)
    
enroll('Sarah','F')
enroll('Bob','M',7)
enroll('Adam','M',city='Tianjin')

L = []
def add_end(L = None):
    if L is None:
        L = []
    L.append('END')
    return L

add_end(L)
add_end(L)
print(L)

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc(1,2))
print(calc(1,2,3))
nums = [1,2,3]
print(calc(*nums))


def person(name, age, **kw):
    print('name:',name,'age:',age,'other:',kw)

person('Michael',30)
person('Bob',35,city='Beijing')

extra = {'city':'Beijing','Job':'Engineer'}
person('Jack', 24, **extra)

def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city = 'Beijing', job='Engineer')

def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('Jack', 24, 'Fucku', 'Bitch', city = 'Beijing', job = 'bitch')



#Pratice
def product(*mult):
    if len(mult) == 0:
        raise TypeError
    sum = 1
    for n in mult:
        sum = n*sum
    return sum

print('product(0) =', product(0))
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))

   
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')









