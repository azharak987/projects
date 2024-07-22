#include <SoftwareSerial.h>
#include "TFMini.h"
 
// Setup software serial port 
SoftwareSerial mySerial (12, 13);      // Uno RX (TFMINI TX), Uno TX (TFMINI RX)
TFMini Tfmini;
 
void setup(){
  // Step 1: Initialize hardware serial port (serial debug port)
  Serial.begin (115200);
  // wait for serial port to connect. Needed for native USB port only
  while(Serial);
     
  Serial.println("Initializing...");
 
  // Step 2: Initialize the data rate for the Software Serial port
  mySerial.begin (TFMINI_BAUDRATE);
 
  // Step 3: Initialize the TF Mini sensor
  Tfmini.begin(&mySerial);    
}
 
 
 void loop () {
  // Take one TF Mini distance measurement
  uint16_t distance = Tfmini.getDistance ();
  // Display the measurement
  Serial.print(distance);
  Serial.println (" cm");
 
  // Wait some short time before taking the next measurement
  delay(25);  
}
