#define sensor1 A0
#define sensor2 A1
#define sensor3 A2
#define output 4
#define threshold 970
int intervalDelay = 10000;
unsigned long timeNow = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(sensor1, INPUT);
  pinMode(sensor2, INPUT);
  pinMode(sensor3, INPUT);
  pinMode(output, OUTPUT);
  digitalWrite(output, LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorVal1 = analogRead(sensor1);    
  int sensorVal2 = analogRead(sensor2);  
  int sensorVal3 = analogRead(sensor3);  
  if(sensorVal1 < threshold || sensorVal2 < threshold || sensorVal3 < threshold){
    digitalWrite(output, HIGH);
    timeNow = millis();
    while(millis()<timeNow + intervalDelay){
      sensorVal1 = analogRead(sensor1);
      sensorVal2 = analogRead(sensor2);
      sensorVal3 = analogRead(sensor3);
          if(sensorVal1 < threshold || sensorVal2 < threshold || sensorVal3 < threshold){
            timeNow = millis();
      }
    }
  }
  
  else{
    digitalWrite(output, LOW);
  }
}
