#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

#function define
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TpyeError('bad operand type') #check illegal para
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-10))

#do nothing: pass 
def nop():
    pass

nop()

#multi return
def move(x, y, step, angle = 0):
    nx = x + step*math.cos(angle)
    ny = x + step*math.sin(angle)
    return nx, ny
x,y = move(100, 100, 60, math.pi/6)
print(x,y)

r = move(100,100,60,math.pi/6)
print(r)

def quadratic(a,b,c):
    if not isinstance(a,b,c,(int,float)):
        raise TpyeError('bad operand type') #check illegal para
    
