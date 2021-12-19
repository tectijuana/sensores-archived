#
# OSCAR HERNANDEZ MEDINA
# Reviso Aquino Villegas Daniel 18212144
from machine import Pin
import utime

sensor=Pin(26, Pin.IN)
utime.sleep(1)

while True:
    if sensor.value()==1:
        print("Campo magnetico detectado")
        utime.sleep(1)    
    else:
        print("Ningun campo detectado")
        utime.sleep(1)
utime.sleep(1)
