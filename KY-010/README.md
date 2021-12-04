![titulo-removebg-preview (1)](https://user-images.githubusercontent.com/89493294/144682432-e709be06-c991-48fb-a8c5-4205b8295e32.png)

### `1. Marco Teórico`
El módulo KY-010  consta de un emisor / detector óptico en la parte frontal y dos resistencias (1 kΩ y 33 Ω) en la parte posterior. 
Es un fotosensor que combina dos partes las cuales son transmisión y de recepción en un módulo, ya que de un lado tiene el emisor y por el otro extremo tiene un rector que recibe la señal y cuando se interrumpe la luz infrarroja esta manda una señal al microcontrolador. 

> ¿Para qué es?

Se utilizan para detectar la velocidad de un giro de un motor con un una lamida también puede detectar cualquier objeto que interrumpa la luz infrarroja se puede utilizar para el cierre de una puerta con una sencilla programación y para algunos desplazamientos de máquinas.

> ¿Cómo Funciona?

El sensor ky-010 es un dispositivo electrónico que responde cuando se interrumpe la luz infrarroja el cual se manda al microcontrolador la señal se emplean en algunas aplicaciones como pueden ser en la automatización de oficinas, árcades, detección de objetos en general.

![KY-010](https://user-images.githubusercontent.com/89493294/144683140-520dd8b6-3899-4c82-9bc9-454340db3150.jpg)

### `2. Diagrama`

![pi-and-ky-010-layout](https://user-images.githubusercontent.com/89493294/144686932-a7214c04-93d0-4a5b-bdfa-f63ba80bb3b4.jpg)



> Especificaciones Técnicas.

- Voltaje de funcionamiento 3.3 ~ 5V.
- Dimensiones 18.5mm x 15mm [0.728in x 0.591in]

> Diagrama de conexión KY-010.

![pi-and-ky-010-schematic](https://user-images.githubusercontent.com/89493294/144686912-9e4286bc-89e5-4e97-93c5-85b3a3b58184.jpg)


> Conexiones.

| KY-010    	| Rasperry        	|
|-----------	|-----------------	|
| (-)       	| (Izquierda) GND 	|
| Pin medio 	| + 5V            	|
| (S)       	| (Derecha) Pin 3 	|


### `3. Codigo`
codigo.py
