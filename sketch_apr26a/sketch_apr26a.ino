
#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 90;    // variable to store the servo position
int resetPos= 100;
int maxPos = 150;
int minPos=50;

int redLightPin = 3;
int greenLightPin = 2;

void resetServo(){
  servoLeftToValue(resetPos);
  servoRightToValue(resetPos);
}

void servoLeftToValue(int value){
  while(pos > value){
    myservo.write(pos--);              // tell servo to go to position in variable 'pos'
    delay(15);    
  }
}

void servoRightToValue(int value){
  while(pos < value){
    myservo.write(pos++);              // tell servo to go to position in variable 'pos'
    delay(15);    
  }
}

void setup() {
  // initialize serial:
  Serial.begin(9600);
  // make the pins outputs:
  pinMode(1, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
//  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  
  myservo.attach(4);  // attaches the servo on pin 9 to the servo object
  myservo.write(resetPos); // initial pos


  // Send an 'r' to let the controller app know we're ready to respond to commands
  Serial.print('r');
}


void resetLeds(){
  
  digitalWrite(0, LOW);
  digitalWrite(1, LOW);
  digitalWrite(2, LOW);
  digitalWrite(3, LOW);
  //digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  
}

void loop() {
  // if there's any serial available, read it:
  while (Serial.available() > 0) {
    resetLeds();
    int input = Serial.parseInt();

    if(input==9){
      digitalWrite(greenLightPin, HIGH);
      servoLeftToValue(minPos);
      delay(4000);
      resetServo();
      digitalWrite(greenLightPin, LOW);
    }
    
    if(input==8){
      digitalWrite(greenLightPin, HIGH);
      servoRightToValue(maxPos);
      delay(4000);
      resetServo();
      digitalWrite(greenLightPin, LOW);
    }
     
    if(input==0){
      digitalWrite(redLightPin, HIGH);
      resetServo();
      delay(2000);
      digitalWrite(redLightPin, LOW);
    }
   
  }

}
