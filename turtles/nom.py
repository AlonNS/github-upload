from turtle import *
import random
from math import exp

CourtSize = 600
BorderSize = 50

def wall(turtle,mode='colide'):    
    if turtle.xcor() > CourtSize//2 - 6 or turtle.xcor() < 6 - CourtSize//2:
        if mode == 'colide':
            player.setheading(180-player.heading())
        elif mode == 'pacman':
            turtle.ht()
            s = turtle.speed()
            turtle.speed(0)
            turtle.setx(-turtle.xcor())
            turtle.speed(s)
            turtle.st()            
    if turtle.ycor() > CourtSize//2 - 6 or turtle.ycor() < 6 - CourtSize//2:
        if mode == 'colide':
            turtle.setheading(360-player.heading())
        elif mode == 'pacman':
            turtle.ht()
            s = turtle.speed()
            turtle.speed(0)
            turtle.sety(-turtle.ycor())
            turtle.speed(s)
            turtle.st()
            
def randpos():
    x = random.randint(-CourtSize//2,CourtSize//2)
    y = random.randint(-CourtSize//2,CourtSize//2)
    return (x,y)


def eat(turtle,food,n):
    LunchTime = 50
    pause = 100
    sense = CourtSize/5
    if n == 0:
        if turtle.distance(food) < 20:
            return (1,0)
        else:
            angle = (turtle.heading()-turtle.towards(food))% 360 - 180
            dist = turtle.distance(food)
            s = turtle.speed()
            turtle.speed(0)            
            if angle > 0:
                turtle.left(min(angle,5*exp(-(dist/sense)**2)))
            else:
                turtle.right(min(-angle,5*exp(-(dist/sense)**2)))
            turtle.speed(s)   
            return (0,1)        
    elif n <= LunchTime:
        d = turtle.distance(food)//25
        if n%5 != 0: d = 0
        return (n+1,d)
    elif n < LunchTime+pause:
        food.ht()
        return (n+1,1)
    else:
        food.setpos(randpos())
        food.st()
        return(0,1)
        


setup(width=CourtSize+2*BorderSize, height=CourtSize+2*BorderSize)
bgcolor(.7,.7,.7)

Yehoshua = Turtle()
Yehoshua.speed(10)
Yehoshua.penup()
Yehoshua.setposition(-CourtSize//2,-CourtSize//2)
Yehoshua.pendown()
Yehoshua.pensize(2)
Yehoshua.fillcolor(.2,1,.6)
Yehoshua.begin_fill()
for i in range(4):
    Yehoshua.forward(CourtSize)
    Yehoshua.left(90)
Yehoshua.end_fill()

players = (Batz, Tzabi) = (Turtle(),Turtle())
for player in players:
    player.penup()
    player.shape('turtle')
    
Batz.color(0,.7,0)
Batz.right(37)

Tzabi.color(0,.6,.1)
Tzabi.setpos(100,50)
Tzabi.left(41)

cabbage = Turtle()
cabbage.shape('circle')
cabbage.color(.4,0,.3)
cabbage.speed(0)
cabbage.penup()
cabbage.setpos(randpos())
cabbage.shapesize(.5,.5)


delay(5)

n = 0
ds = [1,1]
ns = [0,0]

while True:
    for i,player in enumerate(players):
        player.fd(ds[i])
        wall(player)
        (ns[i],ds[i]) = eat(player,cabbage,n)
    n = max(ns)

    if Batz.distance(Tzabi) < 20:
        h = [player.heading() for player in players]
        Batz.setheading(h[1])
        Tzabi.setheading(h[0])
        
exitonclick()