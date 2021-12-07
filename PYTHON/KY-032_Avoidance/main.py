# Se importan los pines y utime.
from machine import Pin
import utime
# Conectamos los pines del Raspberry al sensor y al led. Y los configuramos
led = Pin(16, Pin.OUT)
sensor = Pin(15, Pin.IN)
# Con este loop estaremos detectando si hay un obstaculo o no
while True:
# Con estás lineas imprimimos el valor del sensor (0 o 1)
	print(sensor.value())
	utime.sleep_ms(20)
	
# Con el if decidimos si se prende el led o no, segun el valor del sensor
	if sensor.value() == 1:
		led.value(0)
	else:
		led.value(1)
