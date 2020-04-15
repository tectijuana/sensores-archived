/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
int led = 11;
int val;
void setup()
{
  pinMode(led,OUTPUT);
}
void loop()
{
  val=analogRead(0); 
  if(val<512)
  {
    digitalWrite(led,HIGH);    
  }
  else
  digitalWrite(led,LOW);
}
