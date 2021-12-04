## Titulo
![](Titulo.png)

## Logo
<img src="logo.jpg" width="300">

___
## Introducción
El Módulo ky-004 Sensor Push Button detecta una acción al momento de presionarlo, se utiliza para proyectos en donde se necesite una señal externa.

## ¿Para qué sirve?
El Módulo ky-004 Sensor Push Button se utilizan en dispositivos mecánicos y/o electrónicos  para mandar una señal, interruptor o reiniciar un programa.

## ¿Cómo funciona?
El ky-004 su funcionamiento interno consta de 2 contactos, los cuales al ser pulsado uno este activara una función la cual puede ser un NA (normal mente abierto) o NC (normalmente cerrado) dependiendo de las características y la programación.

## ¿Cuáles son las diferencia entre interruptor  y pulsador?
El ky-004 su funcionamiento interno consta de 2 contactos, los cuales al ser pulsado uno este activara una función la cual puede ser un NA (normal mente abierto) o NC (normalmente cerrado) dependiendo de las características y la programación.

#### Un interruptor: 
Tiene la capacidad de abrir un circuito con carga conectada, el interruptor tiene tres posiciones (on) que significa cerrado (off) que significa abierto y uno intermedio que indica falla (puede ser por corto circuito o por sobrecarga).

#### Un pulsador:
Tiene la característica de que solo conducen cuando están presionados a estos se les llama normalmente abiertos y hay otros que dejan de conducir cuando están presionados a estos se les llama normalmente cerrados. Estos tienen la capacidad de interrumpir el paso de una corriente con carga muy pequeña ya que por lo general no provocan arcos eléctricos y cuando controlan grandes cargas están conectados en un arreglo por medio de reveladores ya sean digitales, de estado sólido, o electromagnéticos. Están conectados de modo que la parte del control maneja poca tensión y/o corriente y la parte de fuerza controla una tensión y/o corrientes muy grandes.

## Especificaciones
- Voltaje de Funcionamiento 3.3V – 5V
- Salida Digital: 0 / 1
- Vida de Contacto 100.000 Ciclos
- Pines
- – : GND
- VCC: 5V
- S: Señal

Para poder conectar el sensor al microcontrolador se necesita tomar en cuenta la siguiente tabla para **conectar una resistencia en el pin del LED**.
| Voltaje | Resistencia |
|---------|-------------|
| 3.3v    | 120 ohms    |
| 5v      | 220 ohms    |

## Asignación de pines
![](pines.png)

## Diagrama
<img src="diagrama.png" width="500" height="500">

## Código
