# Martinez Estrada Ana Karen
# Revisado por Aquino Villegas Daniel

import machine import pin
import utime import sleep

Sound = Pin (28, Pin.IN)
led = pin(22,pin.OUT)
clap_count=1

while True:
    ded.value(1)
    if Sound.value()==1 and clao_count==1:
        led.value(1)
        Sound.value(0)
        sleep(0.50)
        
    if Sound.value()==1 and clap_count==2:
        led.value(0)
        clap_count=1
        Sound.value(0)
        sleep(0.5)
