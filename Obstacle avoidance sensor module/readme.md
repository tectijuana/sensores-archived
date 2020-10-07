<p align="center">
  <img  src="https://raw.githubusercontent.com/tectijuana/sensores/master/Obstacle%20avoidance%20sensor%20module/sensor_obtaculos_img.png">
</p>
 
El Sensor de obstaculos KY-032 es un modulo que posee la habilidad de detectar obstáculos que se encuentran en su camino, 
su implementación es muy sencilla ya que tiene un rango de detección desde los 2 hasta los 40 cm, se compone de un transmisor y receptor, 
un led indicador, dos resistencias smd, un integrado 74hc00d, un mini jumper puente corto, dos potenciometros de ajuste (uno para determinar el nivel de umbral, 
es decir el valor mínimo de señal que ha de estar presente para detectar y el otro para modificar la frecuencia de emisión del transmisor) 
y un header macho de angulo de 4 pines.

<p align="center">
  <img width="460" height="300" src="https://raw.githubusercontent.com/tectijuana/sensores/master/Obstacle%20avoidance%20sensor%20module/ky-032.png">
</p>

#### ¿Como funciona?
Este sensor funciona con una precisión increíble y mediante el infrarrojo tiene la capacidad de detectar cualquier tipo de obstáculo que se presente. 
Su función básicamente se basa en la captación de luz exterior/ambiental. En su interior posee un par de receptores y transmisores que permiten que este sensor 
funcione perfectamente.

#### ¿para que sirve?
El Sensor de obstaculos ky-032 es un modulo qué tiene la capacidad de detectar obstáculos está diseñado para un aparato con ruedas, 
ya sea un chasis para carro o cualquier otro dispositivo, se recomienda para proyectos en movimiento como seguidores de linea o incluso 
robots minisumos y es compatible con arduino y microcontroladores que los proporcione una alimentación de 5 volts.

#### Especificaciones técnicas
- Voltaje de Trabajo: 3.3 Volts a 5 Volts CD
- Corriente:  ≥ 20 mA
- Temperatura:  -10 ℃   a  50 ℃
- Distancia de Detección:  2  a 40 cm
- Interfaces de entrada/salida:  (- / + / S / EN)
- Ajuste: Gire con un destornillador el trimpot para la sensibilidad que requiera de detección.
- Angulo Efectivo:  35°
- Tamaño: 41 x 18 x 13 mm
- Peso: 6 gr

```javascript

void setup() {
  Serial.begin(9600); // Velocidad de comunicación serial a 9600 baudios
  pinMode(sensor,INPUT); // Se configura sensor como entrada
}

void loop() {
  valor=digitalRead(sensor); // Se lee el valor digital del sensor y se asigna a valor
  if(valor==1){              // Sí el valor es igual a uno se accede a las instrucciones
    Serial.println("NEGRO"); // Se imprime un texto en el monitor serial
  }else if(valor==0){        // Sí el valor es igual a cero se ejecuta la instrucción  
   Serial.println("BLANCO"); // Se imprime blanco en el monitor serial
   }
}
```
