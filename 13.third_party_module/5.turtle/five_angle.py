# -*- coding: utf-8 -*-
from turtle import *
def drawStar(x,y):
    pu()      #pen up
    goto(x,y)
    pd()     #pen down
    
    seth(0) #Set the orientation of the turtle to to_angle
    for i in range(10):
        fd(40) #forward
        rt(36) #right

for x in range(0,250,50):
    drawStar(x,0)

done()
    