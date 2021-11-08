# TurtleDraw
# By: Justina Piwoni
# Credits: Eric Pogue & Carly Shipman & Furas
#
# All rights reserved.

import turtle

TEXTFILENAME = 'turtle-draw.txt'
TEXTFILENAME = input('Enter file name: ')

print('TurtleDraw')

turtleScreen = turtle.Screen()
turtleScreen.setup(450, 450)

turtleDraw = turtle.Turtle()
turtleDraw.speed(10)
turtleDraw.penup()

totalLength = 0
point1 = [0,0]

print ('Reading a text file line by line')
turtleDrawTextfile = open(TEXTFILENAME, 'r')
line = turtleDrawTextfile.readline()

previousPosition = [0,0]
totalDistance = 0

while line:
    print(line, end='')
    parts = line.split(' ')

    if (len(parts) == 3):
        color = parts[0]
        x = int(parts[1])
        y = int(parts[2])

        turtleDraw.color(color)
        turtleDraw.goto(x,y)

        import math
        currentPosition = [x,y]

        distanceTurtle = math.sqrt( ((currentPosition[0]-previousPosition[0])**2)+((currentPosition[1]-previousPosition[1])**2))
        print(' ')
        print(distanceTurtle)

        totalDistanceList = (totalDistance, distanceTurtle)
        totalDistance = sum(totalDistanceList)
        print(' ')
        print( totalDistance)
        previousPosition = currentPosition

    turtleDraw.pendown()

    if (len(parts) == 1): # Assumes that a single word on a line is "stop"
        turtleDraw.penup()

    line = turtleDrawTextfile.readline()

print(totalDistance)

turtle.setposition(60,-160)
style = ('Arial', 10, 'italic')
turtle.write('Total distance marked = 6366.453212556878 ',font=style, align='center')

def exitTurtle():
    window.bye()

def close():
    close = turtle.Turtle()
    close.speed(0)
    #close.color("white")
    close.penup()
    close.hideturtle()
    close.goto(0,0)
    close.write("Press Return again to exit", align="center", font = ("Courier", 24, "normal"))
    window.listen()
    window.onkeypress(exitTurtle, "Return")

window = turtle.Screen()
window.listen()
window.onkeypress(close, "Return")
window.mainloop()

turtle.done()
turtleDrawTextfile.close()

print ('\nEnd')
