# Sensor Vibración Módulo KY-002
![ky002](https://user-images.githubusercontent.com/89440798/144691038-c20e698e-3520-4910-87c0-a5825c90564b.png)

## Marco teórico 
Este sensor detecta cualquier tipo de movimiento que se encuentre en el switch. Es implementado en máquinas expendedoras cuando detectan un forcejeo o intento de robo, también en el desbalance de un motor de un sistema de ventilación, o en golpes de cerraduras, candados entre otros. 

Lo que realiza este programa es que al detectar movimiento, enciende el LED, en caso de que el LED esté encendido, se apaga. Es útil para seguridad donde se requiera conectar una alarma donde se active si se detecta forcejeo de una puerta.

## Ficha técnica

* Tensión de trabajo 3.3 V  – 5 V
* Corriente: 5 mA
* Dimensiones : 18.5 mm x 15 mm
* Peso: 4 gr
* Señal digital de salida Inversa: Alta (HIGH) significa cuando no hay detección de vibración y un nivel bajo (LOW) es porque tenemos vibración.

## Diagrama 

![ky002_diagrama](https://user-images.githubusercontent.com/89440798/144733252-07170c6a-69e0-42c4-89b2-d2620654cf57.png)


## Código
```python
# Cortez Flores Adrián Alejandro 18212163

#Revisado por Daniel García Chacón - 18212185
#NOTA: Ya lo calé, le hice unas modificaciones a la sintaxis, pero el programa parece que no hace nada :/

import sys
# import RPi.GPIO as GPIO
from machine import Pin


estadoKY = 0
KY002 = Pin(7, Pin.IN) # Pin asignado para Sensor Vibración
LED = Pin(11, Pin.OUT) # Pin asignado para LED

while True:
    estadoKY = KY002.value() # Busca el valor del sensor KY002 booleano (si detecta movimiento)
    if estadoKY == 1: # Si detecta movimiento 
        if LED.value == 0: # Si el LED está apagado
            LED.value(1) #Se enciende
        else:  # Si no
            LED.value(0) #Se apaga
 ```
