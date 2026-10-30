# def sumTo(n):
#     total = n * (n + 1) / 2
#     return total
#
# print(sumTo(10))
#
# n = int(input("Enter a number: "))
# print(sumTo(n))
import math
import turtle
# def drawStar(t, n, size):
#     angle = 180-180/n
#     for i in range(n):
#         t.forward(size)
#         t.right(angle)
#
# wn = turtle.Screen()
# t=turtle.Turtle()
# t.pensize(3)
#
# drawStar(t, 7, 100)
# wn.exitonclick()




# def sumTo(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     return total
#
# print(sumTo(10))
# n = int(input("Enter a number: "))
# print(sumTo(n))


# def mySqrt(n):
#     guess = n/2
#     for i in range(20):
#         guess = (1/2) * (guess + (n/guess))
#         print(guess)
#     return guess
#
# n = int(input("Enter a positive integer: "))
# print(math.sqrt(n))
# print(mySqrt(n))


# import turtle
# def  drawSprite(someturtle, legs, length):
#     angle = 360/legs
#     for i in range(legs):
#         someturtle.forward(length)
#         someturtle.left(angle)
#         someturtle.backward(length)
#
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSprite(t, 8, 20)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# t = turtle.Turtle()
# t.color("hotpink")
# t.pensize(2)
#
# fancySquare(t, 100)


#wn.exitonclick()


# import turtle
# def drawTip(t, size):
#     t.begin_fill()
#     t.left(90)
#     t.forward(size/2)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size)
#     t.right(120)
#     t.forward(size/2)
#     t.right(90)
#     t.end_fill()
#
# def drawSpriteWithTips(someturtle, legs, lenght):
#     angle = 360/legs
#     for i in range(legs):
#         someturtle.forward(lenght)
#         drawTip(someturtle,10)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
#
# def fancySquare(t, size):
#     for corner in range(4):
#         drawSpriteWithTips(t, 8, 20)
#         t.forward(size)
#         t.left(90)
#
# t = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("black")
# t.color("white")
# t.pensize(2)
# t.speed(0)
# fancySquare(t,100)
#
# wn.exitonclick()


# def checknumber(n):
#     if n > 0:
#         return "positive"
#     elif n<0:
#         return "negative"
#     else:
#         return "zero"
#
# number_list=[-7,0,5]
#
# for number in number_list:
#     print(checknumber(number))
#
# n = int(input("Enter a number: "))
# print(checknumber(n))

import turtle




def drawBar(t, height, gap):
    t.penup()
    t.left(90)
    t.forward(height+gap)
    t.write(" " + str(height))
    t.backward(height + gap)
    t.right(90)
    t.pendown()


    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def barChart(data):
    maxheight = max(data)
    num_bars = len(data)

    border = 10
    gap=(maxheight + border)/25

    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    right = 40 * num_bars+border
    top=maxheight+4*border
    wn.setworldcoordinates(-border,-border,right,top)

    t = turtle.Turtle()
    t.color("blue")
    t.fillcolor("red")
    t.pensize(3)

    for height in data:
        drawBar(t, height, gap)

    wn.exitonclick()

data = [48,117,200,240,160,260,220]
barChart(data)