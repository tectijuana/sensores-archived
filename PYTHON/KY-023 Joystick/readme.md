   ![cooltext399252547415326](https://user-images.githubusercontent.com/79487256/144521544-71de8013-3d80-4cb7-b062-635800397118.png)

![ky-023-v8-150x150](https://user-images.githubusercontent.com/79487256/144521798-79c184b9-169e-4915-bc6c-4263fecfd33d.jpg)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## INFORMACIÓN
¿Qué es Módulo KY-023 Sensor JoyStick?
El Módulo KY-023 Sensor JoyStick es un dispositivo electromecánico consta de dos potenciómetros en un ángulo de 90 grados, lo que se requiere de 2 pines analógicos para realizar la interfaz con cualquier tarjeta de desarrollo: Arduino, ESP32, ESP8266, etc.

## ¿Para qué sirve?

Este elemento te permite controlar y manejar determinados aparatos electrónicos. Normalmente se utilizan para proyectos robóticos en el cual se necesitan para la movilidad analógica de las articulaciones de un brazo robótico. El Módulo Joystick, es más utilizado para proyectos de robótica y control de dispositivos RF(Radio Frecuencia)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Diagramas
![Image 18](https://user-images.githubusercontent.com/79487256/144523109-d0257b82-60ba-4cde-81f8-fe50723e613e.png)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Tablas técnicas

| ESPECIFICACIÓN Y CARACTERÍSTICAS |
| :--- |
| Módulo: JoyStick biaxial XY (KY-023) |
| Voltaje de alimentación: 3.3 V a 5V |
| Salida: Analógica(X,Y) y Digital(Z) |
| Número de potenciómetros: 2 de 10Kohm. |
| Pulsador central normalmente abierto. |
| Dimensiones: 40mm x 26mm  x 32 mm |
| Peso: 14 g |

## Como conectar correctamente.

| RASPBERRY PI | SENSOR |
| ---| --- |
| GPIO 24 [Pin 18] | button |
| 3.3V [Pin 1] | +V |
| ground [pin 6] | GND |
| KY-053 A1 | VRy |
| KY-053 A0 | VRx |

| SENSOR | RASPBERRY PI |
| --- | --- |
| VRy | A1 |
| VRx | A0 |
| +V | 3.3V [Pin 1] |
| GND | Ground [Pin 6] |

| RASPBERRY PI | SENSOR |
| ---| --- |
| GPIO 3 [Pin 5] | SCL |
| Gpio 2 [Pin 3] | SDA |


## Código

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
# Librerias
import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# GPIO 24
Button_PIN = 24
GPIO.setup(Button_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

delayTime = 0.2
# Crear el Bus I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Crear el objeto ADC usando el bus I2C
ads = ADS.ADS1115(i2c)

# Crear una entrada de un solo extremo en los canales
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)


while True:
    # Los valores actuales se registran
    x = '%.2f' % chan0.voltage
    y = '%.2f' % chan1.voltage
```


## COMO EJECUTAR 
``` sudo python3 KY023-RPi.py ```
