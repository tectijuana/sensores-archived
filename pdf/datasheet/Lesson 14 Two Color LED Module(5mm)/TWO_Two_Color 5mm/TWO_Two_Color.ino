
/********2018.5.29********************/
int redpin = 11;  // select the pin for the red LED 
int greenpin = 10;// select the pin for the greenLED
int val;
void setup () {
pinMode (redpin, OUTPUT); 
pinMode (greenpin, OUTPUT); 
Serial.begin (9600);
}
void loop ()
{
for (val = 255; val> 0; val --)
{
analogWrite (11, val);
 
analogWrite (10, 255-val);
delay (15);
}
for (val = 0; val <255; val ++)
{
analogWrite (11, val);
analogWrite (10, 255-val);
delay (15);
}
Serial.println (val, DEC);
}

