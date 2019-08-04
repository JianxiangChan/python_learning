# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#!usr/bin/python
import re

def is_valid_email(addr):
    return re.match(r'[\w\.]*@[0-9a-zA-Z]*\.com',addr)

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')

print(re.match(r'[\w]*','adfa312..32.....'))
print(re.match(r'[\w]+','adfa312..32.....'))

def name_of_email(addr):
    return re.match(r'.*?([\w\s]+)@*', addr).group(1)


print(name_of_email('<Tom Paris> tom@voyager.org'))


print(name_of_email('tom@voyager.org'))
