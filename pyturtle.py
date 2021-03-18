import pygame
import turtle # import the turtle library

screen=turtle.Screen() #give the screen a reference
pointer=turtle.Turtle() # give the turtle a reference


def hl():
    pointer.sety(pointer.ycor()+10) # move the pointer 10 pixels up

def h2():
    pointer.sety(pointer.ycor()-10) # move the pointer 10 pixels down

def h3():
    pointer.forward(10) # move the pointer 10 to the right

def h4():
    pointer.back(10) # move the pointer 10 pixels to the left

screenr.onkey(
