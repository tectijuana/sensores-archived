# Se importan los pines y utime
# Revisado por Aquino Villegas Daniel 18212144
from machine import Pin
import utime

sensor = Pin(18, Pin.IN)
utime.sleep(2)

while True:
# Se imprime un mensaje en función del valor del sensor
    if sensor.value() == 1:
        print("Libre")
    else:
        print("Línea")
    utime.sleep(2)
