# KY-025 Reed Switch
<img src="https://uelectronics.com/wp-content/uploads/2017/06/AR0043-Sensor-KY-025-v5.jpg" width="250">

### ¿Qué es Sensor KY-025 Reed Switch?

_El KY-025 Reed Switch Module es un pequeño interruptor eléctrico operado por un campo magnético aplicado, comúnmente utilizado como sensor de proximidad._
_El módulo tiene salidas digitales y analógicas._
_Se utiliza un recortador para calibrar la sensibilidad del sensor._
_Compatible con Arduino, Raspberry Pi, ESP32 y otros microcontroladores._


### Especificaciones

| Voltaje de funcionamiento       | 3.3V a 5.5V             |
|---------------------------------|-------------------------|
| Dimensiones                     | 1.5cm x 3.6cm           |
| Salidas                         | Analógica y digital     |
|Sensor magnético                 | Alta sensibilidad       |
|Comparador de salida de corriente| 16 mA                   |
|Peso                             | 3 g                     |


### Material para testing

  - Tarjeta arduino 
  - KY-025 Reed Swtich
  - 4 wires(Conectores)

### Conexion de pines

  - Pin A0 (KY-025) a pin A0 (Arduino)
  - G (KY-025) a GND (Arduino)
  - (+) (KY-025) a +5V (Arduino)
  - D0 (KY-025) a Pin 3 (Arduino)

<img src="image_2021-12-07_194950.png" width="500">


### Codigo

```
//Revisado por Daniel Garcia - 18212185
//No tendran la version con un Raspberry Pico?


int led = 13; // define the LED pin
int digitalPin = 3; // KY-025 digital interface
int analogPin = A0; // KY-025 analog interface
int digitalVal; // digital readings
int analogVal; //analog readings

void setup()
{
  pinMode(led, OUTPUT);
  pinMode(digitalPin, INPUT);
  //pinMode(analogPin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  // Read the digital interface
  digitalVal = digitalRead(digitalPin); 
  if(digitalVal == HIGH) // if magnetic field is detected
  {
    digitalWrite(led, HIGH); // turn ON Arduino's LED
  }
  else
  {
    digitalWrite(led, LOW); // turn OFF Arduino's LED
  }

  // Read the analog interface
  analogVal = analogRead(analogPin); 
  Serial.println(analogVal); // print analog value to serial

  delay(100);
}

```
