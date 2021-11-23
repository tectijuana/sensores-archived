# SMALL PASSIVE BUZZER MODULE
## Description
Arduino Passive Piezoelectric Buzzer Module Keyes KY-006, it can produce a range of sound tones depending on the input frequency.
![KY-006](https://arduinomodules.info/wp-content/uploads/KY-006_passive_buzzer_arduino_module-240x240.jpg)
## Specifications
The KY-006 Buzzer Module consists of a passive piezoelectric buzzer, it can generate tones between 1.5 to 2.5 kHz by switching it on and off at different frequencies either using delays or PWM.
| Description           | Info                              |
|-----------------------|-----------------------------------|
| Operating Voltage     | 1.5 ~ 15V DC                      |
| Tone Generation Range | 1.5 ~ 2.5 kHz                     |
| Dimensions            | 18.5mm x 15mm [0.728in x 0.591in] |
## KY-006 Connection Diagram
Connect signal (S) to pin 8 on the Arduino and ground (-) to GND. The middle pin is not used.
![Diagram](https://arduinomodules.info/wp-content/uploads/Arduino_KY-006_Keyes_Passive_buzzer_module_connection_diagram.png)
## KY-006 Example Code
The following Arduino sketch will generate two different tones by turning on and off the KY-006 buzzer at different frequencies using a delay.
```javascript
int buzzer = 8; // set the buzzer control digital IO pin

void setup() {
	pinMode(buzzer, OUTPUT); // set pin 8 as output
}

void loop() {
	for (int i = 0; i < 80; i++) {  // make a sound
		digitalWrite(buzzer, HIGH); // send high signal to buzzer 
		delay(1); // delay 1ms
		digitalWrite(buzzer, LOW); // send low signal to buzzer
		delay(1);
	}
	delay(50);
	for (int j = 0; j < 100; j++) { //make another sound
		digitalWrite(buzzer, HIGH);
		delay(2); // delay 2ms
		digitalWrite(buzzer, LOW);
		delay(2);
	}
	delay(100);
}
