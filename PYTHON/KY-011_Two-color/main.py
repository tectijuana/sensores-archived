#Cuevas Oliva Josue Emanuel 18212164
# Revisado por Daniel Aquino Villegas 18212144

from machine import Pin
import time

led_pins=[21,20]#Pines de LEDS
leds=[Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT)]#Matriz de control de pines

while True:
    for led in leds:#Iteracion entre cada led
        led.high()#LED Encendido
        time.sleep(0.1)#Tiempo de espera
        led.low()#LED Apagado
        time.sleep(0.1)#Tiempo de espera
    
