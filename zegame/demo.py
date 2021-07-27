import os
import sys
import time 
import tkinter
from tkinter.constants import X
import turtle
from random import choice, randint 
tiempo = 0.1
porce = [1]
primeri = 1
window = turtle.Screen()
window.title("Zero Game")
window.bgcolor("black")
window.setup(width=600,height=600)
window.tracer(0)
g, h = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,99999999999999999999999999999999999999999999999999999999999999999999999999999999999
#GOOD
head = turtle.Turtle()
head.speed(0)
head.shape('triangle')
colorc = (choice(['white','pink', 'green', 'red', 'blue', 'yellow']))
head.color(colorc)
head.penup()
head.goto(0,0)
#Points
food = turtle.Turtle()
food.speed(0)
food.penup()
food.shape('square')
colord = 'yellow'
food.color(colord)
food.goto(70,100)

food1 = turtle.Turtle()
food1.speed(0)
food1.penup()
food1.shape('square')
colord1 = 'cyan'
food1.color(colord1)
food1.goto(100,100)

food2 = turtle.Turtle()
food2.speed(0)
food2.penup()
food2.shape('square')
colord2 = 'white'
food2.color(colord2)
food2.goto(20,100)
head.direction = None
golor = 'black'

fubad = turtle.Turtle()
fubad.speed(0)
fubad.shape('triangle')
colorf = choice(['red','brown'])
fubad.color(colorf)
fubad.penup()
fubad.goto(0,0)
#Funciones
def a0():
    fubad.direction = '1'
    head.direction = 'a'
def a1():
    head.direction = 'b'
    fubad.direction = '2'
def a2():
    head.direction = 'c'
    fubad.direction = '3'
def a3():
    head.direction = 'd'
    
def cruceta():
    colorc = (choice(['white','pink', 'green', 'red', 'blue', 'yellow']))
    head.color(colorc)
    figure = 'circle'
    head.shape(figure)
    if head.direction == 'a':
        y = head.ycor()
        head.sety(y+20)
        head.direction = None
        porce.append(1)
    elif head.direction == 'b':
        y = head.ycor()
        head.sety(y-20)
        head.direction = None
        porce.append(1)
    elif head.direction == 'c':
        x = head.xcor()
        head.setx(x+20)
        head.direction = None
        porce.append(1)
    elif head.direction == 'd':
        x = head.xcor()
        head.setx(x-20)
        head.direction = None
        porce.append(1)
#BADi
    if head.direction == 'a':
        y = head.ycor()
        head.sety(y+20)
        head.direction = None
    elif head.direction == 'b':
        y = head.ycor()
        head.sety(y-20)
        head.direction = None
    elif head.direction == 'c':
        x = head.xcor()
        head.setx(x+20)
        head.direction = None
    elif head.direction == 'd':
        x = head.xcor()
        head.setx(x-20)
        head.direction = None
#Board 
window.listen()
window.onkeypress(a0, 'w')
window.onkeypress(a1, 's')
window.onkeypress(a2, 'd')
window.onkeypress(a3, 'a')
#Correr
punt = []
mpc = [food]
while True:
   window.update()
   #chaos
   def zeg():
      for c in range(0,1):
         food3 = turtle.Turtle()
         food3.speed(0)
         food3.penup()
         food3.shape('square')
         colord3 = 'red'
         food3.color(colord3)

         ab0, ab1 = randint(-900,900), randint(-200,200)
         food3.goto(-ab0,ab1)
         porce.clear()
         mpc.append(food3)
   
   if len(porce) == 3:
       zeg()
   #BAD
   def fun():
       d0, d1 = randint(0, 30), randint(0,30)
       fubad.goto(-d0,d1)
    
    #Ida
   if head.distance(food) < 20:
       food.goto(-g,h)
       punt.append(1)
   if head.distance(food1) < 20:
       food1.goto(-g,h)
       punt.append(1)
   if head.distance(food2) < 20:
       food2.goto(-g,h)
       punt.append(1)
   for cd in range(1,len(mpc)):
      if head.distance(mpc[cd]) < 20:
       print("Perdiste!")
       exit()
   fun()
   #Regreso
   if len(punt) == 3:
       x0 = randint(-200,200)
       y0 = randint(-200,200)
       food.goto(x0,y0)

       x1 = randint(-200,200)
       y1 = randint(-200,200)
       food1.goto(x1,y1)

       x2 = randint(-200,200)
       y2 = randint(-200,200)
       food2.goto(x2,y2)
       punt.clear()
       
   cruceta()
   time.sleep(tiempo)
   