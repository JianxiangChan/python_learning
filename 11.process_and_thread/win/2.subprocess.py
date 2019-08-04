# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#!usr/bin/python

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])

print('Exit code', r)
