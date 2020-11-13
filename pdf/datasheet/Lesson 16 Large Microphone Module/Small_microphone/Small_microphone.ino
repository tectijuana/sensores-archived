/*****************************/
int Led=13;
int ledPin=12; 
int buttonpin=7;
int sensorPin = A0; 
int sensorValue = 0; 
int val;
void setup()
{
Serial.begin(9600);
pinMode(Led,OUTPUT); 
pinMode(ledPin, OUTPUT); 
pinMode(buttonpin,INPUT);
}
void loop()
{
sensorValue = analogRead(sensorPin); 
digitalWrite(ledPin, HIGH);
delay(sensorValue);
digitalWrite(ledPin, LOW);
delay(sensorValue); 
Serial.println(sensorValue, DEC); 
val=digitalRead(buttonpin);
if(val==HIGH)
{
digitalWrite(Led,HIGH);
}
else
{
digitalWrite(Led,LOW);
}
}

