#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def int2(x,base=2):
    return int(x,base)
import functools
int2 = functools.partial(int, base=2)

print(int2('1010110'))

