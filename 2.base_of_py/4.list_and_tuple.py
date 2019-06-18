#!/usr/bin/env python3

#list
classmates = ['Michael','Bob','Tracy']
print(classmates,len(classmates))

print(classmates[-1])
print(classmates[-2])
#insert 
classmates.insert(1,'Jack')
#delect tail
classmates.pop()
#delect one
classmates.pop(2)
#append tail
classmates.append('Adam')
#change one
classmates[-1] = 'Shane'
print(classmates,len(classmates))

#list in list
classmates2 = ['Diya','Bald']
classmates.insert(0,classmates2)
print(classmates)
print(classmates[0][0])
classmates.insert(-1,'test')
print(classmates)

#Tuple:const list
t = (1) #this is not tuple,pls pay attention!!!!!


t = (1,)
print(t)

t = ('a','b',['a','b'])
print(t)
