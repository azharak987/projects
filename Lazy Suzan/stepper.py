from time import sleep
import RPi.GPIO as GPIO

DIR = 20        #Direction GPIO Pin
STEP = 21       #Step GPIO Pin
CW = 1          #Clockwise Rotation
CCW = 0         #Counterclockwise Rotation
SPR = 200        #Steps per Revolution

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

MODE = (14, 15, 18)
GPIO.setup(MODE, GPIO.OUT)
RESOLUTION = { 'Full': (0, 0, 0),
               'Half': (1, 0, 0),
               '1/4' : (0, 1, 0),
               '1/8' : (1, 1, 0),
               '1/16': (1, 1, 1),
}

GPIO.output(MODE, RESOLUTION['1/4'])
step_count = SPR
delay = 0.0208

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(0.5)
GPIO.output(DIR, CCW)

for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)
