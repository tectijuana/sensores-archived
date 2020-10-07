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

### Ejemplo.

    int Led = 13 ; // definir interfaz LED
    int Shock = 3 //   definir la interfaz del sensor de percusión
    int val ; // definir variables numéricas val
     
    void setup ()
    {
      pinMode (Led, OUTPUT) ; // definir LED como interfaz de salida
      
      pinMode (Shock, INPUT) ; // definir la interfaz de salida del sensor de golpe.
    }
    void loop ()
    {
      val = digitalRead (Shock) ; // a la interfaz digital de lectura se le asigna un valor de 3 val
      
      if (val == HIGH) // When the percussion when the sensor detects a signal, LED flashes

      {
        digitalWrite (Led, LOW);
      }
      else
      {
        digitalWrite (Led, HIGH);
      }
    }

