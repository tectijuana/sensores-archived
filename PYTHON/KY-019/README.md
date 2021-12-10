# Módulo KY-019 Sensor Relevador 5V



 ![](https://camo.githubusercontent.com/1bec201eaf92bd376e98e5eae6c87141b121b065685619e9f16c2ba7692178c5/68747470733a2f2f656e637279707465642d74626e302e677374617469632e636f6d2f696d616765733f713d74626e3a414e6439476351495f354a744d465f574d66644d765963717956326a4f7a632d32766b4a57594463446726757371703d434155)


# Marco Teorico

## Descripción

El módulo de relé Arduino KY-019 se utiliza para controlar los circuitos de AC, el relé actúa como un interruptor que responde a una señal recibida del Arduino, tiene un LED integrado que indica si la señal es alta o baja.

Comúnmente utilizado en proyectos de control y automatización para controlar luces y otros dispositivos electrónicos.

El KY-019 consiste en una resistencia de 1MΩ, un LED, un diodo rectificador 1N4007 y un relé de 5VDC capaz de manejar hasta 250VAC y 10A.

En el lado de CC de la placa hay 3 pines para señal, potencia y tierra. En el lado de CA hay 3 contactos, NC (normalmente cerrado), común y NO (normalmente abierto).

> ESPECIFICACIONES TÉCNICAS

- Señal de control TTL 5VDC a 12VDC (algunas tarjetas pueden funcionar con 3.3)
- Máxima CA 10A 250VAC
- Máximo DC 10A 30VDC
- Tipo de contacto NC y NO
- Dimensiones 27 mm x 34 mm [1.063in x 1.338in]
- Peso: 14g

Conexión de los pines KY-019 Para la parte de CC del circuito, conecte los pines al arduino de acuerdo a su diagrama.
En el lado de CA, conecte su alimentación a Common (contacto medio) y use NC o NO de acuerdo con sus necesidades.
Siempre tenga mucho cuidado al experimentar con CA, la descarga eléctrica puede provocar lesiones graves.

![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUOChJz_aLg-cot9QD4uiYCU2TbwwKdMcNWQ&usqp=CAU)

# Tablas Técnicas

> ESPECIFICACIONES Y CARACTERISTICAS 

TTL Control Signal | 5VDC to 12VDC (some boards may work with 3.3)
-- | --
Maximum AC | 10A 250VAC
Maximum DC | 10A 30VDC
Contact Type | NC and NO
Board Dimensions | 27mm x 34mm [1.063in x 1.338in]

# Diagrama

## Hoja de conexiones Raspberry pi pico
![](https://raw.githubusercontent.com/tectijuana/sensores/master/PYTHON/KY-019/Screen%20Shot%202021-12-09%20at%2021.18.19.png)

## Diagrama de conexión
![](https://raw.githubusercontent.com/tectijuana/sensores/master/PYTHON/KY-019/Screen%20Shot%202021-12-09%20at%2021.17.08.png)
