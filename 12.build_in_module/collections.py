# -*- coding: utf-8 -*-

from collections import  namedtuple

Point = namedtuple('Point',['x','y'])

p = Point(1,2)

print(p.x)
print(p.y)

print(isinstance(p,Point))
print(isinstance(p,tuple))
Circle = namedtuple('Circle',['x','y','z'])

from collections import deque

q = deque(['a','b','c'])

q.append('x')
q.append('y')
print(q)
q.popleft()
print(q)

from collections import defaultdict

dd = defaultdict(lambda:'N/A')

dd['key1'] = 'abc'

dd['key1']

print(dd['key2'])

from collections import OrderedDict

d = dict([('a',1),('b',2),('c',3)])
print(d)
od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od)
print(od['z'])

class LastUpdatedOrderedDict(OrderedDict,):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
        
i = LastUpdatedOrderedDict(3)
i['1'] = 'a'
i['2'] = 'b'
i['3'] = 'c'
i['4'] = 'd'
print(i)
i['2'] = 'e'
print(i)


from collections import ChainMap
import os, argparse

defaults = {'color':'red',
            'user':'guest'}

parser = argparse.ArgumentParser()

parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
namespace = parser.parse_args()
command_line_args = {k: v for k, v in vars(namespace).items() if v}#获取v不为空的dict

combined = ChainMap(command_line_args, os.environ, defaults)

print('color = %s' % combined['color'])
print('user = %s' % combined['user'])

from collections import Counter

c = Counter()

for ch in 'programming':
    c[ch] = c[ch]+1
    
print(c)
print(c['p'])

d =  Counter('programming')

print(d)
print(d['p'])