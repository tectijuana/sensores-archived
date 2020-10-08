
## Sensor Touch.

Interruptor sensible al tacto. Tocar el sensor producirá una salida en el pin ‘DO’ La salida no es una señal limpia pero incluye señales inducidas de 50 Hz (‘mains hum’). La señal se salida es "Alto activo" y la sensibilidad del circuito se pueden ajustar con un potenciómetro. En el pin ‘AO’ se encuentra disponible una señal analógica de salida.


![enter image description here](https://i2.wp.com/www.drouiz.com/wp-content/uploads/2016/03/sensor-capacitivo-arduino.jpg?resize=300,300&ssl=1)

### Características del Sensor Touch Analógico.

El sensor detecta cuando se le toca con la mano (o cualquier parte del cuerpo) generalmente este sensor detecta una determinada capacidad al pulsarlo nuestro cuerpo crea un efecto capacitivo sobre tierra suficiente para que el sensor salte a estado alto.

### Diagrama del cableado

### Ejemplo de programación de sensor touch.

**Encender LED con tocar el sensor.**

![enter image description here](https://i2.wp.com/www.drouiz.com/wp-content/uploads/2016/03/touch-sensor-4.png)

El programa es realmente sencillo simplemente se va a encender un LED al pulsar sobre el sensor, este dispositivo es un pulsador es decir solo funciona mientras se pulsa a diferencia de un interruptor que permanece en un estado.

### Código.



    //PULSADOR TOUCH SENSOR CON LED PARA ARDUINO*
    
    int pinLED = 13;
    int pinTouch = 8;
    
    void setup() {
    pinMode(pinLED,OUTPUT);
    pinMode(pinTouch,INPUT);
    }
    void loop() {
    
    digitalWrite(pinLED, digitalRead(pinTouch));
    
    }
