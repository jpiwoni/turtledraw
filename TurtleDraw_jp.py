# TurtleDraw
# By: Justina Piwoni
# Credits: Eric Pogue & Carly Shipman
#
# All rights reserved.

import turtle

TEXTFILENAME = 'turtle-draw.txt'

# ToDo: Ask user for the file name.

print('TurtleDraw')

turtleScreen = turtle.Screen()
turtleScreen.setup(450, 450)

turtleDrawLite = turtle.Turtle()
turtleDrawLite.speed(10)
turtleDrawLite.penup()


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


        turtleDrawLite.color(color)
        turtleDrawLite.goto(x,y)

        # Todo: Calculate the distance and add it to the total distance.

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

    turtleDrawLite.pendown()

    if (len(parts) == 1): # Assumes that a single word on a line is "stop"
        turtleDrawLite.penup()

    line = turtleDrawTextfile.readline()

print(totalDistance)

# Todo: Print the total near the bottom.

turtle.done()
turtleDrawTextfile.close()

# Todo: Wait for the user to press the enter key before closing.

print ('\nEnd')
