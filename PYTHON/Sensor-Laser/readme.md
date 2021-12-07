
![alt text](https://images.cooltext.com/5568073.png)

# Raspberry PI Pico:

El Raspberry Pi Pico es el primer producto con silicio diseñado por la fundación Raspberry Pi (Raspberry Silicon). Esta pequeña tarjeta se presenta como una opción de mayores prestaciones a lo existente en el mercado de los microcontroladores y viene a competir con algunos de los productos ofrecidos por Arduino y fabricantes similares (feather, micro:Bit, etc).

El Raspberry Pi Pico marca el punto de entrada de este fabricante al mercado de la tarjetas con microcontroladores. Esta basado en el chip RP2040 que tiene en su interior dos núcleos ARM cortex M0+ corriendo a una velocidad de 133 Mhz. Posee 264 KB de RAM, mientras que su memoria para almacenar programas (y datos) es de 2 MB y cuenta con 30 pines de GPIO. Se trata de un producto similar a un Arduino Nano, aunque con prestaciones muy superiores.

Hay que aclarar que no se trata de una tarjeta que rivalice de ninguna forma con las computadoras Raspberry Pi (4, Zero, Compute Modules, etc). Sería algo que más bien entra en la arena de los microcontroladores como el Arduino Uno, Nano o MKR. Por lo tanto, no debes verlo como una Raspberry Pi miniatura ni nada por el estilo, pues ese nicho lo cubre desde hace tiempo la Raspberry Pi Zero W.

Con estas características el Raspberry Pi Pico busca posicionarse como una importante alternativa para correr MicroPython y así unirse a otros microcontroladores que han sido sumamente exitosos en el mercado educativo y de hobby. Sin embargo, como ya estamos acostumbrados por este fabricante, la relación de precio / prestaciones es grandiosa.

# ¿Cómo se programa?

La tarjeta viene con dos opciones para programarse:

El SDK de C / C++
El SDK para MicroPython
El Raspberry Pico viene con un bootloader que permite grabar el programa que elaboremos sin la necesidad de un programador especializado. Todo lo que debemos hacer es conectarlo a la PC a través de un cable USB y arrastrar nuestros archivos compilados a una unidad extraible (como si se tratara de una memoria USB).

# Caracteristicas Principales:

| CARACTERÍSTICAS	 | VALORES |
| ------------- | ------------- |
| Microcontrolador  | RP2040 diseñado por Raspberry Pi en Reino Unido, Doble núcleo Cortex M0+ con velocidad de hasta 133 Mhz, Aceleración por hardware de punto flotante |
| Memoria RAM  | 264 KB de SRAM  |
| Memoria Flash  | 2 MB de memoria flash (QSPI)  |
| Conectividad USB  | 	Periférico USB integrado con capacidad de comportarse como HOST o DEVICE  |
| Pines de IO  | 	26 pines de entrada / salida de propósito general  |
| Pines Analógicos  | 	16 pines  |
| Pines PWM  | 		3 canales con 12 bits de resolución  |


# KY-008 Laser Emit

# ¿Qué es Sensor Laser Módulo KY-008?
El Sensor Laser Módulo KY-008 es un emisor de luz láser  de color rojo que cuenta con un cabezal de cobre para darle mayor resistencia y una disipación de calor que se produce por el láser. Ya que no cuenta con un pin de activación por el cual se lleva acabo con el pin de alimentación que envía el pulso de activación mediante el pin de salida de Arduino que suministra 5V.

# ¿Para que sirve el KY-008?
Este módulo es útil para determinar la distancia de un objeto o la detección o alarma de movimiento en caso de ser necesario. Es útil para trabajos con Arduino, Esp8266 ya que es fácil de conectar ; ya que cuenta con 3 pines de los cuales solo se trabaja con 2 (Vcc y GND). El cual tiene un alcance de 1.5m a 2m.

![alt text](https://http2.mlstatic.com/D_NQ_NP_628198-MLM46724374994_072021-O.web)

# Diagrama del Circuito: 👷🏻‍♂️
![alt text](https://github.com/tectijuana/sensores/blob/master/PYTHON/Sensor-Laser/Circuito.PNG?raw=true)

# Conexion de pines
El sensor esta compuesto por 3 pines:

Tierra

Sin conexion

Datos

# Codigo
```python
#  Verificado y corregido por Alvarez Espinoza Raul - 18212141
from machine import Pin
import time

laser = Pin(18, Pin.OUT)

while True:
    laser.value(1)
    time.sleep(0.2)
    laser.value(0)
    time.sleep(0.2)
```

# Conclusion
De este sensor se pueden esperar muchas cosas puesto a que las aplicaciones que pueden involucrar este sensor son bastante variados.


![](demo_laser.gif)
