# -*- coding: utf-8 -*-

import psutil
import json
from datetime import datetime

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

print(psutil.cpu_times())

for x in range(10):
    print(psutil.cpu_percent(interval=0.1,percpu=True))
    
print(psutil.virtual_memory())
print(psutil.swap_memory())

print(psutil.disk_partitions()) # 磁盘分区信息

print(psutil.disk_usage('/')) # 磁盘分区信息

print(psutil.disk_io_counters()) # 磁盘IO

print(psutil.net_io_counters()) # 获取网络读写字节／包的个数

print(psutil.net_if_addrs()) # 获取网络接口信息
j = json.dumps(psutil.net_if_addrs())
print('-----------------------')
print(j)

print(psutil.net_connections())

print(psutil.pids() )

p = psutil.Process(16204)

print(p.name())
print(p.exe())
print(p.cwd())
print(p.cmdline())
print(p.ppid())
print(p.parent())
print(p.children())
print(p.status())
print(p.username())
(p.create_time())

print(datetime.fromtimestamp(p.create_time()))

print(p.cpu_times())

print(p.memory_info())

print(p.open_files())
print(p.connections())
print(p.num_threads())

print(p.threads())
print(p.environ())
psutil.test()

#print(p.terminate())
