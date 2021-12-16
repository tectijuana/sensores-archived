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
![](https://github.com/tectijuana/sensores/blob/74f2e97c91f8306d8f9de4a0e29e710dfd39fb5b/PYTHON/KY-003_Hall_Magnetic/diagrama/diagrama.png)
 
 ## Código

```python
#
# OSCAR HERNANDEZ MEDINA
#
from machine import Pin
import utime

sensor=Pin(26, Pin.IN)
utime.sleep(1)

while True:
    if sensor.value()==1:
        print("Campo magnetico detectado")
        utime.sleep(1)    
    else:
        print("Ningun campo detectado")
        utime.sleep(1)
utime.sleep(1)
```
