#include <Wire.h>
#include <LiquidCrystal_I2C.h>//Import I2C library

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int Led_Array[20]     =   {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 22, 23};
const int Button_Array[20]  =   {24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43};
const int Start_Stop = 44;
const int signalPin = 45;
unsigned int Time = 15000; // this is the wait time for the target in ms ( 15000 ms = 15 sec )
unsigned long OffTime = 120000;  // this is the time the game will be on in this case 120,000 ms or 120 sec
unsigned int Score = 0;
unsigned long TIMER = 0;
bool flag = false;
void sendSignal(){
  digitalWrite(signalPin, HIGH);
  delay(100);
  digitalWrite(signalPin, LOW);
}
void setup() {
  Serial.begin(9600);
  // initialize the LCD
  lcd.init();// initialize the lcd
  lcd.begin(16, 2);
  // Turn on the blacklight and print a message.
  lcd.backlight();
  lcd.print("AirSoft Range");
  Serial.println("AirSoft Range");
  pinMode(Start_Stop,INPUT);
  for (int i = 0; i < 20; i++) {
    pinMode(Led_Array[i], OUTPUT);
  }
  for (int i = 0; i < 20; i++) {
    pinMode(Button_Array[i], INPUT);
  }
  pinMode(signalPin, OUTPUT);
  Serial.print("Score : ");
  Serial.println(Score);
  Serial.println(" ");
  lcd.setCursor(0, 1);
  lcd.print("Score : ");
  lcd.print(Score);
}

void loop() {
  if (digitalRead(Start_Stop) == HIGH) {
    while(digitalRead(Start_Stop) == HIGH){}
    flag = true;
    TIMER = millis();
  }
  if((TIMER - millis()) > OffTime){
    flag = false;
  }
  
  if (flag) {
    int num = random(0, 20);
    digitalWrite(Led_Array[num], HIGH);
    unsigned long Now = millis();
    while ((millis() - Now) < Time) {
      if (digitalRead(Button_Array[num]) == HIGH) {
        Score++;
        sendSignal();
        break;
      }
      if (digitalRead(Start_Stop) == HIGH) {
        while(digitalRead(Start_Stop) == HIGH){}
        flag = !flag;
        Score = 0;
        break;
      }
    }
    digitalWrite(Led_Array[num], LOW);
    lcd.setCursor(0, 1);
    lcd.print("Score : ");
    lcd.print(Score);
    Serial.print("Score : ");
    Serial.println(Score);
    Serial.println(" ");
  }
}
