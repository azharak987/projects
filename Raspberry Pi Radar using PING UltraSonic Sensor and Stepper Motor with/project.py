import RPi.GPIO as GPIO
from time import sleep
import time
DIR = 20
STEP = 21
CW =1
CCW =0
US = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR,CW)
GPIO.setwarnings(False)

def ReadDistance(pin):
   GPIO.setup(pin, GPIO.OUT)
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

def writeToFile(angle, radius, direction):
    file = open("/home/pi/Desktop/data.csv", 'a')
    print("File Created")
    file.write(angle+','+radius+','+direction)
    file.close()
while(1):
        print("In While")
        sleep(1)
        GPIO.output(DIR,CW)
        for x in range(400):
            print("In First For")
            GPIO.output(STEP,GPIO.HIGH)
            sleep(.0100)
            GPIO.output(STEP,GPIO.LOW)
            sleep(.0100)
            myDistance = ReadDistance(US)
            myAngle = x*0.9
            print("Going to write to file")
            writeToFile(myAngle, myDistance, 1)
        sleep(1)
        GPIO.output(DIR,CCW)
        for x in range(400):
            GPIO.output(STEP,GPIO.HIGH)
            sleep(.0010)
            GPIO.output(STEP,GPIO.LOW)
            sleep(.0010)
            myDistance = ReadDistance(US)
            myAngle = x*0.9
            writeToFile(myAngle, myDistance, 0)
            