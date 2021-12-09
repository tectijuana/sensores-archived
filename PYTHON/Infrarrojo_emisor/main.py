"""
Palacios Sotelo Ignacio Josafat
L21210894@tectijuana.edu.mx
"""
#Programa para KY-005
import machine
import utime
 
led = machine.Pin(16,machine.Pin.OUT)

while True:
    led.value(1)
