![Cool Text - Heartbeat](https://user-images.githubusercontent.com/84552885/144182471-1ec67c0d-5d3b-406d-b996-ce061eb44e61.png)

![Sensor](https://user-images.githubusercontent.com/84552885/144518236-99b46ddd-8424-484c-a571-a5388afdd4f6.jpg)



## Sensor: KY-039 Heartbeat

# Marco teórico

### ¿Qué es el Detector de Ritmo Cardíaco? 💓

El Detector de Ritmo Cardíaco KY-039 es un sensor óptico de pulsos cardíacos por medio de la huella digital utiliza un LED infrarrojo brillante (IR) y un fototransistor para detectar el pulso del dedo, un LED rojo flashea con cada pulso.

Es un dispositivo de “Plug and Play”, puede ser utilizado para obtener fácilmente una lectura del ritmo cardíaco en tiempo real. 

### ¿Para que funciona el KY-039? 🤔
El KY-039 es una alternativa económica para medir el ritmo cardiaco y es compatible con diversas tarjetas de desarrollo como Arduino, Raspberry, ESP82, entre otras.


### ¿Cómo funciona el sensor de pulso cardíaco? 👷🏻‍♂️
El monitor de pulso funciona de la siguiente manera: el LED es el lado luminoso del dedo y el fototransistor del otro lado del dedo, el fototransistor utilizado para obtener el flujo emitido, cuando la presión sanguínea pulsa con el dedo cuando la resistencia del fototransistor ser ligeramente cambiado.

Cuando el pulso de la presión arterial pasa por el dedo la corriente de la base del fototransistor se modifica ligeramente, debido a que la cantidad de luz que puede atravesar el dedo disminuye, lo que significa una salida por el puerto análogo diferente.

Es muy importante tener en cuenta que es prioritario que se mantenga lo más alejado de la luz parásita, es decir de la luz externa por ejemplo la iluminación del hogar, por eso se recomienda usar algún sistema que sirva de escudo al fototransistor y que evite que otra luz diferente a la del led llegue ya que la señal del latido del corazón es muy débil y la luz ambiente añadirá un ruido considerable.


# Ficha técnica

![especificaciones2](https://user-images.githubusercontent.com/84552885/144528044-c6614b33-9539-4ea0-94e0-90f8653f49fa.png)

### ESPECIFICACIONES TÉCNICAS. 🛠️
- Modelo: KY-039
- Voltaje: 3.3V a 5 V
- Tipo de Salida: Analógica
- Peso: 4 g
- Dimensiones: 25mm x 12mm x 12 mm


Este modulo tiene tres pins: GND, Vcc+ y Signal. El pinout es el siguiente:
![pinout](https://user-images.githubusercontent.com/84552885/144520684-b4e05b62-5744-4e6f-b4cc-1fb168c87ea8.jpg)


El esquema del sensor de latido KY-039 es el siguiente:

![esquema](https://user-images.githubusercontent.com/84552885/144524203-ce1c1c5a-6114-4392-82a1-ada1da1588a7.jpg)

https://www.thegeekpub.com/wp-content/uploads/2019/07/KY-039-heartbeat-sensor-schematic.jpg


## Modo de conexión 

| Pico   | KY-039 Heartbeat |
|--------|------------------|
| Pin 38 | GND              |
| Pin 36 | 3.3V a 5V        |
| Pin 26 | Señal analógica  |

# Diagrama
![HeartBeat_Diagrama](https://user-images.githubusercontent.com/84546168/145541310-a8a9903b-befe-4087-9bcb-ebca30a859d4.png)


_**El diagrama fue realizado en Fritzing, no encontré la librería para el sensor. Encontré uno similar y le coloque etiquetas para identificar cada parte**_

## Sensor y salidas: 
![especificaciones](https://user-images.githubusercontent.com/84552885/144535290-da95c082-2b38-4ca0-ba67-40b458e6e175.jpg)

# Código


```python
# Aquino Villegas Daniel 18212144
# No logré que arroje valor


import machine
import time

factor = 0.75
maximo = 0.0
minimoEntreLatidos = 300
valorAnterior = 500
valorverdadero = 0

sensor = machine.ADC(27)

print('iniciando mediciones')

while True:
    valorticks = time.ticks_ms()
    valorverdadero =  valorverdadero + (time.ticks_ms() - (valorticks - 1))
    
    
    tiempoLPM = valorverdadero
    entreLatidos = valorverdadero
    
    valorLeido = sensor.read_u16()
    
    valorFiltrado = factor * valorAnterior + (1 - factor) * valorLeido
    cambio = valorFiltrado - valorAnterior
    
    valorAnterior = valorFiltrado
    

     
    if((cambio >= maximo) & (valorverdadero > entreLatidos + minimoEntreLatidos)):
        maximo = cambio
        entreLatidos = valorverdadero
        latidos = latidos + 1

    
    
    maximo = maximo *0.97
    
    if (valorverdadero >= tiempoLPM + 15000):
        print('Latidos por minuto: ')
        print(latidos * 4)
        latidos = 0;
        tiempoLMP = valorverdadero
        
    time.sleep_ms(50)
