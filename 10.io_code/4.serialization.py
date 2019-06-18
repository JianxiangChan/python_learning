# -*- coding: utf-8 -*-
import pickle

d = dict(name = 'bob', age = 20, score = 88)

print(pickle.dumps(d))  #use of dumps


with open('dump.txt','wb') as f:
    pickle.dump(d,f)