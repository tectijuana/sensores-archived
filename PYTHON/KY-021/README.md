# MODULO KY-021 MINI SWITCH

![](https://arduinomodules.info/wp-content/uploads/KY-021_mini_magnetic_reed_switch_module_arduino.jpg)

# MARCO TEÓRICO

## DESCRIPCIÓN

> ¿Que es?

El módulo KY-021 es un sensor interruptor magnético que te permitirá detectar campos magnéticos de una forma rápida, fácil y eficiente, por medio de su mini lámina magnética que viene incorporada al modulo. Esta lámina magnética se encuentra comúnmente abierta (CA) y al detectar un campo magnético se cierra, permitiendo el paso del voltaje.

> ¿Para que sirve?

El KY-021 contiene una resistencia de 10 kΩ y una pequeña lengüeta magnética que comúnmente es utilizado en sistemas mecánicos como sensores de proximidad o como interruptor digital magnético. Este modulo es compatible con plataformas electrónicas populares como Arduino, Teensy, Raspberry Pi y ESP8266.

> ESPECIFICACIONES Y CARACTERÍSTICAS 
- Tipo: Sensor Interruptor Magnético
- Numero de modelo: KY-021
- Voltaje de funcionamiento: 3.3 V a 5 V
- Tipo de salida: Digital
- Dimensiones: 21 mm x 15 mm x 9 mm
- Peso: 2 g

![](https://uelectronics.com/wp-content/uploads/AR0039-Sensor-KY-021-Mini-interruptor-Magnetico-v2.jpg)

# TABLAS TÉCNICAS



Operating Voltage | 3.3V ~ 5V
-- | --
Output Type | Digital
Board Size | 18.5mm x 15mm [0.728in x 0.591in]


# DIAGRAMAS

## Diagrama esquemático
![image](https://user-images.githubusercontent.com/59489846/145524913-074cc2bd-ae3c-469d-a67b-fb8384f82931.png)

## Diagrama Gráfico
![image](https://user-images.githubusercontent.com/59489846/145525022-07aab8f8-96dd-4a9a-90a8-50a19bfbc34d.png)


## Código

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```python

# inicio del programa del relevador

# Needed modules will be imported and configured 
import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
# The input pin which is connected with the sensor
GPIO_PIN = 21
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
  
print "KY-021 Sensor Test [press ctrl+c to end the test]"
  
def outputFunction(null):
        print("Sensor is blocked")
  
# signal detection (raising edge).
GPIO.add_event_detect(GPIO_PIN, GPIO.RISING, callback=outputFunction, bouncetime=100) 
  
# Main program loop
try:
        while True:
                time.sleep(1)
  
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()

# brychxpin was here

```

## COMO EJECUTAR 
```pi@raspberrypi~ python main.py```


