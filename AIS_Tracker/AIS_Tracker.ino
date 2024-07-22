#include <Arduino.h>
#include <AIS.h>
#include <TinyGPS++.h>
#include <SoftwareSerial.h>
#include <IridiumSBD.h>
#define AIS_baudrate 115200
#define IridiumSerial_baudrate 115200
#define GPSBaudRate 9600
#define htonl(x) ( ((x)<<24 & 0xFF000000UL) | \
                   ((x)<< 8 & 0x00FF0000UL) | \
                   ((x)>> 8 & 0x0000FF00UL) | \
                   ((x)>>24 & 0x000000FFUL) )
#define htons(x) ( ((x)<<8) | (((x)>>8)&0xFF) )
#define IridiumSerial Serial1
#define DIAGNOSTICS false
IridiumSBD modem(IridiumSerial);
int RXPin_GPS = 3;
int TXPin_GPS = 4;
String latitude, longitude, altitudeInfo;
String GPS_data = "";
int err;
// Create a TinyGPS++ object
TinyGPSPlus gps;
SoftwareSerial gpsSerial(RXPin_GPS, TXPin_GPS);
void setup() {
  Serial.begin(115200);
  gpsSerial.begin(GPSBaudRate);
  IridiumSerial.begin(19200);
  err = modem.begin();
  if (err != ISBD_SUCCESS)
  {
     //Serial.print("Begin failed: error ");
    if (err == ISBD_NO_MODEM_DETECTED)
      //Serial.println("No modem detected: check wiring.");
    return;
  }
}


void loop() {
  String toDecode = "";
  while(Serial.available()){
    String myText = Serial.readString();
    myText.trim();
    toDecode =  myText.substring(14, 48);
  }
  const AIS &myAIS = AIS((toDecode.c_str()));
  AIS ais_msg(myAIS);
  unsigned long mmsi = showMMSI(ais_msg);
  int timeNow = millis();
 
  while(millis() < timeNow + 60000){
    while (gpsSerial.available() > 0)
      if (gps.encode(gpsSerial.read()))
        displayGPSInfo();
      if (millis() > 5000 && gps.charsProcessed() < 10)
      {
          //"No GPS detected"
       while(true);
      }
}
 //Data = Latitude,longitude,altitude
 GPS_data= latitude + "," + longitude+ "," + altitudeInfo;
 const char * message  = GPS_data.c_str();
 err = modem.sendSBDText(message);
 
  if (err == ISBD_SUCCESS)
  {
    //Sending Success
  }
  else{
    //Sending Unsuccessful
  }
  message  = String(mmsi).c_str();
  err = modem.sendSBDText(message);
  if (err == ISBD_SUCCESS)
  {
    //Sending Success
  }
  else{
    //Sending Unsuccessful
  }
}
unsigned long showMMSI(AIS& ais_msg) {
  unsigned long mmsi = ais_msg.get_mmsi();
  return mmsi;
}
void displayGPSInfo()
{
  if (gps.location.isValid())
  {
    latitude = String(gps.location.lat(),6);

    longitude = String(gps.location.lng(),6);
    
    altitudeInfo = String(gps.altitude.feet()) + " Feet";
  }
  else
  {
    latitude = "No Loc";
    longitude = "No Loc";
  }

}
