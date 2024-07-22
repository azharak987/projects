#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#include <SD.h>
#include <Stepper.h>
#define chipSelect 10
String value1 = "";
char temp = ' ';
File myFile;
// Choose two Arduino pins to use for software serial
#define RXPin 2
#define TXPin 3
#define buttonInput 4
#define stepsPerRevolution = 200;
#define GPSBaud 9600
Stepper myStepper(stepsPerRevolution, 5, 6, 7, 8);

// Create a TinyGPS++ object
TinyGPSPlus gps;

// Create a software serial port called "gpsSerial"
SoftwareSerial gpsSerial(RXPin, TXPin);

void moveStepper();
String  myLocation = "";
void setup()
{
  // Start the Arduino hardware serial port at 9600 baud
  Serial.begin(9600);
  myStepper.setSpeed(60);
  // Start the software serial port at the GPS's default baud
  gpsSerial.begin(GPSBaud);
  while (!Serial);

  Serial.print("Initializing SD card...");

  if (!SD.begin(chipSelect)) {
    Serial.println("initialization failed. Things to check:");
    Serial.println("1. is a card inserted?");
    Serial.println("2. is your wiring correct?");
    Serial.println("3. did you change the chipSelect pin to match your shield or module?");
    Serial.println("Note: press reset or reopen this Serial Monitor after fixing your issue!");
    //while (true);
  }

  Serial.println("initialization done.");
  //Open the file for reading:
  pinMode(buttonInput, INPUT_PULLUP);
   
}


void loop()
{
  // This sketch displays information every time a new sentence is correctly encoded.
  while (gpsSerial.available() > 0)
    if (gps.encode(gpsSerial.read()))
      displayInfo();

  // If 5000 milliseconds pass and there are no characters coming in
  // over the software serial port, show a "No GPS detected" error
  if (millis() > 5000 && gps.charsProcessed() < 10)
  {
    Serial.println("No GPS detected");
    while(true);
  }
}

void displayInfo()
{
  if (gps.location.isValid())
  {
    myLocation = String(gps.location.lat(),4)+","+String(gps.location.lng(),4);
    myFile = SD.open("myFile.csv");

    if (myFile) {
    // read from the file until there's nothing else in it:
    while (myFile.available()) {
      //temp = myFile.read();
      value1= myFile.readStringUntil('\n');
      //Serial.println(value1);
      value1 = value1.substring(0, value1.length() - 1);
      if(value1 == myLocation){
        Serial.println("True");
      }
    }
    
    // close the file:
    myFile.close();
    Serial.println(myLocation);
    delay(1000);
    }
    else {
      // if the file didn't open, print an error:
      Serial.println("error opening test.txt");
    }
  }
  else
  {
    Serial.println("Location: Not Available");
  }

}

void moveStepper(){
  myStepper.step(-stepsPerRevolution);
}
