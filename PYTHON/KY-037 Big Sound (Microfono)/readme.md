<p align="center"><img src="https://user-images.githubusercontent.com/2523851/143512880-d3d82c2c-cdc0-4f9d-ba33-f2233f813c73.png"> </p>
  
<p align="center"><img width="460" height="300" src="KY-038 Sensor Microfono 1.jpg"></p>

**Sensor: KY-037 Big Sound**

# Información

**¿Qué es el módulo KY-037?**
El Módulo KY-037 Sensor de Sonido  permite detectar cualquier tipo de sonido. Incluye un trimpot con el cual se puede ajusta la sensibilidad del sensor la información de salida puede ser analógica y/o digital.

**¿Para que sirve el sensor micrófono?**
El sensor micrófono es útil para para encender o apagar alguna lampara, para detector de ruido en algún lugar de trabajo u hogar.

**¿Cómo funciona el sensor KY-037?**
Este módulo tiene dos salidas de información:
- Analógica(A0): Lleva toda la información que está detectando el micrófono
- Digital(D0): Obtendremos una salida de encendido o apagado que se activa cuando el sonido supera un cierto volumen. Dicha salida de alta o baja se puede configurar mediante el ajuste del umbral
El sensor tiene 3 componentes principales en su placa de circuito. Primero, la unidad de sensor en la parte frontal del módulo que mide el área físicamente y envía una señal analógica a la segunda unidad, el amplificador. El LM396 amplificará la señal, de acuerdo con el valor resistente del potenciómetro, y envía la señal a la salida analógica del módulo. El tercer componente es un comparador que apaga la salida digital y el LED si la señal cae por debajo de un valor específico.
- Tiene un indicador LED de encendido
- Tiene un LED que indica la salida del comparador

<p align="center"><img src="KY-038 Sensor Microfono 2.jpg"></p>

Datased: https://electropeak.com/learn/download/ky-037-datasheet/

# Características

Los sensores de sonido KY-038 y KY-037 son muy similares, ya que ambos cuentan con un micrófono para la detección de sonidos, la única diferencia es la sensibilidad que tiene cada uno.

<p align="center"><img src="KY-038 Sensor Microfono 4.PNG"></p>

El ajuste de la sensibilidad es a través de **trimpot**, siendo que en forma horaria aumenta la sensibilidad y de lado contrario se reduce.

</p> <p align="center"><img src="KY-038 Sensor Microfono 5.jpg"></p>

**ESPECIFICACIONES TÉCNICAS:**
- Modelo: KY-038
- Voltaje de funcionamiento: 5V DC
- Distancia máxima de inducción: 0.5 metros.
- Chip principal: LM393
- Micrófono: Electret
- Gama de frecuencias: 100 – 10.000 Hz.
- Sensibilidad: – 46 ± 2,0, (0dB = 1V / Pa) a 1K Hz.
- La sensibilidad mínima a ruido: 58 dB
- Dimensiones: 36 x 15 x 15 mm
- Peso: 4 g


## Materiales para testing
- RaspBerry pi
- KY-037 Big Sound Sensor
- 2x wires (Conectores)

## Diagrama de conexión al protoboard

<p align="center"><img src="KY-038 Sensor Microfono 2.jpg"></p>

Conexiones Raspberry Pi:
- Señal Digital(D0) = GPIO 24 [Pin 18 (RPi)]
- +V = 3,3V [Pin 1 (RPi)]
- GND = GND [Pin 06 (RPi)]
- Señal Analógica(A0) = Analog 0 [Pin A0 (ADS1115 - KY-053)]

## Código
```
from Adafruit_ADS1x15 import ADS1x15
from time import sleep

import math, signal, sys, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# initialise variables
delayTime = 0.5 # in Sekunden
# assigning the ADS1x15 ADC
ADS1015 = 0x00 # 12-bit ADC
ADS1115 = 0x01 # 16-bit

# choosing the amplifing gain
gain = 4096 # +/- 4.096V
# gain = 2048 # +/- 2.048V
# gain = 1024 # +/- 1.024V
# gain = 512 # +/- 0.512V
# gain = 256 # +/- 0.256V
# choosing the sampling rate
# sps = 8 # 8 Samples per second
# sps = 16 # 16 Samples per second
# sps = 32 # 32 Samples per second
sps = 64 # 64 Samples per second
# sps = 128 # 128 Samples per second
# sps = 250 # 250 Samples per second
# sps = 475 # 475 Samples per second
# sps = 860 # 860 Samples per second
# assigning the ADC-Channel (1-4)
adc_channel_0 = 0 # Channel 0
adc_channel_1 = 1 # Channel 1
adc_channel_2 = 2 # Channel 2
adc_channel_3 = 3 # Channel 3
# initialise ADC (ADS1115)
adc = ADS1x15(ic=ADS1115)
# Input pin for the digital signal will be picked here
Digital_PIN = 24
GPIO.setup(Digital_PIN, GPIO.IN, pull_up_down = GPIO.PUD_OFF)
#############################################################################################################

# loop principal

# The program reads the current value of the input pin
# and shows it at the terminal
try:
 while True:
 #Current values will be recorded
 analog = adc.readADCSingleEnded(adc_channel_0, gain, sps)
 # Output at the terminal
 if GPIO.input(Digital_PIN) == False:
 print "Analog voltage value:", analog,"mV, ","extreme value: not reached"
 else:
 print "Analog voltage value:", analog, "mV, ", "extreme value: reached"
 print "---------------------------------------"
 sleep(delayTime)
 
except KeyboardInterrupt:
 GPIO.cleanup()

```

## Ejecucion
pi@raspberrypi~ python KY-037_microfono.py
