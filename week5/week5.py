import math
import random

# for i in  range(10):
#     print(random.random())


# for i in range(10):
#     print(random.randint(25,35))


# import math
# a = int(input("enter a:"))
# b = int(input("enter b:"))
# c = math.hypot(a,b)
#
# print(c)



# def  areaOfCircle(r):
#      area = math.pi * r * r
#      return area
# print(areaOfCircle(4))



# import turtle
# def drawStar(t, side):
#     for i in range(5):
#         t.forward(side)
#         t.right(144)
#
# tess = turtle.Turtle()
# screen = turtle.Screen()
# drawStar(tess, 200)
#
# screen.exitonclick()




def drawSquare(t,side):
     for i in range(4):
         t.forward(side)
         t.left(90)

# import turtle
# tess = turtle.Turtle()
# screen = turtle.Screen()
#
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.pensize(3)
#
# for i in range(5):
#     drawSquare(tess,side=20)
#     tess.penup()
#     tess.forward(40)
#     tess.pendown()
# screen.exitonclick()


import turtle

screen = turtle.Screen()
tess = turtle.Turtle()

screen.bgcolor("lightgreen")
tess.color("red")
tess.pensize(3)

for i  in range(20, 120, 20):
    drawSquare(tess, i)
    tess.penup()
    tess.backward(10)
    tess.right(90)
    tess.forward(10)
    tess.left(90)
    tess.pendown()

screen.exitonclick()
