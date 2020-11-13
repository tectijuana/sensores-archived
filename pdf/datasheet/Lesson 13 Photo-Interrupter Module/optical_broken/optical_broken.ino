int Led=13;
int sensor=3; 
int val;
void setup()
{
pinMode(Led,OUTPUT);
pinMode(sensor,INPUT);
}
void loop()
{
val=digitalRead(sensor); 
if(val==HIGH)
{
digitalWrite(Led,HIGH);
}
else
{
digitalWrite(Led,LOW);
}
 
}

