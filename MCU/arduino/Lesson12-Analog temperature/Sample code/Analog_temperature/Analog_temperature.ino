/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 */
void setup()
{
  Serial.begin(9600);      //Set serial baud rate to 9600 bps
}
void loop()
{
  int val;
  val=analogRead(0);      //Read value from analog 0
  Serial.print("Val=");
  Serial.println(val,DEC);    //Print the value to serial port
  delay(200);
}

