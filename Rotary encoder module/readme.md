<a href="https://cooltext.com"><img src="https://images.cooltext.com/5470638.png" width="1325" height="102" alt="ROTARY ENCODER Module" /></a>
<a href="http://cooltext.com" target="_top"><img src="https://cooltext.com/images/ct_pixel.gif" width="80" height="15" alt="Cool Text: Logo and Graphics Generator" border="0" /></a>


PIC | SENSOR | FUNCIÓN | URL | COLABORADOR
------------ | -------------| -------------| -------------| -------------
![Rotary encoder](https://microjpm.com/_files/200002168-184e5194a4/ky040%20encoder.jpg) | Rotary encoder |  Es un dispositivo de entrada giratorio(como una perilla)que proporciona una indicación de cuánto se ha girado la perilla y en qué dirección está girando. | [Más información](https://circuits4you.com/2016/05/13/rotary-encoder-arduino-ky-040/#:~:text=%20Arduino%20Rotary%20Encoder%20Module%20KY-040%20%201,and%20Z.%20A%20and%20B%20are...%20More%20) | Giezy Martínez De La Cruz

## Descripción

Es un gran dispositivo para el control de paso a paso y servomotor. También se puede utilizar para controlar dispositivos como potenciómetros digitales.

Un codificador giratorio o "eje" es un dispositivo de medición angular. Se utiliza para medir con precisión la rotación de los motores o para crear controladores de rueda (knobs) que pueden girar infinitamente (sin parada final como un potenciómetro tiene). Algunos de ellos también están equipados con un pulsador cuando se pulsa en el eje (como los utilizados para la navegación en muchos controladores de música). Vienen en todo tipo de resoluciones, desde tal vez 16 a por lo menos 1024 pasos por revolución. Los encoders industriales provienen de 1200PPR a 10000PPR (Pulso por revolución).

Los encoders giratorios tienen dos o tres salidas A, B y Z. A y B se utilizan para determinar la dirección de rotación y contar el número de pulsos dará la posición de rotación. Z está disponible en encoders de grado industrial. Es pulso de posición cero. Sólo da un pulso en una revolución.

Un codificador giratorio tiene un número fijo de posiciones por revolución (PPR). El módulo Keyes KY-040 que tengo tiene treinta de estas posiciones. En un lado del interruptor hay tres pines. Normalmente se denominan A(1), B(3) y C(2). En el caso del KY-040,se orientan como se muestra. Dentro del codificador hay dos interruptores. Una vez que el Switch conecta el pin A(1) al pin C(2) y el otro Switch conecta el pin B(3) con C(1).

En cada posición del codificador, ambos interruptores se abren o se cierran. Cada movimiento angular hace que estos interruptores cambien de estado de la siguiente manera:

- Si ambos interruptores están cerrados,girar el codificador en el sentido de las agujas del reloj o en el sentido contrario a las agujas del reloj una posición hará que ambos interruptores se abran
- Si ambos interruptores están abiertos,girar el codificador en el sentido de las agujas del reloj o en el sentido contrario a las agujas del reloj, una posición hará que ambos interruptores se cierren.

## Especificación
 Voltaje | Corriente | Posiciones | Pulso por revolución | Dimensiones 
 ---| ---| ---| ---| ---
 5v| 10mA| 12(cada 30°)| 20| 20 x 30 x 30 mm
 
## Diagrama de conexión
![diagrama](https://circuits4you.com/wp-content/uploads/2016/05/Encoder-Arduino-Circuit.png)

## Código
```c++
#define encoder0PinA  2  //CLK Output A Do not use other pin for clock as we are using interrupt
#define encoder0PinB  4  //DT Output B
#define Switch 5 // Switch connection if available
 
volatile unsigned int encoder0Pos = 0;
 
void setup() { 
 
  pinMode(encoder0PinA, INPUT); 
  digitalWrite(encoder0PinA, HIGH);       // turn on pullup resistor
  pinMode(encoder0PinB, INPUT); 
  digitalWrite(encoder0PinB, HIGH);       // turn on pullup resistor
  attachInterrupt(0, doEncoder, RISING); // encoder pin on interrupt 0 - pin2
  Serial.begin (9600);
  Serial.println("start");                // a personal quirk
} 
 
void loop(){
// do some stuff here - the joy of interrupts is that they take care of themselves
  Serial.print("Position:");
  Serial.println (encoder0Pos, DEC);  //Angle = (360 / Encoder_Resolution) * encoder0Pos
}
 
void doEncoder() {
  if (digitalRead(encoder0PinB)==HIGH) {
    encoder0Pos++;
  } else {
    encoder0Pos--;
  }
}
```

