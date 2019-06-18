#!/usr/bin/env python3
# -*- coding: utf-8 -*-

age = input('birth: ') #age is not a int here!!!
age = int(age)
if age >= 18:
    print('your age is',age)
    print('adult')
elif age >= 6:
    print('your age is',age)
    print('teenager')
else:
    print('your age is',age)
    print('kid')

height = float(input('height = ____m\b\b\b\b\b'))
weight = float(input('weight = ____kg\b\b\b\b\b\b'))
bmi = weight/(height * height)
if bmi < 18.5:
	print('过轻')
elif bmi > 18.5 and bmi < 25:
	print('正常')
elif bmi > 25 and bmi < 28:
	print('过胖')
elif bmi > 28 and bmi < 32:
	print('肥胖')
elif bmi > 32:
	print('严重肥胖')
