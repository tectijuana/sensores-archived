# Class Bihor Magnetic Sensor

![](cooltext364833552088827.png)
![](400px-Arduino_KY-035_Class_Bihor_magnetic_sensor.png)
|SENSOR   | FUNTION  | COLABORADOR  |  URL |
|---|---|---|---|
| Class Bihor Magnetic Sensor  | he strength of the field is given by an analog voltage at the signal pin of the module KY-035  |  CASTILLO OSCAR | https://tkkrlab.nl/wiki/Arduino_KY-035_Class_Bihor_magnetic_sensor#:~:text=KY-035%20is%20an%20analog,5V%20of%20the%20Arduino%20board.&text=The%20led%20on%20the%20board,strength%20of%20the%20magnetic%20field.  |
# DESCRIPTION
KY-035 is an analog magnetic field sensor module. The strength of the field is given by an analog voltage at the signal pin of the module KY-035. The sensor is connected to gnd and 5V of the Arduino board. The output voltage is measured by analog pin A5 on the Arduino board.

The example program measures the output voltage of the sensor en presents the measured value in the serial monitor of the Arduino.

The led on the board flashes in a speed depending on the strength of the magnetic field. With a small magnet this can be demonstrated.
# CONNECTING TO ARDUINO
- Pin - = GND, connect to GND of the Arduino
- Pin (middle pin) +5 V, connect to Arduino +5 V
- Pin S signal, connect to Arduino pin A5
- Power consumption sensor, 8 mA
# CODE
/* 
KY-035 Hall analog sensor
*/
 
int sensorPin = A5;    // select the input pin
int ledPin = 13;       // select the pin for the LED
int sensorValue = 0;   // variable to store the value coming from the sensor
 
void setup () {
  pinMode (ledPin, OUTPUT);
  Serial.begin (9600);
}
 
void loop () {
  sensorValue = analogRead (sensorPin);
  digitalWrite (ledPin, HIGH);
  delay (sensorValue);
  digitalWrite (ledPin, LOW);
  delay (sensorValue);
  Serial.println (sensorValue, DEC);
}
