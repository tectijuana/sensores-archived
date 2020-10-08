![cooltext364929103794232](https://user-images.githubusercontent.com/60414166/95504881-41c7f300-0962-11eb-9812-fe92544fa46c.png)
<a href="http://cooltext.com" target="_top"><img src="https://cooltext.com/images/ct_pixel.gif" width="80" height="15" alt="Cool Text: Logo and Graphics Generator" border="0" /></a>

![D_NQ_NP_713002-MLM29041738595_122018-O](https://user-images.githubusercontent.com/60414166/95505212-da5e7300-0962-11eb-828b-6f86dac00fcc.jpg)

**INFORMACIÓN**
El DHT11 es un sensor digital de temperatura y humedad relativa de bajo costo y fácil uso. Integra un sensor capacitivo de humedad y un termistor para medir el aire circundante, y muestra los datos mediante una señal digital en el pin de datos (no posee salida analógica). Utilizado en aplicaciones académicas relacionadas al control automático de temperatura, aire acondicionado, monitoreo ambiental en agricultura y más.

Utilizar el sensor DHT11 con las plataformas Arduino/Raspberry Pi/Nodemcu es muy sencillo tanto a nivel de software como hardware. A nivel de software se dispone de librerías para Arduino con soporte para el protocolo "Single bus". En cuanto al hardware, solo es necesario conectar el pin VCC de alimentación a 3-5V, el pin GND a Tierra (0V) y el pin de datos a un pin digital en nuestro Arduino. Si se desea conectar varios sensores DHT11 a un mismo Arduino, cada sensor debe tener su propio pin de datos. Quizá la única desventaja del sensor es que sólo se puede obtener nuevos datos cada 2 segundos. Cada sensor es calibrado en fabrica para obtener unos coeficientes de calibración grabados en su memoria OTP, asegurando alta estabilidad y fiabilidad a lo largo del tiempo. El protocolo de comunicación entre el sensor y el microcontrolador emplea un único hilo o cable, la distancia máxima recomendable de longitud de cable es de 20m., de preferencia utilizar cable apantallado. Proteger el sensor de la luz directa del sol (radiación UV).

En comparación con el DHT22 y DHT21, este sensor es menos preciso, menos exacto y funciona en un rango más pequeño de temperatura / humedad, pero su empaque es más pequeño y de menor costo.

![temperature-humidity-arduino-chiosz1](https://user-images.githubusercontent.com/60414166/95505601-75efe380-0963-11eb-8ee0-cad13febe8c0.jpg)

**Especificaciones Técnicas**
| Voltaje de Operación                 |   3V-5V DC   |
|--------------------------------------|:------------:|
|   Rango de medición de temperatura   |   0 - 50 °C  |
| Precisión de medición de temperatura |    ±2.0 °C   |
|     Rango de medición de humedad     | 20% - 90% RH |
|   Precisión de medición de humedad   |     5% RH    |
|         Resolución de humedad        |     1% RH    |
|           Tiempo de sensado          |    1 seg.    |
|                Modelo                |     DTH11    |
|              Dimensiones             |  16*12*5 mm  |
|                 Peso                 |     1 gr.    |

***Código***
```java
		
#define DHTPIN 2 // Indicamos el pin del arduino donde conectamos el sensor
 
byte bGlobalErr;  //para pasar el codigo de error de vuelta de las funciones
byte DHTDAT[5];  //Array para almacenar los bytes enviados por el sensor
int maxh=0,minh=100,maxt=0,mint=100,t,h; //variables para ir guardando las maximas de
// humedad y temperatura y las minimas de humedad y temperatura
 
void setup()
{
  InitDHT();  // Inicializamos el pin empleado para leer el sensor
  Serial.begin(9600);  //Iniciamos comunicacion serie con el pc para ver los datos leidos
  Serial.println("Test sensor DHT11:");
  delay(1000);  //Este delay es para esperar el tiempo recomendado para acceder al sensor (1 segundo) 
}
 
void loop()
{
  ReadDHT(); // Leemos el sensor y almacenamos el resultados en variables globales
  switch (bGlobalErr)
  {
     case 0:
        //Como en este sensor la humedad y la temperatura no nos sale con decimales, 
        //podemos desechar los bytes 1 y 3 de la lectura del sensor
        h=DHTDAT[0];
        t=DHTDAT[2];
    Serial.print("Humedad relativa: ");
    Serial.print(h);
    Serial.print(" %\t");
    Serial.print("Temperatura: ");
    Serial.print(t);
    Serial.println("*C");
        //Comprobacion de maximos y minimos de humedad y temperatura
        if (maxh<h)
          maxh=h;
        if (h<minh)
          minh=h;
        if (maxt<t)
          maxt=t;
        if (t<mint)
          mint=t;
        Serial.print("Max: ");
        Serial.print(maxh);
        Serial.print(" % ");
        Serial.print("Min: ");
        Serial.print(minh);
        Serial.print(" %\t");
        Serial.print("Max: ");
        Serial.print(maxt);
        Serial.print(" *C ");
        Serial.print("Min: ");
        Serial.print(mint);
        Serial.println(" *C\n");
        break;
     case 1:
        Serial.println("Error 1: Condicion de start 1 no conocida.");
        break;
     case 2:
        Serial.println("Error 2: Condicion de start 2 no conocida.");
        break;
     case 3:
        Serial.println("Error 3: DHT checksum error.");
        break;
     default:
        Serial.println("Error: Encontrado codigo irreconocible.");
        break;
  }
  delay(1000);// Esperamos 1 segundo para la siguiente lectura
}
 
 
// Initilize pin for reading
void InitDHT(){
        pinMode(DHTPIN,OUTPUT);
        digitalWrite(DHTPIN,HIGH);
}
 
void ReadDHT(){
  bGlobalErr=0;
  byte dht_in;
  byte i;
  // Enviamos el comando "start read and report" al sensor
  // Primero: ponemos a "0" el pin durante 18ms
  digitalWrite(DHTPIN,LOW);
  delay(18);
  delay(5);//TKB, frm Quine at Arduino forum
  //Segundo: ponemos a "1" el pin durante 40us,enviamos el comando de "start read" al sensor
  digitalWrite(DHTPIN,HIGH);
  delayMicroseconds(40);
  //Tercero: Cambiamos el pin de Arduino a entrada de datos
  pinMode(DHTPIN,INPUT);
  delayMicroseconds(40); //Esperamos 40 us
  dht_in=digitalRead(DHTPIN);
  //si hay un 1 en la lectura del pin, indicamos que hay error de tipo 1
  if(dht_in)
  {
    bGlobalErr=1;
    return;
  }
  delayMicroseconds(80); //Esperamos 80us
  dht_in=digitalRead(DHTPIN); 
  //si no hay un 1 en la lectura del pin, indicamos que hay error de tipo 2
  if(!dht_in){
    bGlobalErr=2;
    return;
  }
  /*Despues de 40us a nivel bajo, el pin deberia de estar durante 80us a nivel alto.
  Despues de esto comienza el envio del primer bit hasta alcanzar los 40 bits enviados.
  The routine "read_dht_dat()" expects to be called with the system already into this low.*/
  delayMicroseconds(80); //Esperamos 80us
  //Ahora comienza la recepcion de datos, son 5 bytes de datos, es decir 40 bits, almacenamos en un array de 5 bytes
  for (i=0; i<5; i++)
    DHTDAT[i] = read_dht_dat();
  //Cuarto: Volvemos a configurar el pin del arduino como salida
  pinMode(DHTPIN,OUTPUT);
  //Quinto:Ponemos a "1" el pin de salida
  digitalWrite(DHTPIN,HIGH);
  //Comprobamos si los datos recibidos coinciden con el checksum recibido
  byte DHTCHECKSUM = DHTDAT[0]+DHTDAT[1]+DHTDAT[2]+DHTDAT[3];
  //Si no coincide el byte recibido de checksum con la suma de los 4 primeros bytes enviamos error tipo 3
  if(DHTDAT[4]!= DHTCHECKSUM)
    bGlobalErr=3;
  };
 
byte read_dht_dat()
{
  //Cogemos 8 de los bits recibidos y los devolvemos como un byte.
  //Si por ejemplo recibimos 00000100 , devolvemos en decimal 4
  byte i = 0;
  byte result=0;
  for(i=0; i< 8; i++)
  {
    //Entramos mientras dura el primer bit de start (a nivel bajo durante 50us) del byte
    //Esperamos hasta que el pin se pone a nivel alto señalizando fin del la transmision del bit de start
    while(digitalRead(DHTPIN)==LOW);
    //La linea de datos debera estar ahora a nivel alto durante 27 o 70us, 
    //dependiendo si un "0" o un "1" esta siendo enviado respectivamente
    delayMicroseconds(30);  //Esperamos 30 us
    if (digitalRead(DHTPIN)==HIGH)
      result |=(1<<(7-i));  //Si despues de los 30us el pin permanece a "1" añadimos un 1 al byte, sino queda un "0" 
    //Esperamos hasta que el pin se vuelve a poner a nivel bajo,
    // el cual indica la señal de start del siguiente bit de la transmision
    while (digitalRead(DHTPIN)==HIGH);
  }
  return result; //devolvemos el resultado
}
		
```
