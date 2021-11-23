### Optical broken module
![](https://416w7b49llop13pkg72rweoc-wpengine.netdna-ssl.com/wp-content/uploads/modulo-ky-010-sensor-foto-interruptor-cdmx-electronica-D_NQ_NP_917506-MLM27963288634_082018-O.jpg)

El módulo de interruptores de fotos Keyes KY-010 para Arduino activará una señal cuando la luz entre el espacio del sensor esté bloqueada.
El módulo KY-010 Photo Interrupter consta de un emisor / detector óptico en la parte frontal y dos resistencias (1 kΩ y 33 Ω) en la parte posterior. El sensor usa un haz de luz entre el emisor y un detector para verificar si el camino entre ambos está siendo bloqueado por un objeto opaco.

*Diagrama de pines*
![](https://www.cdmxelectronica.com/wp-content/uploads/KY-010.png)

*Especificaciones*
| Voltaje        | 3.3V-5V     |
|----------------|-------------|
| Dimensiones    | 18.5mmx15mm |
| Salida de dato | (0/1)       |
| Peso           | 2g          |

*Diagrama*

![](https://lh3.googleusercontent.com/proxy/3s0b_rEoMEm8g5qlpEpGWfyPr_9u2dSKBGcOrSC44m1DeBfiBad2FPt7DAT06i5ZomJELbvZyHFrnxJdnd8w4i4Cb_duFq5BjRUifhSkEp6SrJ_WxzkNWEGgJv7xCB2FVoi5)

*Conexión con Arduino*

![](https://arduinomodules.info/wp-content/uploads/Arduino_KY-010_Keyes_Photo_interrupter_module_connection-diagram.png)

*Código* 

```
int Led = 13; // definir pin LED
int buttonpin = 3; //definir pin de señal de fotointerruptor
int val; //definir una variable numérica

void setup()
{
	pinMode(Led, OUTPUT); // Pin LED como salida
	pinMode(buttonpin, INPUT); //pin del interruptor de la foto como entrada
}

void loop()
{
	val=digitalRead(buttonpin); //leer el valor del sensor
	if(val == HIGH) // enciende el LED cuando el sensor está bloqueado
	{
		digitalWrite(Led,HIGH);
	}
	else
	{
		digitalWrite(Led,LOW);
	}
}
