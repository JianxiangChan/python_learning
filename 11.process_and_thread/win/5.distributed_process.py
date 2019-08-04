# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#!usr/bin/python

import random,time,queue

from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

#发送任务队列
task_queue = queue.Queue()

#接受结果的队列
result_queue = queue.Queue()


#从BaseManger继承的QueueManager:
class QueueManager(BaseManager):
    pass

def gettask():
    return task_queue;

def getresult():
    return result_queue;

def test():
	#warning: can not use lambda in register fuction in windows
	#error example
	#QueueManager.register('get_task_queue', callable = lambda: task_queue)
	#QueueManager.register('get_result_queue', callable = lambda: result_queue)
	QueueManager.register('get_task_queue', callable = gettask)
	QueueManager.register('get_result_queue', callable = getresult)


	#绑定端口5000，设置验证码‘abc’ need ip adress here
	manager = QueueManager(address = ('192.168.137.1', 5000), authkey = b'abc')

	#启动Queue
	manager.start()

	#获得通过网络访问的Queue对象
	task = manager.get_task_queue()

	result = manager.get_result_queue()
	print('try get result...')
	for i in range(10):
		n = random.randint(0,10000)
		print('put task %d...' % n)
		task.put(n)

	print('try get result...')

	for i in range(10):
		r = result.get(timeout = 10)
		print('result: %s' % r)
		
	#关闭
	manager.shutdown()
	
	print('master exit')   

 
    
if __name__ == '__main__':
    #windows下多进程可能会炸，添加这句可以缓解
    freeze_support()
    test()
    
    
    
    
    
    
    