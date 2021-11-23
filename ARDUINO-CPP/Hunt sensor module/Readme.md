# Hunt sensor module
![](cooltext364834821748877.png)
![](Screen-Shot-2018-03-11-at-3.24.19-PM.png)

|SENSOR   | FUNTION  | COLABORADOR  |  URL |
|---|---|---|---|
| Hunt sensor module  | The KY-033 Hunt sensor module detects if a light reflecting or absorbing area is in front of it  |  CASTILLO OSCAR | http://www.mikroblog.net/arduino/arduino-code/ky-033-hunt-sensor-module-arduino-example.php#:~:text=The%20KY-033%20Hunt%20sensor,in%20front%20of%20the%20module.  |

# DESCRIPTION
The KY-033 Hunt sensor module detects if a light reflecting or absorbing area is in front of it. This module uses an IR transmitter and receiver that will detect how reflective the surface is in front of the module. It has a potentiometer to adjust the sensitivity of the module so it can detect if the surface is black or white.

Operating voltage: 2.5V – 12V(cannot over 12V)
Working current: 18mA – 20mA at 5V
Output electrical level signal: low level when detecting objects / high level when no objects / 0 or 1 decides if objects exist

This behavior can be used to automatically follow a line with a robot and this is a very common application of this module
# CODE
int Sensor = 3; // sensor input pin
 
void setup ()
{
  Serial.begin(9600); // Initialize serial output
  pinMode (Sensor, INPUT) ;
}
 
 
void loop ()
{
  bool val = digitalRead (Sensor) ; // The current signal of the sensor will be read
 
  if (val == HIGH)
  {
    Serial.println("Line detected");
  }
  else
  {
    Serial.println("Line not detected");
  }
  Serial.println("------------------------------------");
  delay(500); // 
}
