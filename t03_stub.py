#################################################################################
# Author:
# Username: hoerstl, ntentiad
#
# Assignment:
# Purpose:
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
def rectangle(w,l,t,pens):
    t.penup()
    t.right(90)
    t.forward(pens/2)
    t.left(90)
    t.forward(pens/2)
    t.pendown()
    for i in range(2):
        t.forward(w-1.5*pens)
        t.right(90)
        t.forward(l-1.5*pens)
        t.right(90)

def boostro(w,l,t,pens):
    t.color("red")
    for i in range(((l-2*pens)//pens)//2):
        t.forward(w - pens*3.5)
        t.right(90)
        t.forward(pens)
        t.right(90)
        t.forward(w -  pens*3.5)
        t.left(90)
        t.forward(pens)
        t.left(90)
    t.forward(w - pens * 3.5)
    t.right(90)
    t.forward(pens)
    t.right(90)
    t.forward(w - pens * 3.5)


def main():
    wn=turtle.Screen()
    w = wn.window_width()
    l = wn.window_height()

    carl = turtle.Turtle()
    carl.speed(1000)
    pens=25
    carl.pensize(pens)
    carl.penup()
    carl.goto(-w/2,l/2)
    carl.pendown()
    rectangle(w,l,carl,pens)
    carl.forward(pens)
    carl.right(90)
    carl.forward(pens)
    carl.left(90)
    boostro(w,l,carl,pens)
    wn.exitonclick()
main()

