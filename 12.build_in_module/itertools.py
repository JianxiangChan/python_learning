# -*- coding: utf-8 -*-

import itertools

natuals = itertools.count(2)

#for n in natuals:
#    print(n)

cs = itertools.cycle('ABC')

#for c in cs:
#    print(c)
    
ns = itertools.repeat('A',3)

for n in ns:
    print(n)
    
    
def limit(a):
    if a < 10:
        return True
    else:
        return False

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10, natuals)
print(list(ns))

for c in itertools.chain('ABC','XYZ'):
    print(c)

for key,group in itertools.groupby('AAABBBCCAAA12345'):
    print(key,list(group))
    
for key,group in itertools.groupby('AaaBbbcCCAaAA',lambda c: c.upper()):
    print(key,list(group))


def pi(N):
    
    retval = 0
    natuals = itertools.count(1)
    ns = itertools.takewhile(lambda x:x<=N,natuals)

    for n in ns:
        if n % 2 == 1:
            retval += 4/(2*n-1)
        else:
            retval -= 4/(2*n-1)
            
    return retval

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')

