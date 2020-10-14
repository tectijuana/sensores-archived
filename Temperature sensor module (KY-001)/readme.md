![](Temperaturesensormodule.png)

### **¿Qué es?** 

*Módulo de sensor de temperatura Arduino Keyes KY-001, permite la medición de la temperatura ambiente mediante un bus serie digital.*

![](sensortemp.png)

### **¿Como Funciona?** 

Este sensor funciona para evitar que la corriente queme nuestro módulo, el LED se enciende para mostrar si el módulo está funcionando correctamente o no. 

### **Especificaciones**

El módulo de sensor de temperatura KY-001 consta de un sensor de temperatura digital de bus único DS18B20, un LED y una resistencia. Compatible con plataformas electrónicas populares como Arduino, Raspberry Pi y Esp8266.

|    Tensión de funcionamiento    |       3,0 V a 5,5 V      |
|:---------:|:------------------:|
|  Rango de medición de la temperatura  |    -55°C a 125°C (-57 ° F a 257 ° F)   |
|  Rango de precisión de medición | 0,5°C |
| Dimensiones |  18,5 mm x 15 mm [0,728 pulgadas x 0,591 pulgadas]              |

![](senstemp2.png)

EXAMPLE SENSOR CODE:

```
#include <OneWire.h> 
#include <DallasTemperature.h> 

// Data wire is plugged into pin 2 on the Arduino #define ONE_WIRE_BUS 2 

// Setup a oneWire instance to communicate with any OneWire devices (not just Maxim/Dallas temperature ICs) 

OneWire oneWire(ONE_WIRE_BUS); 

// Pass our oneWire reference to Dallas Temperature. DallasTemperature sensors(&oneWire); 

void setup(void) 

{ 
// start serial port
Serial.begin(9600); 
Serial.println("Dallas Temperature IC Control Library Demo"); // Start up the library 
sensors.begin(); // IC Default 9 bit. If you have troubles consider upping it 12. Ups the delay giving the IC more time to process the temperature measurement 
} 
void loop(void) 
{ 
// call sensors.requestTemperatures() to issue a global temperature // request to all devices on the bus 
Serial.print("Requesting temperatures..."); 
sensors.requestTemperatures(); // Send the command to get temperatures 
Serial.println("DONE"); 
Serial.print("Temperature for Device 1 is: "); 
Serial.print(sensors.getTempCByIndex(0)); // Why "byIndex"? You can have more than one IC on the same bus. 0 refers to the first IC on the wire 
```
