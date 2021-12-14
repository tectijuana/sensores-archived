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

