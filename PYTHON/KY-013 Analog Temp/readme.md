![cooltext399090049365437](https://user-images.githubusercontent.com/71294551/144157675-1cb85862-a237-4af1-8699-ecfd6762fe82.png)
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

![Sensor](https://user-images.githubusercontent.com/71294551/145511988-fb180ace-ab6e-4efe-9954-7b126754df2b.png)

- El esquema de conexión de este sensor es el siguiente:
- 
![Esquematico](https://user-images.githubusercontent.com/71294551/145515771-5ec93c31-e70d-43c0-8ee6-c9577216b42d.png)

### Diagrama de conexión

El siguiente diagrama de conexión es de un thermistor el cual necesita una resistencia de valor de 10k ohms
Los correspondientes pines en la Pi Pico son:
- Pin # 28 Tierra
- Pin # 40 VSUS (3.3 V)
- Pin # 26 para la lectura analoga

![Diagrama](https://user-images.githubusercontent.com/71294551/145515787-1905f23e-53ab-4ec8-b655-ab51098c179e.png)

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
