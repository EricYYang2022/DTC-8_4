/*
  DTC Winter Quarter 2019
  Section 8, Team 4
  Arduino Code
  March 2019
*/

#include <Keyboard.h>
#include <HID.h>

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Keyboard.begin();
}


//predeclare calibration values(?)
static int cal_val_0 = 280;
static int cal_val_1 = 347;
static int cal_val_2 = 622;
static int cal_val_3 = 468;
static int equilibriumVal = 20; //Tentative value

bool isOnBoard = 0;
bool wasOnBoard = 0;
bool hasBeenOnBoard = 0;
// the loop routine runs over and over again forever:

bool readings = 1;

void loop() {
  // read the input on analog pin 0:
  int sensorValue0 = analogRead(A1); //This will be top right
  int sensorValue1 = analogRead(A2); //This will be bot right
  int sensorValue2 = analogRead(A3); //This will be top left
  int sensorValue3 = analogRead(A4); //This will be bot left


  Serial.print(sensorValue0);
  Serial.print(" ");
  Serial.print(sensorValue1);
  Serial.print(" ");
  Serial.print(sensorValue2);
  Serial.print(" ");
  Serial.println(sensorValue3);
  
  //calibration
  int post_cal0 = abs(sensorValue0 - cal_val_0);
  int post_cal1 = abs(sensorValue1 - cal_val_1);
  int post_cal2 = abs(sensorValue2 - cal_val_2);
  int post_cal3 = abs(sensorValue3 - cal_val_3);

  int summ = post_cal0 + post_cal1 + post_cal2 + post_cal3;

  int centered0 = cal_val_0 + summ/4;
  int centered1 = cal_val_1 + summ/4;
  int centered2 = cal_val_2 - summ/4;
  int centered3 = cal_val_3 - summ/4;
  Serial.print("Your sum is: ");
  Serial.println(summ);
  
  if (summ > 40) {
    isOnBoard = 1;
    Serial.println("You are on the board!");
  }
  else {
    isOnBoard = 0;
  }

  int diff0 = sensorValue0 - centered0;
  int diff1 = sensorValue1 - centered1;
  int diff2 = sensorValue2 - centered2;
  int diff3 = sensorValue3 - centered3;

  Serial.print(diff0);
  Serial.print(" ");
  Serial.print(diff1);
  Serial.print(" ");
  Serial.print(diff2);
  Serial.print(" ");
  Serial.println(diff3);
  Serial.print("Your diffsum is: ");
  Serial.println(abs(diff0 + diff1 + diff2 + diff3));
  Serial.println("--------------");
  
  //insert checking conditions for if user is on the board
  //isOnBoard = bool

  if (isOnBoard == 1) {
    readings = 0;
    if (abs(diff0 + diff1 + diff2 + diff3) <= equilibriumVal) {
      Serial.println("I pressed n, btw");
      Serial.print("Hasbeen: ");
      Serial.print(hasBeenOnBoard);
      Serial.print("WasOn: ");
      Serial.print(wasOnBoard);
      Serial.print("IsOn: ");
      Serial.println(isOnBoard);
      Keyboard.press('n');
      delay(50);
      Keyboard.release('n');
    }
    else {
      Serial.println("I pressed m, btw");
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
      Keyboard.press('s');
    Serial.print("I pressed s, btw");
    delay(50);
    Keyboard.release('s');
    delay(950);
  }
  if ((isOnBoard == 1) && (wasOnBoard == 0)) {
    if (hasBeenOnBoard == 0) {
      Keyboard.press('a');
      Serial.println("I pressed a, btw");
      hasBeenOnBoard = 1;
      delay(50);
      Keyboard.release('a');
      delay(900);
    }
    else if (hasBeenOnBoard == 1) {
      Keyboard.press('w');
      Serial.println("I pressed w, btw");
      delay(50);
      Keyboard.release('w');
      delay(900);
    }
  }
  
  if (readings == 1) {
    delay(250);
  }
  //post-check resetting conditionals
  wasOnBoard = isOnBoard;
}
//Keyboard.end();
