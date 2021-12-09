![tituloInflerrojo](https://user-images.githubusercontent.com/80190387/144157302-30fff52e-75be-4f3b-b209-13ae3ed568af.png)

  ![KY-005](https://user-images.githubusercontent.com/80190387/144529198-972a4baf-53d5-450d-a260-0d67d1fa7e29.png)

El módulo transmisor de infrarrojos KY-005 consta de solo un LED de infrarrojos de 5 mm. Funciona junto con el módulo receptor de infrarrojos KY-022.

**Caracteristicas y Estructura**

Este sensor es perfectamente compatible con muchas placas de desarrollo como Arduino, Módulo WIFI Esp8266. Este sensor consta de un LED de 5mm al recibir el voltaje apropiado que va de 3.3 a 5Voltios, emite un haz de luz infrarroja de 940 nm en un ángulo de 20 grados. Este sensor consume de 30 a 60 miliamperios de corriente durante su funcionamiento completo. Junto con el LED de infrarrojos, hay algunas resistencias previas integradas en el módulo.
|Voltaje|Coriente|Temperatura|    
|--|--|--|                        
|5V|30-60 mA|-25°C to 80°C|

|Pin S|Pin en medio|Pin -|
|--|--|--|
|Senal|Voltaje|GND|

**Diagrama**

![circuito](https://user-images.githubusercontent.com/80190387/145470044-afb68a51-4dc3-4b71-bb5f-5f7408036408.png)

**Codigo Python**
"""
Palacios Sotelo Ignacio Josafat
L21210894@tectijuana.edu.mx
"""
#Programa para KY-005
import machine
import utime
 
led = machine.Pin(16,machine.Pin.OUT)

while True:
    led.value(1)

