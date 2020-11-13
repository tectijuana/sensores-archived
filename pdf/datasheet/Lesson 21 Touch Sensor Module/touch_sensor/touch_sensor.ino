int Led = 13;// define LED Interface
int Sensor = 3;
int val;// define numeric variables val
void setup ()
{
pinMode (Led, OUTPUT) ;//define LED as output interface
pinMode (Sensor, INPUT) ;// define metal touch sensor output interface
}
 
void loop ()
{
val = digitalRead (Sensor) ;//digital interface will be assigned a value of 3 to read val
if (val == HIGH) //When the metal touch sensor detects a signal, LED flashes
{
digitalWrite (Led, HIGH);
}
else
{
digitalWrite (Led, LOW);
}
}

