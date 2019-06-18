#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):  #首字母一般大写
                        #object 表示该类是从哪里继承，如果没有继承就是默认object
    def __init__(self, name, score):  #__init__ special func
                                      #self 就是实例本身
        self.name = name              #with inited args, creating void instances
                                      #is not allowed
        self.score = score

    def print_score(self):                      #类的方法
        print('%s %s' %(self.name, self.score))
    
    def get_grade(self):
       if self.score > 90:
           print('A')
       elif self.score > 60:
           print('B')
       else:
           print('C')

bart = Student('Bart Simpson', 50)

bart.print_score()

