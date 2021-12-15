<a href="https://es.cooltext.com"><img src="https://images.cooltext.com/5568078.png" width="522" height="97" alt="Rotary Encoders" /></a>
<br />Image by <a href="https://es.cooltext.com">Cool Text: Free Graphics Generator</a> - <a href="https://es.cooltext.com/Edit-Logo?LogoID=3990886918">Edit Image</a>

![image](https://www.prometec.net/wp-content/uploads/2018/01/rotary-encoder.jpg)


## Marco Teorico

Un <u>codificador rotatorio</u>, también llamado "codificador del eje" o "generador de pulsos".
Suele ser un dispositivo electromecánico usado para convertir la posición angular de un eje a un código digital, lo que lo convierte en una clase de transductor. 

## Tablas técnicas

| ESPECIFICACIÓN Y CARACTERÍSTICAS |
| :--- |
| Módulo: Rotary Encoders (KY-035) |
| Voltaje de alimentación: 5V |
| Círculo de pulso: 20 |
| Dimensiones: ‎4 x 0.7 x 3 pulgadas |
| Peso: 0.352 Onzas |

## Diagramas
![image](144543260-97e09c03-6092-4ff0-a6f3-98debacaff9e.png)

## Codigo

```python
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
```
