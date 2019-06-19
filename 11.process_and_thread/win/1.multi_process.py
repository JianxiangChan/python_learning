# -*- coding: utf-8 -*-
#!usr/bin/python

from multiprocessing import Process

import os

run_check = ['not run']

def run_proc(name):
    global run_check
    print(run_check)
    print('Run child process %s (%s)...' % (name, os.getpid()))
    run_check[0] = 'run already'
    print(run_check)
    print(id(run_check))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target = run_proc, args = ('test',)) #注意这个IDE里面运行是不生效的
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
    print(run_check)
    print(id(run_check))
    
    run_proc('test')
    print(run_check)
    print(id(run_check))