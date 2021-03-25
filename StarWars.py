import turtle
import random
import time


def Up():
    ypos = ship.ycor()
    ypos += 20
    ship.sety(ypos)


def Down():
    ypos = ship.ycor()
    ypos -= 20
    ship.sety(ypos)


def Right():
    xpos = ship.xcor()
    xpos += 20
    ship.setx(xpos)


def Left():
    xpos = ship.xcor()
    xpos -= 20
    ship.setx(xpos)


space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("space.png")
space.addshape("sprite.gif")
space.addshape("meteor2.gif")
space.listen()
space.onkeypress(Up, "Up")
space.onkeypress(Down, "Down")
space.onkeypress(Right, "Right")
space.onkeypress(Left, "Left")
space.tracer(0)

ship = turtle.Turtle()
ship.shape("sprite.gif")
ship.penup()

meteor = turtle.Turtle()
meteor.shape("meteor2.gif")
meteor.penup()
meteor.setx(380)

while True:
    space.update()
    meteor.setx(meteor.xcor() - 4)
    if ship.ycor() > 300:
        ship.sety(-300)
    if ship.ycor() < -300:
        ship.sety(300)
    if ship.xcor() > 400:
        ship.setx(-400)
    if ship.xcor() < -400:
        ship.setx(400)
    if meteor.xcor()< -400:
        meteor.setx(400)
        meteor.sety(random.randrange(-300, 300, 1))
    time.sleep(0.0001)
