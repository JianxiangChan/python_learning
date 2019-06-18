# -*- coding: utf-8 -*-

#use of property
class Student(object):
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value
        print(self._score)
        
s = Student()

s.score = 60 #s.set_score

s.score

class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('score must be an integer!')
        if value < 0:
            raise ValueError('score must between 0~100!')
        self._width = value
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        if not isinstance(value,(int,float)):
            raise ValueError('score must be an integer!')
        if value < 0:
            raise ValueError('score must between 0~100!')
        self._height = value 
        
    @property
    def resolution(self):
        return self.height * self.width
    
s = Screen()

s.height = 768
s.width = 1024
print(s.height)
print(s.width)
print(s.resolution)
    
        
    
        