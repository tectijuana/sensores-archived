![](https://images.cooltext.com/5568705.png)
<a href="http://cooltext.com" target="_top"><img src="https://cooltext.com/images/ct_pixel.gif" width="80" height="15" alt="Cool Text: Logo and Graphics Generator" border="0" /></a>
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Información
El Sensor de Obstáculos KY-033 infrarrojo o detector de línea es un dispositivo que detecta la presencia de un objeto mediante la reflexión que produce en la luz. El uso de luz infrarroja (IR) es simplemente para que esta no sea visible para los humanos. Actúa a distancias cortas, típicamente de 2 a 40 cm.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## ¿Para que sirve?
El Sensor de Obstáculos Módulo KY-033 te permitirá realizar una detección de línea de forma fácil, rápida y precisa, es compatible con cualquier microcontrolador que posea un pin de 5 V.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Diagrama


![Captura de pantalla 2021-12-07 144056](https://user-images.githubusercontent.com/42977905/145350368-20256cd6-c8dd-4a7c-9cf9-82accff284bf.png)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##Código

```
# Se importan los pines y utime
from machine import Pin
import utime

sensor = Pin(18, Pin.IN)
utime.sleep(2)

while True:
# Se imprime un mensaje en función del valor del sensor
    if sensor.value() == 1:
        print("Libre")
    else:
        print("Línea")
    utime.sleep(2)
    
 ```
 
