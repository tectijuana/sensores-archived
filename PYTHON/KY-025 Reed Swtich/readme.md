# KY-025 Reed Switch
<img src="https://uelectronics.com/wp-content/uploads/2017/06/AR0043-Sensor-KY-025-v5.jpg" width="250">

### ¿Qué es Sensor KY-025 Reed Switch?

_El KY-025 Reed Switch Module es un pequeño interruptor eléctrico operado por un campo magnético aplicado, comúnmente utilizado como sensor de proximidad._
_El módulo tiene salidas digitales y analógicas._
_Se utiliza un recortador para calibrar la sensibilidad del sensor._
_Compatible con Arduino, Raspberry Pi, ESP32 y otros microcontroladores._


### Especificaciones

| Voltaje de funcionamiento       | 3.3V a 5.5V             |
|---------------------------------|-------------------------|
| Dimensiones                     | 1.5cm x 3.6cm           |
| Salidas                         | Analógica y digital     |
|Sensor magnético                 | Alta sensibilidad       |
|Comparador de salida de corriente| 16 mA                   |
|Peso                             | 3 g                     |


### Material para testing

  - RASPBERRY PI
  - KY-053
  - KY-025 Reed Swtich
  - 8 wires(Conectores)

  
### Conexión


<img src="https://sensorkit.joy-it.net/files/files/sensors/KY-024/024-RPi.svg" width="500">

### Codigo

```
//Revisado por Daniel Garcia - 18212185
//No tendran la version con un Raspberry Pico?
//ACTUALIZADO ADRIANA PEREA

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

i2c = busio.I2C(board.SCL, board.SDA)

ads = ADS.ADS1115(i2c)

chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

delayTime = 1
Digital_PIN = 24

GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)

while True:
    analog = '%.2f' % chan0.voltage
 
    
    if GPIO.input(Digital_PIN) == False:
        print ("Analog voltage value:", analog, "V, ", "Limit: not yet reached")
    else:
        print ("Analog voltage value:", analog, "V, ", "Limit: reached")
    print ("---------------------------------------")

    button_pressed = False
    time.sleep(delayTime)
```
##Ejecución
```bash
sudo python3 KY024-RPi.py
```
