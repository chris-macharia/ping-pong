# Simple pong game for beginners
# Author: Chris Macharia

import turtle

win = turtle.Screen()
win.title("Pong by Chris Macharia")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Main game loop
while True:
    win.update()