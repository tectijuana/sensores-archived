# Codigo hecho y verificado por Alvarez Espinoza Raul - 18212141

from machine import Pin, ADC
import time

digital = Pin(18, Pin.IN)
analog = ADC(26)

while True:
    print(str(digital.value()) + ' - ' + str(analog.read_u16()))
    time.sleep(1)
