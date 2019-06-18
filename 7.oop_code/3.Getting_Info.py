#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import types


#use of type

print(type(123))

print(type(abs))


def fn():
    pass

print(type(fn) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x: x) == types.LambdaType)

print(type(x for x in range(10)) == types.GeneratorType)

#use of isinstance

class Animal(object):
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass


a = Animal()

d = Dog()

h = Husky()

print(isinstance(h,Husky))

print(isinstance(h,Husky))

print(isinstance(d,Dog) and isinstance(d, Animal))

print(isinstance(d,Husky))

print(isinstance([1,2,3],(list,tuple)))

print(isinstance((1,2,3),(list,tuple)))


#use of dir
print(dir('ABC'))

len('ABC')

print('ABC'.__len__())

class MyDog(object):
    def __len__(self):
        return 100


'ABC'.lower()

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
    
obj = MyObject()   

print(hasattr(obj,'x'))
    
print(hasattr(obj,'y'))

setattr(obj,'y',19)
print(obj.y)    
print(getattr(obj,'y'))

#if no 'z', return 404
print(getattr(obj,'z',404))

getattr(obj,'power')
power = getattr(obj,'power')

print(power())


def readImage(fp):
    if hasattr(fp,'read'):
        pass
#        return readData(fp)
    return None