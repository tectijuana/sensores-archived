![](sensor1.png)

The sound detection microphone module known as KY 0 37. This is the module itself. So let's get started. Today's video is brought to you by our GVS an online store where you can find shirts, jeans and gold accessories that fit your needs. The products are made in Italy, they can be shipped worldwide, so don't waste your time start looking fancy today with their site. For more information go to RGV SM sharp dot net or check it out at the link on the video description.

This module is integrated on board one microphone one potentiometer on microchip sixers diesters m two led the resistor r1. Using this module it's on there as these are our two it's 100 kilo ohms. There is this there are three it's 150 on there is therefore it's one kilo ohm. There's these there are five it's one kilo and there is Easter it is 100 kilo ohms The main reason for using the resistors is to limit currency collating inside the module. In other words, to prevent current from burning our module the LED will light up to show if the module is working properly or not.

![](connectionsarduino2.PNG)
![](input2.PNG)
#### EXAMPLE SENSOR CODE:
```
// Declaration and initialization of the input pin
int Analogue_Eingang = A0; // X-axis-signal
int Digital_Eingang = 3; // Button
void setup ()
{
pinMode (Analogue_Eingang, INPUT);
pinMode (Digital_Eingang, INPUT);
Serial.begin (9600); // Serial output with 9600 bps
}

// The program reads the current value of the input pins
// and outputs it via serial out

void loop ()
{
float Analogue;
int Digital;

// Current value will be read and converted to voltage
Analogue = analogueRead (Analogue_Eingang) * (5.0 / 1023.0);
Digital = digitalRead (Digital_Eingang);

//... and outputted here
Serial.print ("Analogue voltage value: "); Serial.print (Analogue,4); Serial.print ("V, ");
Serial.print ("Extreme value: ");

if(Digital==1)
  {
    Serial.println (" reached");
  }
  else
  {
    Serial.println (" not reached yet");
  }
  
Serial.println ("----------------------------------------------------------------");
delay (200);

}

```
