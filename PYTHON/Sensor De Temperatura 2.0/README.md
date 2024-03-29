#  Sensor De Temperatura 

## ¿Qué son los sensores de temperatura?

*Los sensores de temperatura son componentes eléctricos y electrónicos que, en calidad de sensores, permiten medir la temperatura mediante una señal eléctrica determinada. Dicha señal puede enviarse directamente o mediante el cambio de la resistencia. También se denominan sensores de calor o termosensores. Un sensor de temperatura se usa, entre otras aplicaciones, para el control de circuitos. Los sensores de temperatura también se llaman sensores de calor, detectores de calor o sondas térmicas.*

[![img-0019.jpg](https://i.postimg.cc/ZRMhpRqs/img-0019.jpg)](https://postimg.cc/hzTwqKTV)

## Historia

*El primer sensor de temperatura reglado de la historia se atribuye a Daniel Gabriel Fahrenheit, y tenía una forma muy similar a la que se ha conservado hasta hace muy poco. Tras probar varios materiales (el I+D de la época), se decantó en 1714 por un termómetro de vidrio con mercurio en su interior.*

*Durante más de un siglo, los termómetros fueron mejorando gracias a distintos científicos, generalmente franceses. Y colocados allí donde podían o les dejaban. Hasta el momento en que las primeras pruebas de radio llamaron la atención de estos científicos, que se preguntaron si merecía la pena conocer la temperatura de un punto alejado.*

[![Christin-1743.jpg](https://i.postimg.cc/Z5vtzZV6/Christin-1743.jpg)](https://postimg.cc/HrmPQGGL)

[![fahrenheit.jpg](https://i.postimg.cc/5NjD8bcD/fahrenheit.jpg)](https://postimg.cc/hfWCBFt0)

## ¿Qué materiales detecta un sensor de temperatura?

*La detección del material depende del tipo y diseño del sensor de temperatura. Esto es especialmente válido para sensores de temperatura que muestran el cambio de temperatura mediante el cambio de otra magnitud o propiedad física.*

[![bills-of-materials.jpg](https://i.postimg.cc/vm8Bv4QG/bills-of-materials.jpg)](https://postimg.cc/68StW52P)

## Tipos

*Existen muchas clasificaciones, sin embargo una de las más usadas es la que clasifica a este tipo de sensores en seis categorías, estas son:*

1. Sensores de temperatura termopar
2. Dispositivos de temperatura resistivos RTD y termistores
3. Dispositivos bimetálicos
4. Dispositivos de dilatación de líquido
5. Radiadores infrarrojos
6. Dispositivos de cambio de estado

[![tipos-contratos-trabajo.png](https://i.postimg.cc/g2JQqpff/tipos-contratos-trabajo.png)](https://postimg.cc/Cz3cS3MN)

## Esquemas

*Las siguientes imagenes son esquemas de sensores de temperatura.*

[![termoregul.png](https://i.postimg.cc/gchZj6j7/termoregul.png)](https://postimg.cc/Wt23fzMm)

[![arduino-LM35-esquema-electrico.png](https://i.postimg.cc/Cxr1mFdD/arduino-LM35-esquema-electrico.png)](https://postimg.cc/BjD4vfTQ)

[![ECT-02.jpg](https://i.postimg.cc/FK2KXDyH/ECT-02.jpg)](https://postimg.cc/gwHpvytC)

## Especificaciones y caracteristicas

[![Screenshot-8.png](https://i.postimg.cc/WpZ5VzvN/Screenshot-8.png)](https://postimg.cc/K4ZPrZjw)

## Diagrama

*El siguiente proyecto se realizo en la pagina Tinkerkad, donde se tratara de realizar e implementar usar el sensor de temperatura TMP36, tratando de compilarlo a la mano de un led, donde este se prendera si la temperatura del TMP36 es alta.*

Componentes para el proyecto:

1. Sensor De Temperatura TMP36
2. Componente Led
3. Placa De Protobot De Pruebas
4. Ardurino Uno R3

[![Screenshot-9.png](https://i.postimg.cc/3NgXMkzd/Screenshot-9.png)](https://postimg.cc/Wq1Fg1Nv)

## Codigo De Diagrama

```
int LED = 7;
int TMP = 0;
float temperatura = 0;

void setup()
{
 	pinMode(LED, OUTPUT); 
}

void loop()
{
	temperatura = map(analogRead(TMP),0,1023,-50,450);


	if (temperatura>= 25)
	{
  		digitalWrite(LED,HIGH);
	}

	else
	{
  		digitalWrite(LED,LOW);
	}
  
  	delay (10);
	
}		
```


## Diagrama Final Con Resultados

[![Screenshot-13.png](https://i.postimg.cc/26qdGkYX/Screenshot-13.png)](https://postimg.cc/tZjVCHYh)

[![Screenshot-14.png](https://i.postimg.cc/WzGkYtHS/Screenshot-14.png)](https://postimg.cc/rRpsKyct)
[![Screenshot-15.png](https://i.postimg.cc/8zP6wpBB/Screenshot-15.png)](https://postimg.cc/2VMySftV)

## Conclusiones 

Como vimos se logro exitosamente el uso del sensor de temperatura TMP36 al asiganerle las variables correctas para que este junto con el led, se lograra prender si este superaba la temperatura superada para que este se activara. 

## Fuentes Apa

- Carlos Pardo. (Noviembre 2021). Sensor de temperatura. 10 de diciembre del 2021, de Picuino Sitio web: https://www.picuino.com/es/control-sensor-temp.html
- NA. (2021). Sensor de temperatura con su propio diagrama. Esquema de termostato simple y confiable para la incubadora. Gestión de temperatura casera: instrucción paso a paso Источник: https://newtravelers.ru/es/asus/datchik-temperatury-svoimi-rukami-shema-prostaya-i-nad-zhnaya-shema.html. 10 de diciembre del 2021 , de newtravelers.ru Sitio web: https://newtravelers.ru/es/asus/datchik-temperatury-svoimi-rukami-shema-prostaya-i-nad-zhnaya-shema.html
- MARCOS MARTÍNEZ. (23 de agosto del 2021). ¿Sabes cuál fue el primer sensor conectado de la historia?. 10 de diciembre del 2021, de Nobbot Sitio web: https://www.nobbot.com/general/primer-sensor-conectado/
- NA. (NA). El sensor de temperatura. 3 de diciembre del 2021, de Rechner Sensors Sitio web: https://www.rechner-sensors.com/es/documentacion/knowledge/el-sensor-de-temperatura

