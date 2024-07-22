
#include <SD.h>
#include<String.h>
const int chipSelect = 10;
String value1 = "";
String value2 = "45.63455,45.54454";
char temp = ' ';
File myFile;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  // wait for Serial Monitor to connect. Needed for native USB port boards only:
  while (!Serial);

  Serial.print("Initializing SD card...");

  if (!SD.begin(chipSelect)) {
    Serial.println("initialization failed. Things to check:");
    Serial.println("1. is a card inserted?");
    Serial.println("2. is your wiring correct?");
    Serial.println("3. did you change the chipSelect pin to match your shield or module?");
    Serial.println("Note: press reset or reopen this Serial Monitor after fixing your issue!");
    while (true);
  }

  Serial.println("initialization done.");
  //Open the file for reading:
  myFile = SD.open("myFile.csv");
  bool flag = false;
  if (myFile) {
    Serial.println("myFile.csv:");

    // read from the file until there's nothing else in it:
    while (myFile.available()) {
      //temp = myFile.read();
      value1= myFile.readStringUntil('\n');
      Serial.println(value1);
      value1 = value1.substring(0, value1.length() - 1);
      if(value1 == value2){
        Serial.println("True");
      }
    }
    
    // close the file:
    myFile.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening test.txt");
  }
}

void loop() {
  // nothing happens after setup
}
