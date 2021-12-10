![](images/Logo.png)
## Sensor de Temperatura analogo

-El componente MF52-103 es un sensor análogo de temperatura que normalmente es utilizado en equipos de aire acondicionado, equipos de calefacción, equipos médicos, instrumentación de control de temperatura, higrómetro electrónico, calendario electrónico de temperatura de la automoción, la batería recargable y cargador, batería del ordenador portátil


|Especificaciones|
|:----|
|Modelo: MF52-103|
|Material aislante: Ceramica|
|Color: Negor|
|Potencia nominal: 0.05W|
|Valor de resistencia: 10k|
|Tolerancia de resistencia: H (Â±3%)|
|Valor B: 3950K|

![](images/Sensor.png)

- El esquema de conexión de este sensor es el siguiente:
- 
![](images/Esquema.png)

### Diagrama de conexión

El siguiente diagrama de conexión es de un thermistor el cual necesita una resistencia de valor de 10k ohms
Los correspondientes pines en la Pi Pico son:
- Pin # 28 Tierra
- Pin # 40 VSUS (3.3 V)
- Pin # 26 para la lectura analoga

![](images/Diagram.png)

# Código

```python
# Avila Jimenez David Alfredo
# Se necesita testear el código

import machine
from utime import sleep

def main():
    sensor_temperatura = machine.ADC(26)
    factor_16 = 3.3 / (65535)
    
    while True:
        voltaje = sensor_temperatura.read_u16() * factor_16
        temperatura = 27 - (voltaje - 0.706)/0.001721
        print(temperatura)
        sleep(2)

if __name__ == '__main__':
    main()
