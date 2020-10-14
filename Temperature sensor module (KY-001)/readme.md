![](Temperaturesensormodule.png)

### **¿Qué es?** 

*Módulo de sensor de temperatura Arduino Keyes KY-001, permite la medición de la temperatura ambiente mediante un bus serie digital.*

![](sensortemp.png)


En otras palabras, para evitar que la corriente queme nuestro módulo, el LED se enciende para mostrar si el módulo está funcionando correctamente o no. Ahora, mostraré cómo estos componentes están conectados entre sí. Ahí tenemos el sensor en sí y por supuesto, la luz LED y
Ahí está usted Sir r1 en tercer itube Para ver cómo se conectan los pines de los módulos en esta placa. Entonces, tenemos internet el flujo del voltaje en negro con el flujo de tierra. Y en verde el flujo del letrero de este módulo es suyo para medir la temperatura con un sensor como el Dallas ds 18 b 20, que tiene un rango de temperatura de menos 55 puertas Celsius a más calibre 125 Celsius o menos 67 grados Fahrenheit a 257.

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
