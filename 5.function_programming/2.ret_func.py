#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def createCounter():
    n = [0]
    def counter():
        n[0] = n[0] + 1
        return n[0]
    return  counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('Test pass')
else:
    print('Test fail')



