# Codigo por Rivera Perez Alex 18212259 
# Al inclinar el sensor se despliega el mensaje "Sensor detectado"
# Revisado por Aquino Villegas Daniel 18212144
from machine import Pin
import utime

pin=27
sensor=Pin(pin, Pin.IN)
utime.sleep(1)

while True:
    if sensor.value()==1:
        print("Sensor detectado")
        utime.sleep(2)    
    else:
        print("No detectado")
        utime.sleep(2)
utime.sleep(1)
