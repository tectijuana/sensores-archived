![1](https://user-images.githubusercontent.com/2523851/143512880-d3d82c2c-cdc0-4f9d-ba33-f2233f813c73.png)
<p align="center">
  ![KY-038 Sensor Microfono 1](https://user-images.githubusercontent.com/89493045/144693229-25d3b7ae-53d7-49a2-8389-6c5b4b6fb1e6.jpg)
</p>
**Sensor: KY-037 Big Sound**
# Información
**¿Qué es el módulo KY-037?**
El Módulo KY-037 Sensor de Sonido  permite detectar cualquier tipo de sonido. Incluye un trimpot con el cual se puede ajusta la sensibilidad del sensor la información de salida puede ser analógica y/o digital.
**¿Para que sirve el sensor micrófono?**
El sensor micrófono es útil para para encender o apagar alguna lampara, para detector de ruido en algún lugar de trabajo u hogar.

**¿Cómo funciona el sensor KY-037?**
Este módulo tiene dos salidas de información:
- Analógica (A0): Lleva toda la información que está detectando el micrófono
- Digital(D0): Obtendremos una salida de encendido o apagado que se activa cuando el sonido supera un cierto volumen. Dicha salida de alta o baja se puede configurar mediante el ajuste del umbral
El sensor tiene 3 componentes principales en su placa de circuito. Primero, la unidad de sensor en la parte frontal del módulo que mide el área físicamente y envía una señal analógica a la segunda unidad, el amplificador. El LM396 amplificará la señal, de acuerdo con el valor resistente del potenciómetro, y envía la señal a la salida analógica del módulo. El tercer componente es un comparador que apaga la salida digital y el LED si la señal cae por debajo de un valor específico.
- Tiene un indicador LED de encendido
- Tiene un LED que indica la salida del comparador

# Ficha Técnica
**ESPECIFICACIONES TÉCNICAS:**
- Modelo: KY-038
- Voltaje de funcionamiento: 5V DC
- Distancia máxima de inducción: 0.5 metros.
- Chip principal: LM393
- Micrófono: Electret
- Gama de frecuencias: 100 – 10.000 Hz.
- Sensibilidad: – 46 ± 2,0, (0dB = 1V / Pa) a 1K Hz.
- La sensibilidad mínima a ruido: 58 dB
- Dimensiones: 36 x 15 x 15 mm
- Peso: 4 g

![KY-038 Sensor Microfono 2](https://user-images.githubusercontent.com/89493045/144693234-335c253d-6ca0-499c-b89c-dc2603838877.jpg)

**El esquema del sensor de latido KY-037 es el siguiente:**
Datased: https://electropeak.com/learn/download/ky-037-datasheet/
