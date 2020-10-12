### Photo resistor module KY-002
![](https://arduinomodules.info/wp-content/uploads/KY-002_vibration_switch_arduino_module.jpg)

El módulo detector de vibración KY-002 consta de un resorte y un poste conductor central con una resistencia de 10K conectada a la alimentación positiva. Ante golpes y vibraciones, el resorte reacciona desplazándose de su centro y cerrando el circuito a tierra. Por esto la salida es inversa: un nivel ALTO significa que no hay detección, y un nivel BAJO que sí existe impacto o vibración.
![](http://robots-argentina.com.ar/didactica/wp-content/uploads/ky-002-interno.png)

*Diagrama de pies*

![](https://tostatronic.com/store/496-large_default/sensor-de-vibracion.jpg)

*Especificaciones*
| Voltaje     | 3.3V-5V     |
|-------------|-------------|
| Dimensiones | 18.5mmx15mm |

*Diagrama*

![](https://1.bp.blogspot.com/-Jg4VM4R5-u4/V8pMmCN5JvI/AAAAAAAAAug/7nyCjT37op4qOfXqG7If4ZwT70u_I6msQCLcB/s1600/KY-002-Vibration-Shock-Sensor-Schematic%2By%2Bfoto.jpg)

*Conexión con Arduino*

![](https://arduinomodules.info/wp-content/uploads/Arduino_KY-002_Keyes_Vibration_switch_module_connection-diagram.png)

*Código* 

```
int sensor = 2; // pin donde se conecta el sensor
 
void setup () {
pinMode (LED_BUILTIN, OUTPUT); // define pin del LED como salida
pinMode (sensor, INPUT); // entrada desde el sensor KY-002
}
void loop () {
digitalWrite (LED_BUILTIN, LOW);
if (digitalRead (sensor) == LOW )  // el sensor entrega un BAJO en una deteccion
{ // cuando el sensor detecta impacto el LED enciende
  digitalWrite(LED_BUILTIN, HIGH); 
  delay(10); // Usted puede probar valores para lograr la indicacion mas conveniente
} 
}
