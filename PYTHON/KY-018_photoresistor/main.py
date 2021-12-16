#
# Programador: 
#
from machine import Pin
import time
photo_pin =machine.ADC(26) #GP26 Pin31
led = Pin(25, Pin.OUT)
while True:
    raw = photo_pin.read_u16() #La lectura tal cual lee el RB
    if (raw>30000): #si la lectura es mayor a 30000 imprimira ON
        print(str(raw) + " ON")
        led.on()
        
    else: #Si la lectura es menor a 30000 imprimira OFF
        print(str(raw)+" OFF")
        led.off()
    time.sleep(.2)
