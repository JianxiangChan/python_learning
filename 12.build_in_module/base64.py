# -*- coding: utf-8 -*-
import base64

print(base64.b64encode(b'binary string'))
print(base64.b64decode(b'YmluYXJ5IHN0cmluZw=='))
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))


print('###########################')
def safe_base64_decode(s):
    if len(s)%4 != 0:
        s = s + b'=' * (4-len(s)%4)
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
