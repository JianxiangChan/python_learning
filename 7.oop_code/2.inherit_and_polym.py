
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal(object):  #Father
    def run(self):
        print('Animal is running...')
        
class Dog(Animal):  #son
    
    def run(self):
        print('Dog is runing...')

    def eat(self):
        print('Eating meating...')
        
        
class Cat(Animal):
    
    def run(self):
        print('Cat is runing...')
        

dog = Dog()

dog.run()

cat = Cat()

cat.run()

isinstance(dog, Dog)
isinstance(dog, Animal)

def run_twice(animal):
    animal.run()
    animal.run()
    
run_twice(dog)
run_twice(cat)

class Timer(object):
    def run(self):
        print('start...')
time = Timer()
        
run_twice(Timer())

print(isinstance(time,Animal))


