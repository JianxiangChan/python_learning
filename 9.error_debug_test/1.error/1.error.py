# -*- coding: utf-8 -*-

def some_function():
    return -1

def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    return r

def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass

try:
    print('try...')
    r = 10/int('2')
    print('result:', r)
except ZeroDivisionError as e:
    print('except:',e)
except ValueError as e:
    print('ValueError:', e)
except UnicodeError as e:    #UnicodeError 是 ValueError子类
    print('UnicodeError:',e)  
else:
    print('no error')
finally:
    print('finally...')
    

    
print('End')

import logging

def foo(s):
    return 10/int(s)

def bar(s):
    return foo(s)*2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
        logging.exception(e)
    finally:
        print('finally...')

main()

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s ' % s)
    return 10/n

#foo('0')

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError')
        raise
        
bar()

try:
    10/0
except ZeroDivisionError:
    raise ValueError('input error!')
   
