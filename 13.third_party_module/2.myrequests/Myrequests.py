# -*- coding: utf-8 -*-
import requests

r = requests.get('https://www.douban.com/') 
r.status_code
with open('douban.html','w',encoding = 'utf-8') as f:
    f.write(r.text)
 
print(r.url)

print(r.status_code)
print(r.encoding)
print(r.headers)
print(r.headers['Content-Type'])
#print(r.cookies['ts'])

r = requests.get('https://www.douban.com/search', params = {'q':'python','cat':'1001'})



cs = {'token': '12345', 'status': 'working'}
r = requests.get('https://www.douban.com/', cookies=cs)
#print(r.content)

with open('search.html','w',encoding = 'utf-8') as f:
    f.write(r.text)

r = requests.get('https://www.douban.com/', headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

with open('douban_iphone.html','w',encoding = 'utf-8') as f:
    f.write(r.text)
    
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})


url = 'https://www.douban.com/'
params = {'key': 'value'}
r = requests.post(url, json=params)

upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)


def get_cookie():
    url = "https://fanyi.baidu.com"
    headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'}
    req = requests.get(url, headers= headers)
    print(f'{req.status_code}')
    print(f'{req.cookies}\n')
    for item in req.cookies:  # cookie信息
        print(f'Name = {item.name}')
        print(f'Value = {item.value}')
    
get_cookie()