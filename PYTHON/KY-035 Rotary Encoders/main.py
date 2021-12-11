#Amador Garcia Fernando

#1ra-Revisado por Daniel García Chacón - 18212185
#CORREGIDO: La RPI Pico no soporta la libería RPi, solo es para la RPI 3

from machine import Pin

button_pin = Pin(16, Pin.IN, Pin.PULL_UP)
direction_pin = Pin(17, Pin.IN, Pin.PULL_UP)
step_pin  = Pin(18, Pin.IN, Pin.PULL_UP)

previous_value = True
button_down = False

while True:
     if previous_value != step_pin.value():
         if step_pin.value() == False:
             if direction_pin.value() == False:
                 print("turned left")
             else:
                 print("turned right")
         previous_value = step_pin.value()   
    
     if button_pin.value() == False and not button_down:
         print("button pushed") 
         button_down = True
