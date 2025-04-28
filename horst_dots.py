import random
import turtle
from turtle import Turtle,Screen
turtle.colormode(255)
tom=Turtle()
s1=Screen()
tom.penup()
tom.speed(10)
for i in range(300):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.pencolor(r,g,b)
    
    tom.goto(random.randint(-300,300),random.randint(-300,300))
    tom.dot(20)












s1.exitonclick()
