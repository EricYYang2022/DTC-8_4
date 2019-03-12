/*
DTC Winter Quarter 2019
Section 8, Team 4
Arduino Code
March 2019
*/

#include <Keyboard.h>

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Keyboard.begin();
}


//predeclare calibration values(?)
static int cal_val_0 = 0;
static int cal_val_1 = 0;
static int cal_val_2 = 0;
static int cal_val_3 = 0;
static int equilibriumVal = 100;

bool isOnBoard = 0;
bool wasOnBoard = 0;
// the loop routine runs over and over again forever:

bool omegalul = 1;
void loop() {
  // read the input on analog pin 0:
  int sensorValue0 = analogRead(A1); //This will be top left
  int sensorValue1 = analogRead(A2); //This will be bot left
  int sensorValue2 = analogRead(A3); //This will be top right
  int sensorValue3 = analogRead(A4); //This will be bot right

  Serial.print(sensorValue0);
  Serial.print(" ");
  Serial.print(sensorValue1);
  Serial.print(" ");
  Serial.print(sensorValue2);
  Serial.print(" ");
  Serial.println(sensorValue3);

  //calibration
  int post_cal0 = sensorValue0 - cal_val_0;
  int post_cal1 = sensorValue0 - cal_val_1;
  int post_cal2 = sensorValue0 - cal_val_2;
  int post_cal3 = sensorValue0 - cal_val_3;
  
  //insert checking conditions for if user is on the board
  //isOnBoard = bool
  
  if (isOnBoard == 1) {
    omegalul = 0;
    if (abs(post_cal0 + post_cal1 - post_cal2 - post_cal3) <= equilibriumVal) {
      Keyboard.press('n');
      delay(50);
      Keyboard.release('n');
  }
    else {
      Keyboard.press('m');
      delay(50);
      Keyboard.release('m');
    }
  
  }

  //Checking board conditionals
  if (isOnBoard == wasOnBoard) {
     delay(990);
  }
  if ((isOnBoard == 0) && (wasOnBoard == 1)) {
     Keyboard.press('d');
     Serial.print("I pressed d, btw");
     delay(50);
     Keyboard.release('d');
     delay(950);
  }
  if ((isOnBoard == 1) && (wasOnBoard == 0)) {
     Keyboard.press('a');
     Serial.print("I pressed a, btw");
     delay(50);
     Keyboard.release('a');
     delay(900);
  }
if (omegalul == 1) {
    delay(250);
}
  //post-check resetting conditionals
  wasOnBoard = isOnBoard;
}
//Keyboard.end();
