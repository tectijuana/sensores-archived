#Cuevas Oliva Josue Emanuel 18212164
#Revisado por Aquino Villegas Daniel 
#Fallo: Solo detecta flama en todo momento

from machine import Pin
import utime

flame_sensor = Pin(16, Pin.IN)
utime.sleep(2)

while True:
   if flame_sensor.value() == 1:
       print("Flame Detected")
       utime.sleep(3)
   else:
       print("No Flame")
       utime.sleep(1)
utime.sleep(0.1)
