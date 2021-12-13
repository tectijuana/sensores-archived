# KY-035 ANALOG HALL

![](https://uelectronics.com/wp-content/uploads/2017/06/AR0052-Sensor-KY-035-Sensor-Magnetico-Analogico-v3.jpg)


# MARCO TEÓRICO

> ¿Qué es el KY-035 sensor magnético? 

El KY-035 es un módulo que integra un sensor magnético de Efecto Hall con salida analógica, el cual permite detectar de forma fácil, rápida y precisa campos magnéticos producidos cerca de sensor.

> ¿Para qué sirve el KY-035 sensor magnético?

Es muy útil en proyectos de electrónica, robótica y automatización ya que tiene una amplia gama de aplicaciones, como poder ser un excelente sensor de posición sin contacto, un contador de ciclos, es muy común verlos en aplicaciones como velocímetros sobre todo en bicicletas, etc.

## ESPECIFICACIONES Y CARACTERÍSTICAS
- Voltaje de alimentación: 3.3V a 5 V DC
- Consumo de energía: 8 mA
- Tipo de Salida: Analógica, Lineal
- Rango de detección: 650 – 1000 Gauss
- Temperatura: -40°C a 85 °C
- Dimensiones: 18mm x 15mm x 6 mm
- Peso: 1 g

![](https://uelectronics.com/wp-content/uploads/2017/06/KY035-V3.jpg)


# TABLAS TÉCNICAS


## Información técnica

Chipset | AH49E
-- | --
A low-noise output makes filtering practically superfluous |  
Reacts to positive and negative Gauss (Gauss is the unit in which Magnetic Force is measured.) |  
Measuring range | -40 °C to 85 ° C
Electricity consumption | 3.5mA at 5V




RASPBERRY PI | SENSOR
-- | --
KY-053 A0 | Signal
3.3V [Pin 1 ] | +V
Mass [ Pin 6 ] | GND


# DIAGRAMA
![](https://github.com/tectijuana/sensores/blob/master/PYTHON/KY-035/images/Screen%20Shot%202021-12-13%20at%202.31.53.png?raw=true)

# CÓDIGO



---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

```python

# inicio del programa del sensor mágnetico

# ! /usr/bin/python
#  coding = utf-8

import time
import board
import busio
import  adafruit_ads1x15.ads1115 as  ADS
from  adafruit_ads1x15.analog_in import AnalogIn

#  Create the I2C bus
i2c  =  busio. I2C (board. SCL, board. SDA)

#  Create the  ADC object  using the  I2C  bus
ads  =  ADS.ADS1115(i2c)
voltageMax  =  3.3
#  Create single-ended input on channels
chan0  =  AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 =  AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)


while True:
    resistance  =  chan0.voltage / (voltageMax – chan0.voltage)   *  10 000

    print (“Voltage value: “,'%.2f'  % chan0.voltage”,V, resistance:  ",'%.2f' % resistance,  "ÃŽÂ©" )
    print("---------------------------------------------------")
    time.sleep(1)


# brychxpin was here

```

## COMO EJECUTAR 
``` sudo python3 main.py ```


