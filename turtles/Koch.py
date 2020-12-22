from turtle import *

def koch(n,s):
    if n == 0: fd(s)
    else:
        koch(n-1,s/3)
        lt(60)
        koch(n-1,s/3)
        rt(120)
        koch(n-1,s/3)
        lt(60)
        koch(n-1,s/3)
        
setup (width=600, height=600)
        
fillcolor(.7,.8,1)
pu()
setpos(-243,140)
pd()
speed(2)
delay(15)


for n in range(6):
    delay(delay()/3)
    speed(speed()+1)
    begin_fill()
    for i in range(3):
        koch(n,486)
        rt(120)
    end_fill()

exitonclick()