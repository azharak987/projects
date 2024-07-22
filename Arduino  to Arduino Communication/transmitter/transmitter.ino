/*
 * How to configure and pair two HC-05 Bluetooth Modules
 * by Dejan Nedelkovski, www.HowToMechatronics.com
 * 
 *                 == MASTER CODE ==
 */

#define ledPin 13

int state = 0;
int potValue = 0;

void setup() {
  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);
  Serial.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() {
 // Reading the potentiometer
 potValue = 125;
 int potValueMapped = 102;
 Serial.write(potValueMapped); // Sends potValue to servo motor
 delay(100);
}
