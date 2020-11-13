

int shockPin = 10;    // Use Pin 10 as our Input
int shockVal = HIGH; // This is where we record our shock measurement 
boolean bAlarm = false;
unsigned long lastShockTime; //Record the time that we measured a shock 
int shockAlarmTime = 250; //Number of milli seconds to keep the shock alarm high
void setup ()
{
Serial.begin(9600);
pinMode (shockPin, INPUT) ;
}
void loop ()
{
shockVal = digitalRead (shockPin) ; // read the value from our sensor
if (shockVal == LOW) // If we're in an alarm state
 
lastShockTime = millis(); // record the time of the shock
  if (!bAlarm)
 {
   Serial.println("Shock module");
   bAlarm = true;
  }
   else
{
  if( (millis()-lastShockTime) > shockAlarmTime && bAlarm)
  { Serial.println("no alarm");
    bAlarm = false;
     }
   }
}



