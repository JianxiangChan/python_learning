# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#!usr/bin/python

import time, threading

#新线程执行的代码
def loop():
    print('thread %s is runing...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
    print('thread %s ended' % threading.current_thread().name)
    
print('thread %s is running...' % threading.current_thread().name)

t = threading.Thread(target = loop, name = 'LoopThread')

t.start()

t.join()

print('thread %s ended.' % threading.current_thread().name)


balance = 0

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

lock  = threading.Lock()

def run_thread(n):
    for i in range(10000000):
        #先要获取锁
        lock.acquire()
        try:
            change_it(n)   # no lock here 
        finally:
            lock.release()
        
t1 = threading.Thread(target = run_thread, args = (1000,))
t2 = threading.Thread(target = run_thread, args = (1000,))
t1.start()

t2.start()

t1.join()

t2.join()

print(balance)




    
