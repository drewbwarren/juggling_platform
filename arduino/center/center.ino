#include <Servo.h>

//Servo myservo;

Servo servo[6];
const int servo_pin[] = {9,3, 5, 11, 6, 10}, servo_zero[6] = {1710, 1280, 1700, 1300, 1680, 1300};

void setup() {
  // put your setup code here, to run once:

//  myservo.attach(9);
//  myservo.writeMicroseconds(1500);

  for(int i = 0; i < 6; i++)
  {
    servo[i].attach(servo_pin[i]);
//    servo[i].writeMicroseconds(servo_zero[i]);
  }
  delay(1000);
  
}

void set_pos(int ms)
{
  for(int i = 0; i < 6; i++)
  {
    servo[i].writeMicroseconds(ms);
  }
}

void loop() {
  // put your main code here, to run repeatedly:

  
  delay(1000);
//  set_pos(650);
  delay(1000);
  set_pos(1500);
  delay(1000);
//  set_pos(2300);
  delay(1000);
  set_pos(1500);

//  delay(1000);
//  myservo.write(10);
//  delay(1000);
//  myservo.write(90);
//  delay(1000);
//  myservo.write(180);
//  delay(1000);
//  myservo.write(90);
  
}

