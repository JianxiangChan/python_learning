# -*- coding: utf-8 -*-

from urllib import request,parse
import json

"""
with request.urlopen('https://api.douban.com/v2/book/12345') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k, v))
    print('data', data.decode('utf-8'))
""" 

req = request.Request('http://www.douban.com/')

req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print('data:',f.read().decode('utf-8'))
    
print('Login to weibo.cn...')
email = '849456161@qq.com'
passwd = 'XIANG-NG15251123'

login_data = parse.urlencode([
         ('username', email),
        ('password', passwd),
        ('entry', 'mweibo'),
        ('client_id', ''),
        ('savestate', '1'),
        ('ec', ''),
        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
        ])
print(login_data)

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
    
    
URL = 'https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/urllibTest'

def fetch_data(url):

    with request.urlopen('https://www.easy-mock.com/mock/5cbec5d8bfb3b05625e96633/dreamlf/urllibTest') as f:

        data = f.read()
        
        data_str = data.decode('utf-8')
        print(data_str)
        return json.loads(data_str)

data = fetch_data(URL)
json_dict = json.dumps(data,indent=4)
print(json_dict)

print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')
