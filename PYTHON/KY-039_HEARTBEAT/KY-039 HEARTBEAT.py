from machine import ADC
from utime import sleep

sensor = ADC(26)

conversion_factor = 3.3 / (65535)

while True:
        lectura = sensor.read_u16() * conversion_factor
	print(lectura)
        sleep(0.09)
