/******************************************
 *Website: www.elegoo.com
 * 
 *Time:2017.12.12
 *
 ******************************************/
int Led=13;      //define the led's port
int buttonpin=3; //define the port of light blocking module
int val;//define digital variable val
void  setup()
{
pinMode(Led,OUTPUT);//define digital variable val
pinMode(buttonpin,INPUT);//define light blocking module as a output port
}
void  loop()
{ val=digitalRead(buttonpin);//read the value of the digital interface 3 assigned to val 
if(val==HIGH)               //when the light blocking sensor have signal, LED blink
{
digitalWrite(Led,LOW);
}
else
{
digitalWrite(Led,HIGH);
}
}
