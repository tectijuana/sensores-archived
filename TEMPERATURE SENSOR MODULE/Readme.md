<a href="https://cooltext.com"><img src="https://images.cooltext.com/5470346.png" width="1029" height="97" alt="KY-028 TEMPERATURE SENSOR MODULE" /></a>
<br />Image by <a href="https://cooltext.com">Cool Text: Free Graphics Generator</a> - <a href="https://cooltext.com/Edit-Logo?LogoID=3648324763">Edit Image</a>

### **¿Qué es?** 
*El Modulo KY-028 Sensor Temperatura Digital los permite medir la temperatura a través de un termistor  NTC, en el cual el proceso de acondicionamiento de los datos le permitirá al sensor adecuar una señal de trabajo operable. Esta construido de un termistor NTC, un comparador lm393, seis resistencias smd, dos led indicadores, un trimput y un header macho de angulo 4 pines.*

### **¿Cómo funciona?**
*El sensor temperatura (KY-028) tiene 3 componentes principales en su placa de circuito. Primero, la unidad del sensor en la parte frontal del módulo que mide el área físicamente y envía una señal analógica a la segunda unidad, el amplificador. El amplificador amplifica la señal, de acuerdo con el valor resistente del potenciómetro, y envía la señal a la salida analógica del módulo. **El siguiente video muestra el uso del Modulo KY-028 Sensor de Temperatura Digital con Arduino:**



[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID_HERE)

### **Especificaciones Técnicas Y Características**
+ *Salida analógica: medición directa de la unidad de sensor*
+ *LED1: muestra que el sensor está recibiendo energía*
+ *LED2: muestra que el sensor a detectado un campo magnetico*
+ *Rango de temperatura: -55 °C / + 125 °C*
+ *Voltaje de funcionamiento: 3.3 Volts a  5 Volts*
+ *Dimensiones: 38 x 15 x 14 mm*
+ *Peso: 3 gr*

### **Conexión de los pines del módulo** ###
![Sensor](https://github.com/aris-dev/Sensores/blob/main/TEMPERATURE%20SENSOR%20MODULE/t1.PNG "Sensor")

|    Pin    |       Modulo       |
|:---------:|:------------------:|
|  [Pin 3]  |    Señal Digital   |
|  [Pin 5V] | Positivo (5 volts) |
| [Pin GND] |         GND        |
|  [Pin 0]  |    Señal Analoga   |

### **Ejemplo De Código De Sensor:** ####
```
int led = 13; // define the LED pin
int digitalPin = 2; // KY-028 digital interface
int analoguePin = A0; // KY-028 analogue interface
int digitalVal; // digital readings
int analogueVal; //analogue readings
void setup()
{
pinMode(led, OUTPUT);
pinMode(digitalPin, INPUT);
//pinMode(analoguePin, OUTPUT);
Serial.begin(9600);
}
void loop()
{
// Read the digital interface
digitalVal = digitalRead(digitalPin);
if(digitalVal == HIGH) // if temperature threshold reached
{
digitalWrite(led, HIGH); // turn ON Arduino's LED
}
else
{
digitalWrite(led, LOW); // turn OFF Arduino's LED
}
// Read the analogue interface
analogueVal = analogueRead(analoguePin);
Serial.println(analogueVal); // print analogue value to serial
delay(100);
```

