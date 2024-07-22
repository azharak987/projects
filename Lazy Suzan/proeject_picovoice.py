from picovoice import Picovoice
from Mic import MicArray
myMic = MicArray()
prePosition = 1
quaterSteps = 50
class StepperHandler():
    __CLOCKWISE = 1
    __ANTI_CLOCKWISE = 0

def __init__(self, stepPin, directionPin, delay=0.208, stepsPerRevolution=200):

    # Configure instance
    self.CLOCKWISE = self.__CLOCKWISE
    self.ANTI_CLOCKWISE = self.__ANTI_CLOCKWISE
    self.StepPin = stepPin
    self.DirectionPin = directionPin
    self.Delay = delay
    self.RevolutionSteps = stepsPerRevolution
    self.CurrentDirection = self.CLOCKWISE
    self.CurrentStep = 0

    # Setup gpio pins
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(self.StepPin, GPIO.OUT)
    GPIO.setup(self.DirectionPin, GPIO.OUT)

def Step(self, stepsToTake, direction):
    print("Step Pin: " + str(self.StepPin) + " Direction Pin: " + str(self.DirectionPin) + " Delay: " + str(self.Delay))
    print("Taking " + str(stepsToTake) + " steps.")

    # Set the direction
    GPIO.output(self.DirectionPin, direction)

    # Take requested number of steps
    for x in range(stepsToTake):
    print("Step " + str(x))
    GPIO.output(self.StepPin, GPIO.HIGH)
    self.CurrentStep += 1
    sleep(self.Delay)
    GPIO.output(self.StepPin, GPIO.LOW)
    sleep(self.Delay)

# Define pins
STEP_PIN = 21
DIRECTION_PIN = 20

# Create a new instance of our stepper class (note if you're just starting out with this you're probably better off using a delay of ~0.1)
stepperHandler = StepperHandler(STEP_PIN, DIRECTION_PIN, 0.0025)
def rotate(dir):
        print("Rotate function called")
        error = dir - prePosition
        steps = quaterSteps
        if error < 0:
            if error == -1:
                stepsTT = 3*steps
                stepperHandler.step(stepTT, stepperHandler.ANTI_CLOCKWISE)
            if error == -2:
                stepsTT = 2*steps
                stepperHandler.step(stepTT, stepperHandler.ANTI_CLOCKWISE)
            if error == -3:
                stepsTT = steps
                stepperHandler.step(stepTT, stepperHandler.ANTI_CLOCKWISE)
        if error > 0:
            stepsTT = steps*error
            stepperHandler.step(stepTT, stepperHandler.ANTI_CLOCKWISE)
        if error == 0:
            pass
def wake_word_callback():
    print("Wake Word Detected")
    direction = myMic.getDirection()
    rotate(direction)
def inference_callback(inference):
   if inference.is_understood:
      intent = inference.intent
      slots = inference.slots
   else:
      pass
handle = Picovoice(
     access_key="2zkzS9Wziwz68hAeN07j5zmxTpS17U6pBedgow5wB98n2dAeL03aJQ==",
     keyword_path="/home/pi/Desktop/PICO Voice files/Wake words/hey-lazy-suzan.ppn",
     wake_word_callback=wake_word_callback,
     context_path="/home/pi/Desktop/PICO Voice files/Speech to intent (Rhino)/lazy-2_en_raspberry-pi_v2_1_0.rhn",
     inference_callback=inference_callback)
