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

![1 1](https://user-images.githubusercontent.com/79487256/144535156-f3b5fcfe-6b14-4d8b-9186-60a15f3dce23.png)


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
from machine import Pin, ADC
import utime
 
xAxis = ADC (Pin (27))
yAxis = ADC (Pin (26))
button = Pin (16,Pin.IN, Pin.PULL_UP)
 
while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value ()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    if xValue <= 600:
        xStatus = "left"
    elif xValue >= 60000:
        xStatus = "right"
    if yValue <= 600:
        yStatus = "up"
    elif yValue >= 60000:
        yStatus = "down"
    if buttonValue == 0:
        buttonStatus = "pressed"
    print ("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
    utime.sleep(0.1)
```

## COMO EJECUTAR 
``` sudo python3 KY023-RPi.py ```
