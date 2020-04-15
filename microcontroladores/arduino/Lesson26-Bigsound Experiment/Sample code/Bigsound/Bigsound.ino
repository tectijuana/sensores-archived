/*
 * Author: SMRAZA KEEN
 * Date:2016/6/29
 * IDE V1.6.9
 * Email:TechnicSmraza@outlook.com
 * Function:
 * Tips:Open the serial port
 */
int analog_sensor  = A0; // select the input pin for the potentiometer
int digit_sensor = 8; // select the input pin for the potentiometer
int analogValue ; // value from the analog input pin
int digitValue ;  //  value from the digit input pin
void setup () 
{
pinMode (digit_sensor, INPUT);
Serial.begin (9600);
}
void loop () 
{
  analogValue = analogRead (analog_sensor);
  digitValue=digitalRead(digit_sensor);
  Serial.print("analogValue=");
  Serial.print(analogValue);
  Serial.print('\t');
  Serial.print("digitValue=");
  Serial.println (digitValue);
  delay(300);
}
