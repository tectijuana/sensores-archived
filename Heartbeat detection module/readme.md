<p align="center">
  <img  src="https://raw.githubusercontent.com/tectijuana/sensores/master/Heartbeat%20detection%20module/sensor_cardiaco_img.png">
</p>

El sensor de ritmo cardíaco es un dispositivo de “plug and play”, puede ser utilizado para obtener fácilmente una lectura del ritmo cardíaco en tiempo real. 
Una de las ventajas de este tipo de dispositivos es que el software es de código abierto lo que permite obtener gráficamente el 
ritmo cardíaco en tiempo real mediante Processing si se está utilizando la tarjeta Arduino.

<p align="center">
  <img width="460" height="300" src="https://raw.githubusercontent.com/tectijuana/sensores/master/Heartbeat%20detection%20module/Sensor%20KY-039.webp">
</p>

#### ¿Como Funciona?
El sensor funciona con un sensor de ritmo cardíaco óptico, donde tiene una etapa de amplificación y un filtro para el ruido, 
lo cual hace que su señal de salida sea confiable y estable. El consumo de corriente es bajo siendo de 4mA con una alimentación de 5V.

Está basado en un LED emisor y un sensor receptor de intensidad, la cantidad de luz reflejada por el dedo cuando hay paso de corriente sanguínea define 
la salida del sensor. Por lo que es posible visualizar gráficamente o numéricamente la información del mismo.

*El monitor de pulso funciona de la siguiente manera:*

El LED es el lado luminoso del dedo y el fototransistor del otro lado del dedo, 
el fototransistor utilizado para obtener el flujo emitido, cuando la presión sanguínea pulsa con el dedo cuando la resistencia del 
fototransistor ser ligeramente cambiado.

Cuando el pulso de la presión arterial pasa por el dedo la corriente de la base del fototransistor se modifica ligeramente, d
ebido a que la cantidad de luz que puede atravesar el dedo disminuye, lo que significa una salida por el puerto análogo diferente.

Es muy importante tener en cuenta que es prioritario que se mantenga lo más alejado de la luz parásita, es decir de la luz externa 
por ejemplo la iluminación del hogar, por eso se recomienda usar algún sistema que sirva de escudo al fototransistor y que evite que 
otra luz diferente a la del led llegue ya que la señal del latido del corazón es muy débil y la luz ambiente añadirá un ruido considerable.

#### Especificaciones técnicas

- Modelo: KY-039
- Voltaje: 3.3 a 5 V DC
- Salida: Analógica
- Pasador de sensor “S” conectado a pin Arduino Analog 0 / A0
- El pin del sensor + (pin central) se conecta al pin 5+ de Arduino
- Pasador de sensor: conecte al pin GND de Arduino
- Peso: 4 gr
- Dimensiones: 25 x 12 x 12 mm


#### Diagrama de conección
<p align="center">
  <img src="https://raw.githubusercontent.com/tectijuana/sensores/master/Heartbeat%20detection%20module/ky-039.jpg">
</p>

#### Código de prueba

```javascript
 
int senal = A0 ;  //Conectar en el pin analogico A0 
int valor;


void setup()
{
  Serial.begin(9600);  //Activar puerto serial
}

void loop()
{
  valor = analogRead(senal);  //Lectura señal anañogica
  if(valor >= 30 && 50 >= valor){
      Serial.println("No hay pulso"); 
  }
  else{
       Serial.println("Hay pulso");
  }
}
```

