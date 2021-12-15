#  Verificado y corregido por Alvarez Espinoza Raul - 18212141
from machine import Pin
import time

laser = Pin(18, Pin.OUT)

while True:
    laser.value(1)
    time.sleep(0.2)
    laser.value(0)
    time.sleep(0.2)
