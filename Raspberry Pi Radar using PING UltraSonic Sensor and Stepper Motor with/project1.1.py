import RPi.GPIO as GPIO
from time import sleep
import time
import math
import random
import tkinter as tk
DIR = 20
STEP = 21
CW =1
CCW =0
US = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR,CW)
GPIO.setwarnings(False)

measurement = []
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
def ReadDistance(pin):
   GPIO.setup(US, GPIO.OUT)
   GPIO.output(pin, 0)

   sleep(0.000002)


   #send trigger signal
   GPIO.output(pin, 1)


   sleep(0.000005)


   GPIO.output(pin, 0)


   GPIO.setup(pin, GPIO.IN)


   while GPIO.input(pin)==0:
      starttime=time.time()


   while GPIO.input(pin)==1:
      endtime=time.time()
      
   duration=endtime-starttime
   # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s 
   distance=duration*34000/2
   return distance

def fillData(angle, radius):
    measurementData = (angle, radius)
    measurement.append(measurementData)
sleep(1)
GPIO.output(DIR,CW)
for x in range(400):
    GPIO.output(STEP,GPIO.HIGH)
    sleep(.0100)
    GPIO.output(STEP,GPIO.LOW)
    sleep(.0100)
    myDistance = ReadDistance(US)
    print(myDistance)
    myAngle = x*0.9
    fillData(myAngle, myDistance)
            
            

def updateDisplay():
    global lineNumber, lineObjects, clockwise, anticlockwise, measurement
    angle = measurement[lineNumber][0]
    length = measurement[lineNumber][1]
    dx = length * math.sin(math.radians(angleOffset - angle))
    dy = length * math.cos(math.radians(angleOffset - angle))

    colour = '#%02x%02x%02x' % colourScale[0]
    lineObjects.append(
        canvas.create_line(canvasCenterX, canvasCenterY, dx + canvasCenterX, dy + canvasCenterY, width=lineWidth,
                           fill=colour))

    if clockwise:
        lineNumber += 1
    else:
        lineNumber -= 1

    
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