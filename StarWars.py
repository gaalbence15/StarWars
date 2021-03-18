import turtle


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
space.listen()
space.onkeypress(Up, "Up")
space.onkeypress(Down, "Down")
space.onkeypress(Right, "Right")
space.onkeypress(Left, "Left")


ship = turtle.Turtle()
ship.shape("sprite.gif")
ship.penup()

while True:
    space.update()
    if ship.ycor() > 300:
        ship.sety(-300)
    if ship.ycor() < -300:
        ship.sety(300)
    if ship.xcor() > 400:
        ship.setx(-400)
    if ship.xcor() < -400:
        ship.setx(400)
