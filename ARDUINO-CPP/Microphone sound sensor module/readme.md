![](sensor2.png)

The sound detection microphone module known KY 0 38. This is a module itself. So let's get started. Today's video is brought to you by our GVS an online store where you can find shirts, jeans and gold accessories that fit your needs. All the products are made in Italy, they can be shipped worldwide, so don't waste your time start looking fancy today with their site.For more information, go to RGB SM shop dot net or check it out at the link on the video description.
This module is integrated on board one microphone one potentiometer on microchip sixers. diesters m two LED is the resistor r1 used in this module. It's Thank you arms. There is the SIR r two it's 100 kilo ohms there is the sir are three it's 150 ohms There is there are four it's one kilo there is this there are five it's one kilo and there is this there it is 100 kilo ohms. The main reason for using the resistors is to limit currents equal leading inside the module. In other words, to prevent current from burning our module, the LED l on light up to show if the module is working properly or not.

![](connectionsarduino.PNG )
![](input.PNG )

EXAMPLE SENSOR CODE:

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
Serial.print ("Analogue voltage value:"); Serial.print (Analogue,4); Serial.print ("V, ");
Serial.print ("Extreme value:");
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
