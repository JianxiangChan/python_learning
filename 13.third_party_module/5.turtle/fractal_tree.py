# -*- coding: utf-8 -*-

from turtle import *

colormode(255)


lt(90)

lv = 14

l = 120

s = 45

width(lv)

r = 0

g = 0

b = 0

pencolor(r,g,b)

pu()

bk(l)

pd()

fd(l)

def draw_tree(l, level):
    global r,g,b
    w = width()
    
    width(w*3.0/4.0)
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)
    
    l = 3.0/4.0*l
    
    lt(s)
    
    fd(l)
    
    if level < lv:
        draw_tree(l, level+1)
    
    bk(l)
    rt(2*s)
    fd(l)
    
    if level < lv:
        draw_tree(l, level+1)
    
    bk(l)
    lt(s)
    
    width(w)
    
speed(0)

draw_tree(l,4)
    
    
    
    