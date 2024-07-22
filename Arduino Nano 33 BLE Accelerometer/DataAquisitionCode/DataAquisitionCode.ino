#include <Arduino_LSM9DS1.h>
//Defining LEDs Pins
#define LED1 6
#define LED2 7
#define LED3 8
#define LED4 9
void setup() {
  //Begining Serial Communication for Data display
  Serial.begin(9600);
  Serial.println("Started");

  if (!IMU.begin()) {
    Serial.println("The IMU failed to Initialize.");
    while (1);
  }
  //Declaring the LEDs Pins and Outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
}

void loop() {
  //Variables to store the Acceleration values in different directions
  float x, y, z;
  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(x, y, z);
    //Printing the acceleration values
    Serial.print(x);
    Serial.print('\t');
    Serial.print(y);
    Serial.print('\t');
    Serial.println(z);
    //Condition for a person at 90 degrees
    if((x>0.98 && x<1.01)&&(y>0.2 && y<0.5)&&(z<-2 && z>-5)){
      //Turning ON the LEDs when the person is at 90 degrees
      digitalWrite(LED1, HIGH);
      digitalWrite(LED2, HIGH);
      digitalWrite(LED3, HIGH);
      digitalWrite(LED4, HIGH);
    }
    else{
      //Turning off the LEDs if the person is not at 90 degrees
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, LOW);
      digitalWrite(LED3, LOW);
      digitalWrite(LED4, LOW);      
    }
  }
}
