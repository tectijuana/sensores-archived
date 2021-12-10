![](Two_Color_Titulo.png)

![](Two_Color_Portada.jpg)

# MARCO TEÓRICO
### ¿Qué es el LED Bicolor Módulo KY-011?
El LED Bicolor Módulo KY-011 consta de un LED cátodo común que esta conectado a leds  que emite una luz roja y verde, se puede ajustar la intensidad de color usando pulsos de ancho modulado (PWM) y utilizar 2 resistencias 330 Ω para limitar el voltaje y evitar que se dañe el dispositivo.

### ¿Cómo utilizar el Módulo KY-011?
Esté modulo KY-011 led bicolor lo puedes utilizar como luz indicadora en alguno de tus proyectos para mostrar Encendido (verde) y Apagado (rojo), o funcionamiento correcto e incorrecto. Es útil en aparatos como: MP3,  cámaras digitales, audio para automóviles, comunicaciones, computadoras, cargadores, instrumentación, regalos, juguetes electrónicos y teléfonos móviles. Este modulo es muy similar al KY-029.

# DIAGRAMAS
### Conexión
| KY-011 | Tablero | Pi Pico |
|--------|---------|---------|
| -      |         | Pin 38  |
| medio  | 330 Ω   | Pin 27  |
| S      | 330 Ω   | Pin 26  |

*Nota: se recomienda utilizar resistencias de 330 Ω*

![](Diagrama_TwoColor.png)

# TABLAS TÉCNICAS
### Especificación y características
| Propiedad                 | Característica            |
|---------------------------|---------------------------|
| Tipo Led                  | bicolor cátodo común 5 mm |
| Voltaje de funcionamiento | 2 V a 2.5 V               |
| Corriente                 | 10mA                      |
| Angulo de visión          | 150°                      |
| Longitud de onda          | 571nm a 644 nm            |
| Intensidad luminosa       | 20-40 y 40-80 MCD         |
| Color                     | Rojo y Verde              |
| Dimensiones               | 40 mm ,15 mm y 7 mm       |
| Peso                      | 1 gr                      |

### Pines
![](Two_Color_Pines.png)
| Pin del componente | Propiedad |
|--------------------|-----------|
| (-)                | GND       |
| medio              | rojo      |
| S                  | verde     |

# CÓDIGO
```python
#Cuevas Oliva Josue Emanuel 18212164

from machine import Pin
import time

led_pins=[21,20]#Pines de LEDS
leds=[Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT)]#Matriz de control de pines

while True:
    for led in leds:#Iteracion entre cada led
        led.high()#LED Encendido
        time.sleep(0.1)#Tiempo de espera
        led.low()#LED Apagado
        time.sleep(0.1)#Tiempo de espera
```
