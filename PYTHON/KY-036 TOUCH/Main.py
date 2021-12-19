from machine import Pin
import utime

flame_sensor = Pin(16, Pin.IN)
utime.sleep(2)

while True:
   if flame_sensor.value() == 1:
       print("Tocando")
       utime.sleep(3)
   else:
       print("Libre")
       utime.sleep(1)
utime.sleep(0.1)
