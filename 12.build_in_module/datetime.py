# -*- coding: utf-8 -*-
import re
from datetime import datetime,timedelta,timezone
dt = datetime(2019,8,4,21,20,53,500000)
t = dt.timestamp()
print(dt)
print(t)
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

cday = datetime.strptime('2019-8-4 21:20:53','%Y-%m-%d %H:%M:%S')

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

print(now+timedelta(hours=10))
print(now-timedelta(days=1))
print(now+timedelta(days=2, hours=12))


tz_utc_8 = timezone(timedelta(hours = 8))

now = datetime.now()

dt = now.replace(tzinfo = tz_utc_8)

tzinfo = timezone(timedelta(0,28800))

utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))

print(bj_dt)

def to_timestamp(dt_str, tz_str):
#1. 正则匹配
    dt_catch = re.match(r'^(\d{4})-(\d{1,2})-(\d{1,2})[\s]+(\d{1,2}):(\d{1,2}):(\d{1,2})$' ,dt_str)    
#2. 读取时间
    year   =  dt_catch.group(1)
    month  =  dt_catch.group(2)
    day    =  dt_catch.group(3)
    hour   =  dt_catch.group(4)
    minute =  dt_catch.group(5)
    second =  dt_catch.group(6)
    #设置时间
    dt = datetime(int(year),int(month),int(day),int(hour),int(minute),int(second))
    print(dt)
#3. 读取UTC
    tz_catch = re.match(r'UTC(\+|\-)(\d{1,2}):(\d{1,2})',tz_str)
    
    utc_polarity = tz_catch.group(1)    
    utc_hour = tz_catch.group(2)   
    utc_minute = tz_catch.group(3)

#4. 设置UTC
    if '+' == utc_polarity:  
        tz_utc_read = timezone(timedelta(hours = int(utc_hour),minutes = int(utc_minute)))
        
    else:
        tz_utc_read = timezone(-timedelta(hours = int(utc_hour),minutes = int(utc_minute)))

    utc_dt = dt.replace(tzinfo = tz_utc_read)

    dt_stamp = utc_dt.timestamp()
    return dt_stamp


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
#print(t1)
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

