import turtle
import random
import time
import winsound


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


def MeteorGenerate(meteorName):
    meteorName.shape("meteor2.gif")
    meteorName.penup()
    MeteorReset(meteorName)


def MeteorReset(meteorName):
    meteorName.setx(random.randrange(380, 480, 10))
    meteorName.sety(random.randrange(-300, 300, 10))


def MeteorMovement(meteorName):
    meteorName.setx(meteorName.xcor() - 5)
    if meteorName.xcor() < -400:
        MeteorReset(meteorName)
    if ship.xcor()-30 < meteor.xcor() < ship.xcor()+30 and ship.ycor()-30 < meteorName.ycor() < ship.ycor()+30:
        MeteorReset(meteorName)
        winsound.PlaySound("explosion-01.wav", winsound.SND_ASYNC)

        global shipHP
        shipHP -= 1
        kijelzo.clear()
        kijelzo.write(shipHP, font=("Arial", 28, "bold"))
        if shipHP == 0:
            kijelzo.clear()
            kijelzo.write("Meghaltál!", font=("Arial", 28, "bold"))
            ship.clear()
            ship.ht()


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

shipHP = 3

kijelzo = turtle.Turtle()
kijelzo.color("white")
kijelzo.hideturtle()
kijelzo.penup()
kijelzo.goto(-100, 250)
kijelzo.write(shipHP, font=("Arial", 28, "bold"))

ship = turtle.Turtle()
ship.shape("sprite.gif")
ship.penup()

meteor = turtle.Turtle()
MeteorGenerate(meteor)

meteor2 = turtle.Turtle()
MeteorGenerate(meteor2)

meteor3 = turtle.Turtle()
MeteorGenerate(meteor3)

meteor4 = turtle.Turtle()
MeteorGenerate(meteor4)

while True:
    space.update()
    MeteorMovement(meteor)
    MeteorMovement(meteor2)
    MeteorMovement(meteor3)
    MeteorMovement(meteor4)
    if ship.ycor() > 300:
        ship.sety(-300)
    if ship.ycor() < -300:
        ship.sety(300)
    if ship.xcor() > 400:
        ship.setx(-400)
    if ship.xcor() < -400:
        ship.setx(400)
    time.sleep(0.0001)
