<a href="https://cooltext.com"><img src="https://images.cooltext.com/5470134.png" width="773" height="75" alt="MAGIC LIGHT CUP MODULE" /></a>
<br />Image by <a href="https://cooltext.com">Cool Text: Free Graphics Generator</a> - <a href="https://cooltext.com/Edit-Logo?LogoID=3647584375">Edit Image</a>

### **¿Qué es?** 
*El módulo Keyes Kingduino Compatible Magic Cup Light Modules (KY-027) contiene en su placa un LED indicador, resistencia 103 smd, un header macho de 4 pines de angulo y un interruptor de mercurio en ella.*

### **¿Cómo funciona?**
*El interruptor de mercurio encenderá o apagara el LED dependiendo de su posición real a horizontal. **El siguiente video muestra el uso del magic light cup con Arduino:**



[![Como Usar magic light cup con Arduino](http://img.youtube.com/vi/PT-30OaJF-M/0.jpg)](http://www.youtube.com/watch?v=pCK6prSq8aw)

### **Especificaciones Técnicas Y Características**
+ *Voltaje de alimentación: 3.3 a 5 volts*
+ *Corriente de salida: 12 mA*
+ *Salida: Digital*
+ *Dimensiones: 20 x 18 x 15 mm*
+ *Peso: 1.83 gr*
+ *4 pines*

### **Conexión de los pines del módulo** ###
![Sensor](https://github.com/aris-dev/Sensores/blob/main/MAGIC%20LIGHT%20CUP%20%20MODULE/m3.PNG "Sensor")

| Pin |       Modulo       |
|:---:|:------------------:|
|  G  |    GND (Tierra)    |
|  V+ | Positivo (5 volts) |
|  S  |    Señal Digital   |
|  L  |         LED        |

### **Ejemplo De Código De Sensor:** ####
```
int ledPinA = 9;
int switchPinA = 8;
int switchStateA = 0;
int ledPinB = 6;
int switchPinB = 7;
int switchStateB = 0;
int brightness = 0;

void setup()
{
pinMode(ledPinA, OUTPUT);
pinMode(ledPinB, OUTPUT);
pinMode(switchPinA, INPUT);
pinMode(switchPinB, INPUT);
}
void loop()
{
switchStateA = digitalRead(switchPinA);
if (switchStateA == HIGH && brightness != 255)
{
brightness ++;
}
switchStateB = digitalRead(switchPinB);
if (switchStateB == HIGH && brightness != 0)
{
brightness --;
}
analogueWrite(ledPinA, brightness); // A slow fade out
analogueWrite(ledPinB, 255 - brightness); // B slow bright up
delay(20);
```

