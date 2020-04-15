/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
#define ENABLE 3
#define DIRB 4
#define DIRA 5
int i;
void setup() 
{
  //---set pin direction
  pinMode(ENABLE,OUTPUT);
  pinMode(DIRA,OUTPUT);
  pinMode(DIRB,OUTPUT);
  Serial.begin(9600);
}

void loop() 
{
  //---back and forth example
  Serial.println("One way, then reverse");
  digitalWrite(ENABLE,HIGH); // enable on
  for (i=0;i<5;i++) {
    digitalWrite(DIRA,HIGH); //one way
    digitalWrite(DIRB,LOW);
    delay(500);
    digitalWrite(DIRA,LOW);  //reverse
    digitalWrite(DIRB,HIGH);
    delay(500);
  }
  digitalWrite(ENABLE,LOW); // disable
  delay(4000);

  Serial.println("fast Slow example");
  //---fast/slow stop example
  digitalWrite(ENABLE,HIGH); //enable on
  digitalWrite(DIRA,HIGH); //one way
  digitalWrite(DIRB,LOW);
  delay(1000);
  digitalWrite(ENABLE,LOW); //slow stop
  delay(3000);
  digitalWrite(ENABLE,HIGH); //enable on
  digitalWrite(DIRA,HIGH); //one way
  digitalWrite(DIRB,LOW);
  delay(1000);
  digitalWrite(DIRA,LOW); //fast stop
  delay(3000);

//Serial.println("PWM full then slow");
  //---PWM example, full speed then slow
  digitalWrite(ENABLE,HIGH); //enable on
  digitalWrite(DIRA,HIGH); //one way
  digitalWrite(DIRB,LOW);
  delay(2000);
  analogWrite(ENABLE,128); //half speed
  delay(2000);
  digitalWrite(ENABLE,LOW); //all done
  delay(10000);
}
