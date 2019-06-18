#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = list(filter(lambda x: x% 2,range(1,20)))

print(L)

def is_odd():
    return lambda n:n%2

L = list(filter(is_odd(),range(1,20)))

print(L)
