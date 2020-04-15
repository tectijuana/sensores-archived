/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
const int pirPin = 3; 
const int LED =2;
void setup()
{
 Serial.begin(9600); 
 pinMode(pirPin, INPUT);
 pinMode(LED,OUTPUT);
}
void loop()
{
  int pirVal = digitalRead(pirPin);
  if(pirVal == LOW)
  { //was motion detected
    Serial.println("Motion Detected"); 
    digitalWrite(LED,HIGH);
  } else
  {
    digitalWrite(LED,LOW);
  }
    delay(1000); 
}
