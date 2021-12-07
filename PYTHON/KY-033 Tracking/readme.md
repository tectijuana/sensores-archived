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


![Captura de pantalla 2021-12-07 144056](https://user-images.githubusercontent.com/42977905/145117189-97d92061-dc45-4866-a3cc-5f9a5d183458.png)


-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
##Código

```
# Los módulos necesarios se importarán y configurarán
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Declaración del pin de entrada que está conectado con el sensor
GPIO_PIN = 18
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# La ruptura entre los resultados se definirá aquí (en segundos)
delayTime = 0.2

print "#--- Proyecto de Tracking ---#"

# Bucle principal
try:
        while True:
            if GPIO.input(GPIO_PIN) == False:
                print "Linea detectada"

            # Reset + Delay
            time.sleep(delayTime)

# Trabajo de recolección de residuos una vez finalizado el programa
except KeyboardInterrupt:
        GPIO.cleanup()
 ```
 
