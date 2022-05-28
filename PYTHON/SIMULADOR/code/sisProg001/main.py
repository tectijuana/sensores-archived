# -------------------------------- #
# Sistemas programables            #
# Practica 1                       #
# González Martínez Álvaro Gabriel #
# -------------------------------- #

from machine import Pin
from time import sleep as delay

led = Pin(2, Pin.OUT)

led.value(0)

while True:
    led.value(1)
    delay(1)
    led.value(0)
    delay(1)