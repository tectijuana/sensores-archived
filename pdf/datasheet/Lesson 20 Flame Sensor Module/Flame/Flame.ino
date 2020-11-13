int Led = 13 ;// define LED Interface
int buttonpin = 3; // define the flame sensor interface 
int analoog = A3; // define the flame sensor interface 
int val ;// define numeric variables val
float sensor; //read analoog value 
void setup ()
{
pinMode (Led, OUTPUT) ;// define LED as output interface
pinMode (buttonpin, INPUT) ;// output interface defines the flame sensor 
pinMode (analoog, INPUT) ;// output interface defines the flame sensor 
Serial.begin(9600);
}
void loop ()
{
sensor = analogRead(analoog);
Serial.println(sensor);  // display tempature
val = digitalRead (buttonpin) ;// digital interface will be assigned a value of 3 to read val
if (val == HIGH) // When the flame sensor detects a signal, LED flashes
{
 
digitalWrite (Led, HIGH);
}
else
{
digitalWrite (Led, LOW);
}
delay(1000);
}

