# KY-003-Hall-Magnetic
El módulo de sensor Hall es un interruptor muy sensible que se activa mediante un campo magnético. Puede activarse mediante un imán natural o un electroimán. Las altas tasas de respuesta permiten tomar lecturas incluso a frecuencias de 100 kHz. Los usos más populares son la detección de proximidad para detectar la velocidad de los objetos que giran o como sensores de puertas.

Debido a la naturaleza de la detección (sin contacto), el módulo del sensor de pasillo es muy duradero y no hay desgaste asociado con el uso. Los sensores vienen generalmente sin enclavamiento, sin embargo, las versiones con enclavamiento son posibles (el sensor mantiene el estado después de que se ha quitado el imán hasta que se introduce la polaridad opuesta).

## Sobre el sensor
Este es un módulo de sensor analógico. El sensor se pone ALTO en el pin S cuando se detecta un campo magnético. La PCB contiene una luz LED que indica cuando el sensor detecta un campo y una resistencia para reducir la corriente suministrada a la placa. Es posible detectar cambios de voltaje, que ocurren cuando se aplica el campo magnético.
El valor del voltaje en el pin S dependería de la fuerza de un imán y la distancia desde el sensor.

## Especificaciones
| Voltaje operando            | 4.5V - 24V    |
|---------------------------|-------------------|
| Rango de temperatura operando   | -40°C - 85°C [-40°F - 185°F]    |
| Dimensiones         | 18.5mm x 15mm [0.728in x 0.591in]       |

![](https://arduinomodules.info/wp-content/uploads/KY-003_hall_magnetic_sensor_arduino_module-300x300.jpg)

## Diseño
![](https://i1.wp.com/www.notenoughtech.com/wp-content/uploads/2016/09/ky003.jpg?fit=265%2C300)

## Código
https://raw.githubusercontent.com/Oscar-HM/KY-003-Hall-Magnetic/main/main.py

```
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO_PIR = 24
print "KY-003 Module Test (CTRL-C = exit)"

GPIO.setup(GPIO_PIR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
def printFunction(channel):
    print("Detected")
    GPIO.add_event_detect(GPIO_PIR, GPIO.RISING, callback=printFunction)
try:
    while True :
        Current_State = GPIO.input(GPIO_PIR)
        except KeyboardInterrupt:
GPIO.cleanup()
```
