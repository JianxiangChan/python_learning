# -*- coding: utf-8 -*-

from hello import Hello

h = Hello()

h.hello('Shane')

print(type(Hello))

print(type(h))

def fn(self, name = 'World'):
    print('Hello, %s' % name)

Hello = type('Hello', (object,), dict(hello2=fn)) #创建Hello class

h = Hello()

h.hello2()