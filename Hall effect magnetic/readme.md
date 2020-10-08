<a href="https://cooltext.com"><img src="https://images.cooltext.com/5470136.gif" width="687" height="105" alt="Hall effect magnetic" /></a>
<a href="http://cooltext.com" target="_top"><img src="https://cooltext.com/images/ct_pixel.gif" width="80" height="15" alt="Cool Text: Logo and Graphics Generator" border="0" /></a>


PIC | SENSOR | FUNCIÓN | URL | COLABORADOR
------------ | -------------| -------------| -------------| -------------
![Hall effect magnetic](https://arduinomodules.info/wp-content/uploads/KY-003_Fritzing_custom_part_image-130x240.png) | Hall effect magnetic |  interruptor que se encenderá / apagará en presencia de un campo magnético. | [Más información](https://arduinomodules.info/ky-003-hall-magnetic-sensor-module/) | Giezy Martínez De La Cruz

## Descripción

KEYES KY-003 Arduino Hall Magnetic Sensor Module is a switch that will turn on/off in the presence of a magnetic field. Consists of a 3144EUA-S sensitive Hall-effect switch for high-temperature operation, a 680Ω resistor and a LED. Compatible with popular electronics platforms like Arduino and Raspberry Pi.

The whole magnetic sensor known as KY 003. This is a module itself. So let's get started. This module has integrated on board a magnetic sensor called a 3141. One is sr, and one LED. The resistor used in this module is six sounded at arm and the main reason for using the resistor is to limit current circulating inside the module. In other words to prevent the current from burning our module. The LED lights up to show if the module is working properly or not. Now I will show how these components are connected together. 

There we have the sensor itself and of course led as one other resistor r1 on the right you can see how the pins of the module are connected all these board. So, we have internet the flow of the voltage, we have in black of a flow of the ground. And of course, we have in green the flow of the signal, this module It is used to detect the magnetic field.

## Especificación
El sensor magnético de salón KY-003 consta de un interruptor de efecto Hall sensible 3144EUA-S para operación a alta temperatura, una resistencia de 680o y un LED. Compatible con plataformas electrónicas populares como Arduino y Raspberry Pi.

| Voltaje | temperatura | Dimensiones |
--- | --- | --- 
4.5V a 24V | -40 oC a 85 oC [-x oF a x oF] | 18,5 mm x 15 mm [0,728 pulgadas x 0,591 pulgadas]

## Diagrama de conexión



## Código

```C++
int led = 13;//LED pin
int sensor = 3; //sensor pin
int val; //numeric variable

void setup()
{
	pinMode(led, OUTPUT); //set LED pin as output
	pinMode(sensor, INPUT); //set sensor pin as input
}

void loop()
{
	val = digitalRead(sensor); //Read the sensor
	if(val == LOW) //when magnetic field is detected, turn led on
	{
		digitalWrite(Led, HIGH);
	}
	else
	{
		digitalWrite(Led, LOW);
	}
}
```
