<img src="https://user-images.githubusercontent.com/89493086/144327109-e6fa03f3-6435-4feb-bc4b-98c8dfa7fb2c.png" alt="Titulo" style="height: 118px; width:764px;"/>
<img src="https://arduinomodules.info/wp-content/uploads/KY-031_fritzing_custom_part_image-149x240.png" alt="KY-031" style="height: 150px; width:100px;"/>

El sensor **KY-031 Tap Module** es un sensor de vibración que envía una señal cuando se detecta un golpe.

Es compatible con Arduino, ESP8266, ESP32, Teensy, Raspberry Pi y otras plataformas populares. 

## **Especificaciones**
Este módulo consta de una resistencia de 10 kΩ y un sensor de resorte que envía una señal alta cuando se detecta una vibración. 

| **Voltage de operacion** | 3.3 a 5V |
|----------------------|----------|
| **Output Type**          | Digital  |

<img src="https://raw.githubusercontent.com/tectijuana/sensores/master/PYTHON/KY-031%20Tap%20Module/imagenes/Modulo-KY-031.png" alt="KY-031" style="height: 769px; width:773px;"/>

## Como configurarlo
| Raspberry Pi | Sensor |
|--------------|--------|
| Pin 18       | Señal  |
| Pin 1        | +V     |
| Pin 6        | GND    |
<img src="https://raw.githubusercontent.com/tectijuana/sensores/master/PYTHON/KY-031%20Tap%20Module/imagenes/2021-12-02%2019_57_16-Untitled%20Sketch.fzz_%20-%20Fritzing%20-%20%5BBreadboard%20View%5D.png" alt="KY-031" style="height: 300px; width:500px;"/>

## Codigo

```import RPi. GPIO  as  GPIO
import time
   
GPIO.setmode (GPIO.BCM) 
   
GPIO_PIN = 24
GPIO.setup (GPIO_PIN, GPIO.IN) 
   
print ("Sensor test [press CTRL+C to exit the test]")
   

def outputFunction(null) :
    print("Signal detected")
   
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback= outputFunction ,  bouncetime=100)  
   
try:
    while True:
        time.sleep (1) 
   
except KeyboardInterrupt:
    GPIO.cleanup ()
```
## Como ejecutarlo
```sudo python3 KY031-RPi.py
```

    
