void setup() {
  Serial.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() {
 Serial.println(Serial.available());
 if(Serial.available()>0){
  Serial.println("Serial Available");
  Serial.println(Serial.read());
 }
}
