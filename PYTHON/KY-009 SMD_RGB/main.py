# Codigo hecho y verificado por Alvarez Espinoza Raul - 18212141

from machine import Pin
import time

'''
Don't forget the resistors for the leds
'''

red = Pin(19, Pin.OUT)
green = Pin(18, Pin.OUT)
blue = Pin(20, Pin.OUT)

while True:
    red.value(1)
    green.value(0)
    blue.value(0)
    time.sleep(1)
    
    red.value(0)
    green.value(1)
    blue.value(0)
    time.sleep(1)
    
    red.value(0)
    green.value(0)
    blue.value(1)
    time.sleep(1)
    
    red.value(1)
    green.value(1)
    blue.value(0)
    time.sleep(1)
    
    red.value(0)
    green.value(1)
    blue.value(1)
    time.sleep(1)
    
    red.value(1)
    green.value(0)
    blue.value(1)
    time.sleep(1)
    
    red.value(1)
    green.value(1)
    blue.value(1)
    time.sleep(1)
    
    red.value(0)
    green.value(0)
    blue.value(0)
    time.sleep(1)
