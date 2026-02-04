import turtle
from turtle import *
t = Turtle()

""" for i in range (4):
    t.forward(100)
    t.left(90) """

""" sidelength = 100
rotate = 90
def square(x,y):
    for i in range (4):
        t.forward(x)
        t.left(y)
square(100,90) """
# above does not work

""" for i in range(60):
    side = 100
    rotate = 5
    def square(x,y):
        for i in range(4):
            t.forward(x)
            t.left(y)
    square(100,90)
    t.right(5) """
# above does not work

""" for i in range (4):
    t.forward(100)
    t.left(90) """

""" for i in range(60):
    side = 100
    rotate = 90
    def square(x,y):
        for i in range(4):
            t.forward(x)
            t.left(y)
    square(100,90) """
# above does not work

""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def squares(iRange):
    x = 25
    for i in range(iRange):
        square(x, 90)
        x = x * 2
squares(5) """

""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def squares(iRange):
    x = 25
    for i in range(iRange):
        square(x, 90)
        x += 25
squares(5) """

""" sidelength = 100
rotate = 90
def triangle (x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)
triangle(100,90) """
#above code does not work

""" for i in range(60):
    side = 50
    rotate = 90
    def square(x,y):
        x = 50
        for i in range(4):
            t.forward(x) 
            t.left(y)
    square(50,90) """
#above code does not work

""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def squares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length += 5
squares(5,90) """
#above code does not work

""" def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def squares(iRange):
    x = 5
    for i in range(iRange):
        square(x, 90)
        x += 5
        t.right(5)
squares(60) """

""" t.speed('fastest')

def star(x,y):
    for i in range(5):
        t.forward(x)
        t.left(y)

def stars(iRange):
    x = 5
    for i in range(iRange):
        star(x, 144)
        x += 5
        t.right(5)
stars(60) """

turtle.done()