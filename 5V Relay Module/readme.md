![](5Vrelaymodulo.png)


![](modulo.png)


### **Cómo utilizar un rel** ###
Los relés son los dispositivos de conmutación más utilizados en electrónica.

Antes de continuar con el circuito para impulsar el relé, debemos considerar dos parámetros importantes del relé. Una vez que es el voltaje de disparo , este es el voltaje requerido para encender el relé que debe cambiar el contacto de Común-> NC a Común-> NO. Nuestro relé aquí tiene un voltaje de activación de 5 V, pero también puede encontrar relés de valores de 3 V, 6 V e incluso 12 V, así que seleccione uno según el voltaje disponible en su proyecto. El otro parámetro es su Voltaje y Corriente de Carga , esta es la cantidad de voltaje o corriente que el terminal NC, NO o Común del relé podría soportar, en nuestro caso para DC es máximo de 30V y 10A. Asegúrese de que la carga que está usando esté dentro de este rango.

![](modulo2.png)

### **Aplicaciones de la retransmisión**

+ De uso común en circuitos de conmutación.
+ Para proyectos de domótica para cambiar cargas de CA
+ Para controlar (encendido / apagado) cargas pesadas en un tiempo / condición predeterminados
+ Se utiliza en circuitos de seguridad para desconectar la carga del suministro en caso de falla
+ Se utiliza en la electrónica de automóviles para controlar indicadores de motores de vidrio, etc.

EXAMPLE SENSOR CODE:

``` 
int relay = 10; //Pin 10
void setup()
{
pinMode(relay,OUTPUT);
the port attribute as output
}
void loop()
{
digitalWrite(relay,HIGH);
relay ON
// [NO] is connected to feed
// [NC] is not connected to feed
delay(1000);
// turn the
// Define
digitalWrite(relay,LOW);
// turn
the relay OFF
// [NO] is not connected to feed
// [NC] is connected to feed
delay(1000);
``` 
