#include "nRF24L01.h" // NRF24L01 library created by TMRh20 https://github.com/TMRh20/RF24
#include "RF24.h"
#include "SPI.h"

#define switch1 3
#define output1 2

int ReceivedMessage[1] = {000}; // Used to store value received by the NRF24L01
RF24 radio(9,10); // NRF24L01 SPI pins. Pin 9 and 10 on the Nano

const uint64_t pipe = 0xE6E6E6E6E6E6; // Needs to be the same for communicating between 2 NRF24L01 

void setup(void)
{
  radio.begin(); // Start the NRF24L01
  
  radio.openReadingPipe(1,pipe); // Get NRF24L01 ready to receive
  
  radio.startListening(); // Listen to see if information received
  
  pinMode(output1, OUTPUT); 
  pinMode(switch1, INPUT_PULLUP);
  digitalWrite(switch1, HIGH);
}

void loop(void)
{
  while (radio.available())
  {
    radio.read(ReceivedMessage, 1); // Read information from the NRF24L01

    if (ReceivedMessage[0] == 111 || digitalRead(switch1) == LOW) // Indicates switch is pressed
    {
      digitalWrite(output1, HIGH);
    }
    else
    {
       digitalWrite(output1, LOW);
    }
    delay(2);
   }
  if(digitalRead(switch1) == LOW){
    digitalWrite(output1, HIGH);
  }
  else{
    digitalWrite(output1, LOW);
  }
}
