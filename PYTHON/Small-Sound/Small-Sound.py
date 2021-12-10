# Martinez Estrada Ana Karen
# Revisado por Aquino Villegas Daniel

from machine import Pin
from utime import sleep

Sound = Pin (28, Pin.IN)
led = Pin(22,Pin.OUT)
clap_count=1

while True:
    led.value(1)
    if Sound.value()==1 and clap_count==1:
        led.value(1)
        Sound.value(0)
        sleep(0.50)
        
    if Sound.value()==1 and clap_count==2:
        led.value(0)
        clap_count=1
        Sound.value(0)
        sleep(0.5)
