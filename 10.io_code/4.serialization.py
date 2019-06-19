# -*- coding: utf-8 -*-
import pickle

d = dict(name = 'bob', age = 20, score = 88)

print(pickle.dumps(d))  #use of dumps


with open('dump.txt','wb') as f:
    pickle.dump(d,f)

with open('dump.txt','rb') as f:
    d = pickle.load(f)
    
print(d)

import json

d = dict(name = 'bob', age = 20, score = 88)

print(json.dumps(d))

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
        
s = Student('bob', 20 , 80)
def student2dict(std):
    return {
            'name' : std.name,
            'age' : std.age,
            'score' : std.score
}
    
print(json.dumps(s, default = student2dict))

print(json.dumps(s, default = lambda obj: obj.__dict__))

s = json.dumps(s, default = lambda obj: obj.__dict__)

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

print(json.loads(s , object_hook = dict2student))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=False)
print(s)
s = json.dumps(obj)
print(s)
