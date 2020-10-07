![](5Vrelaymodulo.png)


![](modulo.png)


The relay module known as KY 0 19. This is a module itself. So let's
get started. Today's video is brought to you by all our GVS and an
online store where you can find shirt jeans and call accessories that
fit your needs. All the products are made in Italy, they can be
shipped worldwide, so don't waste your time start looking fancy
today with their stock. For more information, go to RGV SM sharp
dot net or check it out at the link on the video description. This
module is integrated on board. One led one resistor One diet and one
transistor. The resistor used in this module is 150 M. And the main
reason for using the resistor is to limit currency collating inside the
module. The LED lights up to show if the module is working or not.
Now, I will show how these components are connected together.
There we have the relay itself and we can see the LED l one, the
resistor r1, the transistor q1 and of course, the diodes The one on the
right you can see how the piece of the module I connected on this
board, we have inlet the flow of the voltage we have in black, the
flow of the ground and of course we have in green the flow of a
signal relays are switches that open and close secrets electro
mechanically or electronically. The relays control one electrical
circuit by opening and closing contacts in another circuit. As relayed
diagrams show when a relay contacts is normally open, there is an
open contact owner relay it's not energized. When the relay contact is
normally closed, there is a closed contact when you lay it's not
energized. In either case, applying electrical current to the contact
will change their state. relays are generally used

![](modulo2.png)

to switch smaller gardens in the console to quit and do not usually
control power consuming devices. Now the less relays can control
larger voltages and emperors by having an amplifying effect because
of some voltage applied to her lace coil case out in a large voltage
being switched by the contacts. Let's talk about the pins. The pins in
this module are three, we have the ground pin with a minus sign, the
voltage pin is in the middle. And of course we have the pin of the
signal with the S sign. So let's talk about the signal. This module
takes a digital signal so we can connect the pain of the signal with
any digital port of different microcontroller boards like Arduino or
Raspberry Pi.

EXAMPLE SENSOR CODE:

``` 
int relay = 10; //Pin 10
void setup()
{
pinMode(relay,OUTPUT);
the port attribute as output
}
void loop()
{
digitalWrite(relay,HIGH);
relay ON
// [NO] is connected to feed
// [NC] is not connected to feed
delay(1000);
// turn the
// Define
digitalWrite(relay,LOW);
// turn
the relay OFF
// [NO] is not connected to feed
// [NC] is connected to feed
delay(1000);
``` 
