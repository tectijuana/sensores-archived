/******************************************
 *Website: www.elegoo.com
 * 
 *Time:2017.12.12
 *
 ******************************************/
int relayPin = 3;
 
void setup() 
{ 
  pinMode(relayPin, OUTPUT);
} 
 
 
void loop() 
{ 
   digitalWrite(relayPin, HIGH);    // turn the relay on (HIGH is the voltage level)
  delay(2000);                     // wait for a second
  digitalWrite(relayPin, LOW);    // turn the relay off by making the voltage LOW
  delay(2000);                   // wait for a second
} 
