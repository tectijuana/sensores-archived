## Hit Sensor.
  
Hit sensor, cuya señal, después de una colisión con algún objeto, pasa a estado alto. Funciona con voltaje de **5 V**. La placa tiene conector de **3 pines**.

![enter image description here](https://botland.com.pl/img/art/inne/14278_3.JPG)

  

### Conexión del Hit Sensor.

El sensor funciona con cualquier microcontrolador con entradas digitales, incluido Arduino. Para leer datos, simplemente conecte la fuente de alimentación y el pin de salida a cualquier entrada del microcontrolador y lea su estado.

![Conexion del sensor al Arduino](https://botland.com.pl/img/art/inne/14278_6.jpg)

### Especificacion del sensor. 

* Voltaje de suministro: 5 V
* Tipo: digital
* Conector de 3 pines
* Dimensiones: 28 x 15 mm
* Peso: 1,5 g
### Ejemplo de experimento. 

**Encender un LED cuando detecte un golpe**

El modulo sensor de golpe debe ser conectado a un circuito muy simple que constara de un LED conectado al PIN 13 del Arduino, el cual, parpadeara en el momento que el modulo detecte un golpe, de lo contrario el LED permanecerá encendido.

**Conexion.**

![enter image description here](https://github.com/tectijuana/sensores/blob/master/HitSensor/hit.png)

    int Led = 5;
    int Shock = 11;
    int val;
    
    void setup(){
    
    pinMode (Led, OUTPUT);
    pinMode (Shock, INPUT);
    
    }
    
    void loop()
    {
    
    val = digitalRead(Shock);
    
    if (val == HIGH){
    
    digitalWrite(Led, LOW);
    
    }
    else{
    
    digitalWrite(Led, HIGH)
    
    }
    
    }

