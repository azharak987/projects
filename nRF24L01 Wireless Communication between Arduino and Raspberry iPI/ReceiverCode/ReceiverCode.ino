#include<SPI.h>
#include<RF24.h>

RF24 radio(9,10); // ce, csn

void setup(){
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x76);
  radio.openWritingPipe(0xC2C2C2C2C2);
  radio.enableDynamicPayloads();
  radio.powerUp();
}

void loop(){
  const char text[] = "Hello World";
  radio.write(&text, sizeof(text));
  delay(1000);
}
