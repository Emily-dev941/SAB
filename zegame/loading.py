import sys
import turtle
import time
import os
from random import choice, randint 
xindow = turtle.Screen()
xindow.title('______________________')
xindow.bgcolor('gray3')
xindow.setup(width=470,height=470)
xindow.screensize(200, 100)
x = 0
while x < 6:
   line = turtle.Turtle()
   line.speed(90)
   for cis in range(10):
      line.hideturtle()
      line.goto(0,0)
      turtle.colormode(255)
      a, b, c = randint(0,255), randint(0,255), randint(0,255)
      line.pencolor(a,b,c)
      line.pensize(3)
      line.forward(90)
      line.left(100)
   xindow.title('Loading')
   time.sleep(00.1)
   xindow.title('Loading.')
   time.sleep(00.1)
   xindow.title('Loading..')
   time.sleep(00.1)
   xindow.title('Loading...')
   time.sleep(00.1)
   x = x+1
xindow.bye()
os.system('python menu.py')