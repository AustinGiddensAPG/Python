#This is the beginning to the code. This basically gets the Turtle going, importing the use of the program while the code runs.
import turtle
wn = turtle.Screen()
wn.bgcolor("black")
turtle = turtle.Turtle()
turtle.speed(0)
turtle.penup()
turtle.shape("turtle")

#This is the code that draws the initial rectangle that is the outline to the flag.
def drawFillRectangle(x, y, length, width, color):
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    
#This is the code that draws the stars on the flag. It then repeats to properly fill the flag with stars.
def drawStar(x,y,color,length) :
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(color)
    for turn in range(0,5) :
        turtle.forward(length)
        turtle.right(144)
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()

#This code draws out all the stripes on the flag.
def drawStripes() :
    x = -230
    y = 125
    for stripe in range(0,6) :
        drawFillRectangle(x, y, 18, 460, 'red')
        y = y - 20
        drawFillRectangle(x, y, 18, 460, 'white')
        y = y - 19
    drawFillRectangle(x, y, 18, 460, 'red')
    y = y - 20
    
#This code draws the quare where the stars go.
def drawSquare() :
    drawFillRectangle(-230, 125, 135, 150, 'navy')

#Other code that actually inserts the stars.
def drawSixStars() :
    y = 115
    for row in range(0,5) :
        x = -230
        y = y - 4
        for star in range (0,6) :
            x = x + 6
            drawStar(x, y, 'white', 10)
            x = x + 19
        y = y - 20
        
#Other code that actually draws the stars
def drawFiveStars() :
    y = 103
    for row in range(0,4) :
        x = -212
        y = y - 4
        for star in range (0,5) :
            drawStar(x, y, 'white', 10)
            x = x + 25
        y = y - 20

drawStripes()
drawSquare()
drawSixStars()
drawFiveStars()
turtle.goto(0,-140)
turtle.write("GOD BLESS THE USA")
turtle.back(20)

#This python code utilizies repeat turtle commands to properly draw out the flag and all of its components.
