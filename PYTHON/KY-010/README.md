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

![145525022-07aab8f8-96dd-4a9a-90a8-50a19bfbc34d](https://user-images.githubusercontent.com/89493294/145916088-b745d132-dd31-45a1-9e80-015ccf68440b.png)



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

### `4. Conclusión `
Al buscar información sobre los sensores, nos podemos dar cuenta la variedad que existe en el mercado, y no solo eso, si no que se 
encuentran a nuestros alrededor en diferentes dispositivos que  utilizamos día a día.Al realizar este tipo de practicas, nos ayudan a entender los componentes que tienen, así mismo conocer la manera correcta de  implementarlo, ya sea para poner una idea en practica que ayude a ciertas areas como la medicina o la educacion al crear proyectos que faciliten ciertas tareas, el mundo de los sensores abre grande posibilidades de implementacion, es por eso la importancia de aplicarlos y conocer las bases de programacion para darle forma a la idea y como parte de esta materia los sistemas programablque abarcan muchos areas de programacion y circuitos, y algunas de los materiales como los sensores nos permiten abarcar grandeas areas. 
