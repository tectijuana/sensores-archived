#Magnetic Hall Sensor

| Pic 	| Sensor 	| Función 	| URL 	| Colaborador 	|
|-	|-	|-	|-	|-	|
|  	| 	|  	|  	|  	|
|  	|  	|  	|  	|  	|
|  	|  	|  	|  	|  	|
|  	|  	|  	|  	|  	|
|  	|  	|  	|  	|  	|
|  	|  	|  	|  	|  	|

```
EXAMPLE SENSOR CODE:
int led = 13; //Define the LED pin
int buttonpin = 3; //Define the push button pin
int val; //Define a numeric variable
void setup()
{

pinMode(led,OUTPUT);
pinMode(buttonpin,INPUT);

}
void loop()
{

val = digitalRead(buttonpin); // check the state

of the button

if(val==HIGH) // if button is pressed, turn LED

on

{
digitalWrite(led,HIGH);
}
else
{
digitalWrite(led,LOW);

```
