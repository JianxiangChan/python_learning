# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if  100 >= self.score >= 80:
            return 'A'
        elif 80 > self.score >= 60:
            return 'B'
        elif 60 > self.score >= 0:
            return 'C'
        else:
            raise ValueError(r"'Student' object's  attribute '%s' is out of range" % self.score)
                
            
            