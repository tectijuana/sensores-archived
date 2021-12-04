#EJERCICIO: Realizar un montaje que sea necesario pulsar 1 boton para que se encienda el led. - Medina Beltran Carlos Alberto 18212216

from machine import Pin
import time

button=Pin(2,Pin.IN)
led=Pin(16,Pin.OUT)

while True:
    state=button.value()
    led.value(state)
    time.sleep(0.5)
