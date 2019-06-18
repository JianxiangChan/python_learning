# -*- coding: utf-8 -*-

class Student(object):
    pass

s = Student()
s2 = Student()

s.name = 'Micheal'  #给实例绑定一个属性

def set_age(self,age):
    self.age = age
    
from types import MethodType

#给实列绑定一个方法，但只对该实例有效
s.set_age = MethodType(set_age, s)

s.set_age(25)

def set_score(self, score):
    self.score = score
    
#给 class 动态绑定方法
Student.set_score = set_score 

s.set_score(100)

s.set_score(100)

print(s.score)

s2.set_score(100)

print(s2.score)

#use of __slots__
class Student(object):
    __slots__ = ('name', 'age') #限制Student 属性
    
s = Student()

s.name = 'Michael'
s.age = 25
#s.score = 99 #error here

class GraduateStudent(Student):
    pass

g = GraduateStudent()

g.score = 99 #继承的子类不受影响


    