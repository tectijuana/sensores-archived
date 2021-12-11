![Cool Text - KY-018 Modulo fotoresistor 399893486965218](https://user-images.githubusercontent.com/89375469/145665863-7e52fb6a-bebb-489b-8f23-149d44421ea7.png)

# MODULO FOTO RESISTOR

Se explica la teoría para entender el funcionamiento y realizar pruebas con el módulo fotorresistor y la adquisición de datos por medio de un Raspberry pie Pico, el diagrama, y código para su uso.

## Marco teórico.
### Modulo Fotorresistor
![image](https://user-images.githubusercontent.com/89375469/144342999-5d83180b-d8aa-4e65-96d7-d7aa7ccf9a5f.png)

El módulo KY-018 es un dispositivo electrónico foto-resistor que cuya resistencia depende de la intensidad de luz, a mayor cantidad de luz menor resistencia presentara; por lo cual puede determinar la presencia o ausencia de luz.

El Sensor Foto Resistor por lo regular se utiliza en lamparas suburbanas que se encuentran en las calles y fotoceldas eléctricas para controlar de manera automática el encendido y apagado de las luminarias.

### Raspberry pie Pico
![image](https://user-images.githubusercontent.com/89375469/144343041-0982f436-9ed6-4513-beea-362750d99587.png)

## Diagramas y tablas técnicas.

![image](https://user-images.githubusercontent.com/89375469/145665638-0e0c3a28-3d88-4902-9330-3a788368166e.png)


## Código
En seguida se muestr el codigo que tambien se encuentra en el repositorio en el siguiente enlace https://github.com/tectijuana/sensores/blob/master/PYTHON/KY-018/KY-018ejemplo.py

```import RPi.GPIO as GPIO
import time
from gpiozero import MCP3008

led = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,False)

try: 
	while True:
		adc = MCP3008(channel=0)
		voltage = 3.3 * adc.value
		print("Measured voltage is ",voltage);
		time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()```
    
## Ejecución o comprobación.
