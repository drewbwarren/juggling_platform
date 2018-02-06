#include <Servo.h>

Servo myservo;

void setup() {
  // put your setup code here, to run once:

  myservo.attach(9);
  myservo.writeMicroseconds(1500);
  
}

void loop() {
  // put your main code here, to run repeatedly:


  delay(1000);
  myservo.writeMicroseconds(650);
  delay(1000);
  myservo.writeMicroseconds(1500);
  delay(1000);
  myservo.writeMicroseconds(2300);
  delay(1000);
  myservo.writeMicroseconds(1500);


//  delay(1000);
//  myservo.write(10);
//  delay(1000);
//  myservo.write(90);
//  delay(1000);
//  myservo.write(180);
//  delay(1000);
//  myservo.write(90);
  
}

