#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#dict(dictionary)
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

#Add a dict
d['Adam'] = 67
print(d['Adam'])
print(d)

#reset dict
d['Adam'] = 65
print(d['Adam'])

#check if exist
result = 'Thomas' in d
print('If Thomas in d',result)
result = 'Adam' in d
print('If Adam in d',result)

print(d.get('Thomas'))
print(d.get('Thomas', -1)) #if not exist return -1

#delect one
d.pop('Adam')
print(d)

#set
s = set([1,2,3])
print(s)

#add key
s.add(4)
s.add(4)
print(s)

#remove key
s.remove(4)
print(s)

#& |
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)

#unchangeable
a = ['b','c','a']
a.sort()
print(a)

a = 'abc'
a.replace('a','A')
print(a)
a = a.replace('a','A')
print(a)
