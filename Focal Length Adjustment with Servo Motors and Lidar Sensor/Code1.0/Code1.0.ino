#include <Stepper.h>
#include <SoftwareSerial.h>
#include "TFMini.h"
#define STEPS_NEMA 200
#define stepsPerRev_BYJ48 2048
#define pushButton A0
#define motorInterfaceType 1
#define switchInput A5
SoftwareSerial mySerial (12, 13); // Uno RX (TFMINI TX), Uno TX (TFMINI RX)
TFMini Tfmini;  
// Define stepper motor connections and motor interface type. Motor interface type must be set to 1 when using a driver
Stepper stepper_NEMA(STEPS_NEMA, 2, 3); // Pin 2 connected to DIRECTION & Pin 3 connected to STEP Pin of Driver
// Pins entered in sequence IN1-IN3-IN2-IN4 for proper step sequence
Stepper stepper_BYJ48_left(stepsPerRev_BYJ48, 4, 6, 5, 7);
Stepper stepper_BYJ48_right(stepsPerRev_BYJ48, 8, 10, 9, 11);
boolean buttonState = LOW; 
int pressed=0;
int threshold = 50;
int BYJ48_range = 10;
void setup() {
  Serial.begin(9600);
  mySerial.begin(TFMINI_BAUDRATE);
  Tfmini.begin(&mySerial);
  stepper_NEMA.setSpeed(1000);
  stepper_BYJ48_left.setSpeed(12);
  stepper_BYJ48_left.setSpeed(12);
  pinMode(pushButton, INPUT);
  pinMode(switchInput, INPUT);
}
void loop() {
  int buttonState = digitalRead(pushButton);
  if(debounceButton(buttonState) == HIGH && buttonState == LOW)
  {
    pressed++;
    buttonState = HIGH;
  }
  else if(debounceButton(buttonState) == LOW && buttonState == HIGH)
  {
       buttonState = LOW;
  }
   if(pressed == 10)
  {
    while(1){
    int switchValue = digitalRead(switchInput);
    int distance = Tfmini.getDistance();
    //For NEMA 17
    if(distance < threshold-BYJ48_range){
      //Step in one direction
      //direction can be changed by 
      //stepper.NEMA.step(-10);
      //To increase the step size increase the number like
      //stepper.NEMA(100);
      stepper_NEMA.step(10);
      Serial.println("Increasing the Distance");
    }
    if(distance > threshold+BYJ48_range){
      //Step in one direction
      //direction can be changed by 
      //stepper.NEMA.step(10);
      //To increase the step size increase the number like
      //stepper.NEMA(-100);
      stepper_NEMA.step(-10);
      Serial.println("Decreasing the Distance");
    }
    if(distance == threshold){
      Serial.println("Threshold Reached");
    }
    //For BYJ48
    if(distance > threshold-BYJ48_range && distance < threshold){
      //Direction can be changed by changing the sign of 10
      //Step size can be changed by increasing the value, that is 10.
      Serial.println("Increasing the distance by BYJ48");
      stepper_BYJ48_left.step(-10);
      stepper_BYJ48_right.step(10);
    }
    if(distance < threshold+BYJ48_range && distance > threshold){
      //Direction can be changed by changing the sign of 10
      //Step size can be changed by increasing the value, that is 10.
      Serial.println("Decreasing the distance by BYJ48");
      stepper_BYJ48_left.step(10);
      stepper_BYJ48_right.step(-10);
    }
  }
  }
}

boolean debounceButton(boolean state)
{
  boolean stateNow = digitalRead(pushButton);
  if(state!=stateNow)
  {
    delay(10);
    stateNow = digitalRead(pushButton);
  }
  return stateNow;
}
