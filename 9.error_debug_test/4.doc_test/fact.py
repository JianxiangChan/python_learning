# -*- coding: utf-8 -*-

def fact(n):
    '''
    Calculate 1*2*...*n
    
    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
    ValueError
    >>> fact(2.5)
    Traceback (most recent call last):
    ...
    TypeError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    if True == isinstance(n, float):
        raise TypeError()
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()