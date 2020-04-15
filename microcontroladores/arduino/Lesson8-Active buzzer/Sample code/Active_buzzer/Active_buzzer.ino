/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
int buzzer=5; 
void setup()
{
pinMode(buzzer,OUTPUT);
}
void loop()
{
digitalWrite(buzzer, HIGH); // produce sound
}

