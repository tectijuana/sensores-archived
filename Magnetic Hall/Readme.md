![](LMAGNETICHALL.png)

PIC | SENSOR | FUNCIÓN | URL | COLABORADOR
------------ | -------------| -------------| -------------| -------------
![](LMHSENSOR.jpg) | Linear Magnetic Hall Sensor | Detecta campo magenetico | [MAS INFO](https://arduinomodules.info/ky-024-linear-magnetic-hall-module/) | Erik Geovanny Osorio Lopez

# DESCRIPTION 
The magnetic sensor known as KY 0 24. This is a module itself so let's get started.
This module is integrated on board one magnetic hold sensor, one
potentiometer one microchip, six resistors and two LED is the
resistor r1. Using this module, it's Thank you arms, the resistor R
two, it's 100 kilo ohms. The resistor R three is 150 ohms. Their
resistor R four, it's won KY on the resistor R five, it's won KY on
and the resistor R six is 100 kilo ohm. And the main reason for using
the resistor is to limit current circulating inside the module. In other
words to press Current from burning our module the LED l one
lights up to show if the module it's working or not ever led l two
lights up only one the sensor has detected the magnetic field. Now I
will show how these components are connected together. There we
have the sensor itself and of course, the six is Easter's and the two
LVDS override. You can see how the piece of the module icon nated
on this board, we have in black, the flow of the ground, we have in
the red, the flow of the voltage, we have in a light green, the flow of
the analogue signal and of course we have in green, the flow of the
digital signal. This sensor It is used to the tag the magnetic field It
can react in the presence of the magnetic field. It has a potentiometer
to adjust the sensitivity of the sensor, and it provides both analogue 
and digital outputs.


The digital output acts as a switch that will turn on or off when
the magnet is near. On the other hand, the analogue output can measure
the polarity and the relative strength of the magnetic field. 
When a magnetic field is detected by the sensor, the LED l two will light up.
Let's talk about the pins. The pins in this module are four.
We have the ground pin with G sign. We have the voltage pin with the plus sign.
We have the analogue pin with A 0 sine. And of course we have the
digital pin with the 0 sign. So let's talk about the signal. This module
gives two signals, we can connect the pin of the analogue signal with
any analogue board and the pain of the digital signal with any digital
port of different microcontroller boards like Arduino or Raspberry
Pi.

# EXAMPLE SENSOR CODE:
```Arduino Uno

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
