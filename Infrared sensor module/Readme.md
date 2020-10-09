# Infrared sensor module
## Description 
The IR sensor module consists mainly of the IR Transmitter and Receiver, Opamp, Variable Resistor (Trimmer pot), output LED in brief.
![IR sensor](https://components101.com/sites/default/files/inline-images/IR-Sensor-Module-Brief_0.png)
## Specifications
- 5VDC Operating voltage
- I/O pins are 5V and 3.3V compliant
- Range: Up to 20cm
- Adjustable Sensing range
- Built-in Ambient Light Sensor
- 20mA supply current
- Mounting hole
## PIN Configuration
| PIN Name | Description         |
|----------|---------------------|
| VCC      | Power Supply Input  |
| GND      | Power Supply Ground |
| OUT      | Active High Output  |
## Connection Diagram
To connect a breakout board mounted IR receiver, hook it up to the Arduino like this:
![IR Diagram](https://www.circuitbasics.com/wp-content/uploads/2017/05/Arduino-IR-Remote-Receiver-Breakout-Board-Wiring-Diagram.png)
## IR Sensor Module Example Code
```javascript
int IRSensor = 2; // connect ir sensor to arduino pin 2
int LED = 13; // conect Led to arduino pin 13



void setup() 
{



  pinMode (IRSensor, INPUT); // sensor pin INPUT
  pinMode (LED, OUTPUT); // Led pin OUTPUT
}

void loop()
{
  int statusSensor = digitalRead (IRSensor);
  
  if (statusSensor == 1)
    digitalWrite(LED, LOW); // LED LOW
  }
  
  else
  {
    digitalWrite(LED, HIGH); // LED High
  }
  
}
