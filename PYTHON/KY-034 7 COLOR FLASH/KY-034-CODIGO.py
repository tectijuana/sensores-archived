#Modulo KY-034 7 Color Flash en Raspberry Pi Pico
#Chavez Duarte Fernando

from machine import Pin
from utime import sleep

led = Pin(3,Pin.OUT)

while True:
        led.on()
        sleep(1)
        led.off() 
        sleep(1)