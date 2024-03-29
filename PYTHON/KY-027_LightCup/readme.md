![](https://images.cooltext.com/5568655.png)
<a href="http://es.cooltext.com" target="_top"><img src="https://cooltext.com/images/ct_pixel.gif" width="80" height="15" alt="Cool Text: Generador de Logotipos y Gráficos." border="0" /></a>

![](KY-027_LightCup.jpg)
___
## Introducción
El Modulo KY-027 Sensor Magic Cup Light es un sensor que detecta vibraciones o inclinaciones en una superficie por medio de un interruptor de mercurio, entregando una salida digital que activa el regulador PWM y posee un LED que enciende cuando detecta dicha inclinación.

## ¿Para qué sirve?
El Modulo KY-027 Sensor Magic Cup Light son fáciles de desarrollar, los ejemplos mas destacados es para proyectos de nivelación o control de estabilidad; como robot, carros, drones, etc. Este módulo es compatible con Arduino, ESP8266, Raspberry o con cualquier Microcontrolador que posea un pin de 5V.

## ¿Cómo funciona?
Su funcionamiento es como el de un interruptor, ya que tiene dos posiciones de salida: 0 y 1. Está formado por una pequeña cápsula transparente que contiene una bola de mercurio en contacto con dos alambres, que permiten hacer contacto.

## Especificaciones
- Voltaje de alimentación: 3.3 a 5 V
- Tipo de Salida: Digital
- Corriente de salida: 12 mA
- Dimensiones: 20mm x 18mm x 15 mm

**NOTA:** El dispositivo contiene mercurio el cual es altamente toxico, uso delicado.

Para poder conectar el sensor al microcontrolador se necesita tomar en cuenta la siguiente tabla para **conectar una resistencia en el pin del LED**.
| Voltaje | Resistencia |
|---------|-------------|
| 3.3v    | 120 ohms    |
| 5v      | 220 ohms    |

## Asignación de pines
![](Pinout.jpg)

## Diagrama
![](Diagrama.jpg)

## Código
```python
from machine import Pin
import time

Signal_Pin = Pin(20, Pin.IN)
LED_Pin = Pin(21, Pin.OUT)

while True:
    print(Signal_Pin.value())
    LED_Pin.value(Signal_Pin.value())
    time.sleep(0.05)
```

## Conculsión
El sensor puede tener bastante utilidad para proyectos en las que se requiera mantener una posición en un ángulo en concreto, o también puede detectar temblores inusuales debido a como parpadea cuando se pone a temblar.

![](muestra_LightCup.gif)
