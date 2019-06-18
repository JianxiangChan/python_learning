#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list(range(1,11))

[x*x for x in range(1,11)]

#select odd data
[x*x for x in range(1,11) if x%2 == 0]

#double 'for'
[m+n for m in 'ABC' for n in 'XYZ']

import os
d = [d for d in os.listdir('.')]

print(d)

d = {'x':'A','y':'B','z':'C'}
print([k+'='+v for k,v in d.items()])

L = ['Hello','World','IBM','Apple']
print([s.lower() for s in L])

L = ['Hello', 'World', 18, 'Apple', None]

print([s.lower() for s in L if isinstance(s,str)])





