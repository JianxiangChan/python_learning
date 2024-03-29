# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student Object (name: %s)' % self.name
        
s = Student('Shane')
print(s)
print(Student('Michael'))

class Fib(object):
    def __init__(self):
        self.a, self.b = 0,1
    
    def __iter__(self): #use of __iter__()
        return self
    
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    
    def __str__(self): #use of __str__()
        return 'This is Fib' 
    
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b, a+b
            return a
        
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b, a+b
            return L
        
    def __getattr__(self,attr):
        raise AttributeError(' \'Fib\' object has no attribute \'%s\'' % attr)
    
    def __call__(self):
        print('Class name is %s' % self.__class__.__name__) #class's name

for n in Fib():
    print(n)

f = Fib()
print(f)

print(f[100])

print(f[0:5])

print(f())



class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path)) #use of getattr
    
    def __call__(self, path):
        return Chain('%s/%s' % (self._path, path)) #use of call

    def __str__(self):
        return self._path

print(Chain().status.user.timeline.list)
print(Chain().users('michael').repos)

