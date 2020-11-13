int Led = 13 ;// define LED Interface
int sensor = 3; // define the tilt switch sensor interfaces
int val ;// define numeric variables val
void setup ()
{
pinMode (Led, OUTPUT) ;// define LED as output interface
pinMode (sensor, INPUT) ;//define the output interface tilt switch sensor
}
void loop ()
{
val = digitalRead (sensor) ;// digital interface will be assigned a value of 3 to read val
if (val == HIGH) //When the tilt sensor detects a signal when the switch, LED flashes
{
digitalWrite (Led, HIGH);
}
else
{
 
digitalWrite (Led, LOW);
}
}

