<a href="https://cooltext.com"><img src="https://images.cooltext.com/5470391.png" width="1474" height="144" alt=" infrared emission sensor module" /></a>
<a href="https://cooltext.com"></a> - <a href="https://cooltext.com/Edit-Logo?LogoID=3648424343"></a>

 <a> <img width="250px" src="https://images-na.ssl-images-amazon.com/images/I/51oJojQm%2B9L._SL1000_.jpg" /> </a>
 
 **Especificaciones**
El módulo transmisor de infrarrojos KY-005 consta de solo un LED IR de 5 mm. Funciona junto con el módulo receptor de infrarrojos KY-022 . Compatible con plataformas electrónicas populares como Arduino, Teensy, Raspberry Pi y ESP8266.

| Requerimientos                 |    |
|--------------------------------|----|
| Tensión de funcionamiento      | 5V | 
| Corriente directa              | 30 ~ 60 mA | 
| El consumo de energía          | 90 mW | 
| Temperatura de funcionamiento	 | -25 ° C a 80 ° C [-13 ° F a 176 ° F] |
| Dimensiones                    | 18,5 mm x 15 mm [0,728 pulgadas x 0,591 pulgadas] |

**Diagrama de conexión KY-005**
Conecte la línea de alimentación (medio) y tierra (-) a +5 y GND respectivamente. 
Conecte la señal (S) al pin 3 del Arduino UNO o al pin 9 del Arduino Mega. 
El número de pin para el transmisor de infrarrojos lo determina la biblioteca de IRremote, 
consulte la sección de descargas a continuación para obtener más información.

<a><div align="center"><img width="550px" src="https://arduinomodules.info/wp-content/uploads/Arduino_KY-005_Keyes_Infrared_transmitter_module_connection_diagram.png" /> </a></div>
<a><div align="center"><img width="550px" src="https://www.gadgetronicx.com/wp-content/uploads/2015/07/infra-red-module.jpg" /> </a></div>

| KY-005                 |  Arduino UNO |
|------------------------|--------------|
| S                      | Pin 3 | 
| medio	                 | + 5V  |
| -	                     | GND   |


**CODIGO EJEMPO KY-005**
El siguiente boceto de Arduino utiliza la biblioteca IRremote para enviar señales infrarrojas en serie con el KY-005. 
El pin de salida lo determina la biblioteca y depende de la placa que esté utilizando, 
consulte la documentación de la biblioteca de IRremote para conocer las placas compatibles. 
Necesitará un receptor de infrarrojos como el KY-022 para procesar la señal.
Los enlaces a las bibliotecas requeridas para el boceto de ejemplo KY-005 Arduino se pueden encontrar en la sección de Descargas a continuación.

<br>#include <IRremote.h></br>
<br>IRsend irsend;</br>

<br>void setup()</br>
<br>{</br>
 <br>Serial.begin(9600);</br>
<br>}</br>

<br>void loop() </br>
<br>{</br>
   <br>for (int i = 0; i < 50; i++) { </br>
    <br> irsend.sendSony(0xa90, 12); // Sony TV power code</br>
     <br>delay(40);</br>
  <br> }</br>
<br>}</br>

