import math
import random
import tkinter as tk
canvasWidth = 640
canvasHeight = 625

canvasCenterX = (canvasWidth / 2)
canvasCenterY = (canvasHeight / 2)

centerRadius = 10
angleOffset = 90

lineWidth = 3
lineLength = 300

lineNumber = 0
lineObjects = []

colourScale = [(0, 255, 0), (0, 208, 226), (0, 190, 207), (0, 170, 188), (0, 150, 162), (0, 130, 142), (0, 110, 121),
               (0, 90, 100), (0, 75, 75), (0, 50, 50)]

clockwise = True
anticlockwise = False

# Init measurement array (36)

measurement = []

file = open("/home/pi/Desktop/data.csv", 'r')
for rows in file:
    data = rows.split(',')
    measurement.append(data)
file.close()
def updateDisplay():
    global lineNumber, lineObjects, clockwise, anticlockwise, measurement

    # print len(measurement), lineNumber
    file = open("/home/pi/Desktop/data.csv", 'r')
    for rows in file:
        data = rows.split(',')
        measurement.append(data)
    file.close()
    angle = int(measurement[lineNumber][0])
    length = int(measurement[lineNumber][1])
    clockwise = int(measurement[lineNumber][2])
    anticlockwise = int(measurement[lineNumber][2])
    dx = length * math.sin(math.radians(angleOffset - angle))
    dy = length * math.cos(math.radians(angleOffset - angle))

    colour = '#%02x%02x%02x' % colourScale[0]
    lineObjects.append(
        canvas.create_line(canvasCenterX, canvasCenterY, dx + canvasCenterX, dy + canvasCenterY, width=lineWidth,
                           fill=colour))

    if lineNumber != 0:
        if clockwise:
            canvas.delete(lineObjects[lineNumber - 1])

            angle = int(measurement[lineNumber - 1][0])
            length = int(measurement[lineNumber - 1][1])
            clockwise = int(measurement[lineNumber-1][2])
            anticlockwise = int(measurement[lineNumber-1][2])
            dx = length * math.sin(math.radians(angleOffset - angle))
            dy = length * math.cos(math.radians(angleOffset - angle))

            colour = '#%02x%02x%02x' % colourScale[1]
            lineObjects[lineNumber - 1] = canvas.create_line(canvasCenterX, canvasCenterY, dx + canvasCenterX,
                                                             dy + canvasCenterY, width=lineWidth, fill=colour)
        else:
            if lineNumber < (len(measurement) - 1):
                canvas.delete(lineObjects[lineNumber + 1])

                angle = int(measurement[lineNumber + 1][0])
                length = int(measurement[lineNumber + 1][1])
                clockwise = int(measurement[lineNumber+1][2])
                anticlockwise = int(measurement[lineNumber+1][2])
                dx = length * math.sin(math.radians(angleOffset - angle))
                dy = length * math.cos(math.radians(angleOffset - angle))

                colour = '#%02x%02x%02x' % colourScale[1]
                lineObjects[lineNumber + 1] = canvas.create_line(canvasCenterX, canvasCenterY, dx + canvasCenterX,
                                                                 dy + canvasCenterY, width=lineWidth, fill=colour)

    if clockwise:
        lineNumber += 1
    else:
        lineNumber -= 1

    if ((lineNumber == len(measurement)) and clockwise) or ((lineNumber == -1) and anticlockwise):
        for i in range(0, len(lineObjects)):
            canvas.delete(lineObjects[i])

        lineObjects = []
        for i in range(0, len(measurement)):
            angle = measurement[i][0]
            length = measurement[i][1]

            dx = length * math.sin(math.radians(angleOffset - angle))
            dy = length * math.cos(math.radians(angleOffset - angle))

            colour = '#%02x%02x%02x' % colourScale[5]
            lineObjects.append(canvas.create_line(canvasCenterX, canvasCenterY, dx + canvasCenterX, dy + canvasCenterY,
                                                  width=lineWidth, fill=colour))

        if clockwise:
            clockwise = False
            anticlockwise = True
            lineNumber -= 1
        else:
            clockwise = True
            anticlockwise = False
            lineNumber = 0
        
        '''measurement = []
        for i in range(0, 360, 5):
            ran_number = random.random()
            distance = int(ran_number * 300)
            measurementData = (i, distance)
            measurement.append(measurementData)'''

    root.after(200, updateDisplay)


root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

canvas = tk.Canvas(frame, width=canvasWidth, height=canvasHeight, bg='black')
canvas.pack(expand=tk.YES)

photo = tk.PhotoImage(file="//home//pi//Desktop//background2.gif")
canvas.create_image(0, 0, image=photo, anchor=tk.NW)

colour = '#%02x%02x%02x' % colourScale[8]
canvas.create_oval(canvasCenterX - centerRadius, canvasCenterY - centerRadius, canvasCenterX + centerRadius,
                   canvasCenterY + centerRadius, width=0, fill=colour)

root.after(0, updateDisplay)
root.mainloop()