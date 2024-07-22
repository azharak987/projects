#include<SPI.h>                   // spi library for connecting nrf
#include<RF24.h>                  // nrf library
#define motor 4
RF24 radio(9, 10) ;  // ce, csn pins    
void setup(void) {
  pinMode(motor, OUTPUT);
  digitalWrite(motor, LOW);
  while (!Serial) ;
  Serial.begin(9600) ;     // start serial monitor baud rate
  Serial.println("Starting.. Setting Up.. Radio on..") ; // debug message
  radio.begin();        // start radio at ce csn pin 9 and 10
  radio.setPALevel(RF24_PA_MAX) ;   // set power level
  radio.setChannel(0x76) ;            // set chanel at 76
  const uint64_t pipe = 0xE0E0F1F1E0LL ;    // pipe address same as sender i.e. raspberry pi
  radio.openReadingPipe(1, pipe) ;        // start reading pipe 
  radio.enableDynamicPayloads() ;
  radio.powerUp() ;          
}

void loop(void) {

  radio.startListening() ;        // start listening forever
  char receivedMessage[2] = {0} ;   // set incmng message for 32 bytes
  if (radio.available()) {       // check if message is coming
    radio.read(receivedMessage, sizeof(receivedMessage));    // read the message and save
    Serial.println(receivedMessage) ;    // print message on serial monitor 
    radio.stopListening() ;   // stop listening radio
    if(receivedMessage == "ON"){
      digitalWrite(motor, HIGH);
      delay(500);
      digitalWrite(motor, LOW);
    }
   else{
    digitalWrite(motor, LOW);
   }
  }
  delay(10);
}
