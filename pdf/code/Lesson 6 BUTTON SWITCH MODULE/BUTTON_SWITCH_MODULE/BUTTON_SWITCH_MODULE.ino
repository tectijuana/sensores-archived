/******************************************
 *Website: www.elegoo.com
 * 
 *Time:2017.12.12
 *
 ******************************************/
int Led = 13; //define LED port
int Shock = 3; //define shock port
int val;//define digital variable val
void  setup()
{
  pinMode(Led, OUTPUT); //define LED as a output port
  pinMode(Shock, INPUT); //define shock sensor as a output port
}
void  loop()
{ val = digitalRead(Shock); //read the value of the digital interface 3 assigned to val
  if (val == HIGH)         //when the shock sensor have signal, LED blink
  {
    digitalWrite(Led, LOW);
  }
  else
  {
    digitalWrite(Led, HIGH);
  }
}

