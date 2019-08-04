# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#!usr/bin/python
import threading

#global_dict = {}
#
#def Student(name):
#    return name
#
#def std_thread(name):
#    std = Student(name)
#    global_dict[threading.current_thread()] = std
#
#def do_task_1():
#    std = global_dict[threading.current_thread()]
#    print(std)
#    
#def do_task_2():
#    std = global_dict[threading.current_thread()]
#    print(std)

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
    
def process_thread(name):
    local_school.student = name
    process_student()
    
t1 = threading.Thread(target = process_thread, args = ('Alice',), name = 'Thread-A')
t2 = threading.Thread(target = process_thread, args = ('Bob',), name = 'Thread-A')


t1.start()
t2.start()

t1.join()
t2.join()

