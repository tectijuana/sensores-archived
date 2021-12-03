# De Jesus Romero Luis Alfredo

from machine import Pin
import time

led_pins = [16,17,18] # Pines en donde esta el cableado del RGB
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT),
        Pin(led_pins[2],Pin.OUT)] # matriz de control de pines
delay_t = 0.1 # segundos de espera entre cambios
while True: # bucle infinito
    for led in leds: # iteración entre cada led
        led.high() # led encendido
        time.sleep(delay_t) # espera
        led.low() # led apagado
        time.sleep(delay_t) # espera
