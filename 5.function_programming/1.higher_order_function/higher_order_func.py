#!/usr/bin/env python3
# -*- coding: utf-8 -*-

my_abs = abs
#my_abs point to abs
print(my_abs(-10))

def add(x, y, f):
    return f(x) + f(y)
#pass in function abs
print(add(-5, 6, abs))
