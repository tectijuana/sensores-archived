# ¿Qué es MQTT?
MQTT (Message Queuing Telemetry Transport), es un protocolo de mensajería ligero de publicación/suscripción diseñado para telemetría M2M (máquina a máquina) en entornos de bajo ancho de banda. Está basado en la pila TCP/IP como base para la comunicación. En el caso de MQTT cada conexión se mantiene abierta y se "reutiliza" en cada comunicación. Es una diferencia, por ejemplo, a una petición HTTP 1.0 donde cada transmisión se realiza a través de conexión. MQTT es un protocolo controlado por eventos, donde no hay transmisión de datos periódica o continua. Así se mantiene el volumen de transmisión al mínimo. Un cliente sólo publica cuando hay información para enviar, y un bróker sólo envía información a los suscriptores cuando llegan nuevos datos.

Fue diseñado por Andy Stanford-Clark (IBM) y Arlen Nipper en 1999 para conectar sistemas de telemetría de oleoductos por satélite. Fue estandarizado como código abierto por medio de la organización para el avance de estándares de información estructurada (OASIS) en 2010 y se convirtió en un estándar OASIS en 2014.

# ¿CÓMO FUNCIONA EL MQTT?
Una sesión MQTT se divide en cuatro etapas: conexión, autenticación, comunicación y terminación. Un cliente comienza creando una conexión de Protocolo de Control de Transmisión/Protocolo de Internet (TCP/IP) con el broker utilizando un puerto estándar o un puerto personalizado definido por los operadores del broker. Al crear la conexión, es importante reconocer que el servidor puede continuar una sesión antigua si se le proporciona una identidad de cliente reutilizada.

Los puertos estándar son 1883 para la comunicación no cifrada y 8883 para la comunicación cifrada – usando Secure Sockets Layer (SSL)/Transport Layer Security (TLS). Durante la conexión SSL/TLS, el cliente valida el certificado del servidor y autentica el servidor. El cliente también puede proporcionar un certificado de cliente al agente durante el apretón de manos. El agente puede utilizarlo para autenticar al cliente. Aunque no es específicamente parte de la especificación MQTT, se ha convertido en una costumbre que los agentes soportan la autenticación de clientes con certificados SSL/TLS del lado del cliente.

Debido a que el protocolo MQTT tiene como objetivo ser un protocolo para dispositivos con recursos limitados y dispositivos de IO, SSL/TLS puede no ser siempre una opción y, en algunos casos, puede no ser deseado. En tales ocasiones, la autenticación se presenta como un nombre de usuario y una contraseña en texto claro, que son enviados por el cliente al servidor — esto, como parte de la secuencia de paquetes CONNECT/CONNNACK. Además, algunos brokers, especialmente los brokers abiertos publicados en Internet, aceptarán clientes anónimos. En estos casos, el nombre de usuario y la contraseña simplemente se dejan en blanco.

MQTT se llama un protocolo ligero porque todos sus mensajes tienen una pequeña huella de código. Cada mensaje consiste en un encabezado fijo — 2 bytes — un encabezado variable opcional, una carga útil del mensaje que está limitada a 256 megabytes (MB) de información y un nivel de calidad de servicio (QoS).

Durante la fase de comunicación, un cliente puede realizar operaciones de publicación, suscripción, desinscripción y ping. La operación de publicación envía un bloque binario de datos (el contenido) a un tema definido por el editor.

Ejemplo
Los clientes inician una conexión TCP/IP con el broker, el cual mantiene un registro de los clientes conectados. Esta conexión se mantiene abierta hasta que el cliente la finaliza. Por defecto, MQTT emplea el puerto 1883 y el 8883 cuando funciona sobre TLS.

Para ello el cliente envía un mensaje CONNECT que contiene información necesaria (nombre de usuario, contraseña, client-id…). El broker responde con un mensaje CONNACK, que contiene el resultado de la conexión (aceptada, rechazada, etc).

Para enviar los mensajes el cliente emplea mensajes PUBLISH, que contienen el topic y el payload.

Para suscribirse o desuscribirse se emplean mensajes SUBSCRIBE y UNSUSCRIBE, que el servidor responde con SUBACK y UNSUBACK.

Por otro lado, para asegurar que la conexión está activa los clientes mandan periódicamente un mensaje PINGREQ que es respondido por el servidor con un PINGRESP. Finalmente, el cliente se desconecta enviando un mensaje de DISCONNECT.

Estructura de un mensaje MQTT
Uno de los componentes más importantes del protocolo MQTT es la definición y tipología de los mensajes, ya que son una de las bases de la agilidad en la que radica su fortaleza. Cada mensaje consta de 3 partes:

Cabecera fija. Ocupa 2 a 5 bytes, obligatorio. Consta de un código de control, que identifica el tipo de mensaje enviado, y de la longitud del mensaje. La longitud se codifica en 1 a 4 bytes, de los cuales se emplean los 7 primeros bits, y el último es un bit de continuidad. Cabecera variable. Opcional, contiene información adicional que es necesaria en ciertos mensajes o situaciones. Contenido(payload). Es el contenido real del mensaje. Puede tener un máximo de 256 Mb aunque en implementaciones reales el máximo es de 2 a 4 kB.

Los tipos de mensajes y códigos de control que se envían en el protocolo MQTT son los siguientes.

Aplicacion del protocolo de mensajeria
MQTT es el protocolo líder para conectarse a dispositivos de IoT, superando a HTTP, un pilar en el dominio de Internet en 2017. Es más, MQTT fue elegido como el protocolo de mensajería para las plataformas de IoT para Amazon, Microsoft y, por supuesto, IBM, así como muchos productos de open-source y demás productos de agentes comerciales. La Plataforma de IoT Watson de IBM ofrece no solo una conectividad segura a escala masiva para dispositivos MQTT, sino también la administración de dispositivos, el almacenamiento de datos y el análisis de datos en IBM Cloud. MQTT también superó la prueba de escalabilidad al convertirse en el protocolo de mensajería por detrás de Facebook Messenger.

Seguridad
El objetivo original del protocolo MQTT era hacer posible la transmisión de datos de una forma más pequeña y eficiente a través de líneas de comunicación costosas y poco fiables. Como tal, la seguridad no fue una de las principales preocupaciones durante el diseño e implementación de MQTT. Sin embargo, hay algunas opciones de seguridad disponibles a costa de una carga superior en la transmisión de datos y una mayor impronta.

Seguridad de red: si la red en sí puede protegerse, la transmisión de datos inseguros en MQTT es irrelevante. En tal caso, los problemas de seguridad tendrían que producirse desde el interior de la propia red, quizás a través de un actor malicioso u otra forma de penetración en la red.
Nombre de usuario y contraseña: MQTT permite nombres de usuario y contraseñas para que un cliente establezca una conexión con un bróker. Lamentablemente, para mantener la claridad, los nombres de usuario y las contraseñas se transmiten en texto sin cifrar. En 1999, esto era más que suficiente porque interceptar una comunicación por satélite para lo que era esencialmente una lectura de sensor sin importancia habría sido prohibitivamente difícil. Sin embargo, hoy en día, la interceptación de muchos tipos de comunicaciones de red inalámbrica se ha convertido en algo trivial, lo que hace que dicha autenticación sea casi inútil. Muchos casos de uso requieren un nombre de usuario y una contraseña ya no como protección contra actores maliciosos, sino como una forma de evitar conexiones involuntarias.
SSL/TLS: al ejecutarse sobre TCP/IP, la solución obvia para proteger las transmisiones entre clientes y brókeres es la implementación de SSL/TLS. Lamentablemente, esto añade una sobrecarga sustancial a unas comunicaciones, por lo demás, livianas.
El protocolo MQTT se usa para conectar y controlar dispositivos domésticos inteligentes por medio de hubs de hogares inteligentes. Al implementar el protocolo MQTT, los usuarios configuran un servidor. En el caso de los consumidores, por lo general, el servidor se encuentra en una PC o minicomputadora, como Raspberry Pi, a la que los dispositivos pueden conectarse y con la que pueden comunicarse. Si bien el protocolo MQTT es seguro, pueden surgir graves problemas de seguridad si no se implementa y configura bien. Los ciberdelincuentes pueden tener acceso total al hogar y descubrir si los propietarios se encuentran allí; manipular los sistemas de entretenimiento, asistentes de voz y dispositivos domésticos, así como también ver si las puertas y ventanas inteligentes están abiertas o cerradas. Bajo ciertas condiciones, los ciberdelincuentes incluso pueden rastrear la ubicación del usuario, lo que amenaza muy seriamente tanto su privacidad como su seguridad.

![](MqttTOOLapp.gif)


http://www.steves-internet-guide.com/install-mosquitto-linux/

http://www.steves-internet-guide.com/mosquitto_pub-sub-clients/

http://www.steves-internet-guide.com/category/mqtt-tools/


----



# Sentencias de Linux para instalar mosquitto

sudo apt-update 
sudo apt-get mosquitto
apt-get install mosquitto-client

etiquetas:
	-h :host 
	-p :puerto 
	-u :usuario
	-P :contraseña
	-t :topico 
	-m :mensaje 
	
## Comprobar que Mosquitto sirve de manera local

Con dos terminales bastan para comprobar su funcionamiento

### Terminal 1
En la terminal 1, el usuario debe escribir en la terminal

	mosquitto_sub -h localhost -p 1883 -t "prueba"
	
La terminal quedará en espera para que alguien publique un mensaje

### Terminal 2
En la terminal 2, el usuario debe escribir en la terminal

	mosquitto_pub -h localhost -p 1883 -t "prueba" -m "Hola servidor MQTT"
	
En la terminal 1 se arrojará el mensaje Hola servidor MQTT
	
# OPCIONAL (Establecer contraseña)
Sin contraseña, cualquier persona con la IP del servidor, puede acceder a cambiar la información.
  
  ### Primero debemos detener el servicio de mosquitto

  	sudo service mosquitto stop
  
  ### Acceder a la carpeta de mosquitto
  	cd /etc/mosquitto

  ### Crear un archivo de texto

	  cd /etc/mosquitto
	  sudo nano password.txt
  
  ### En el archivo, poner:
  usuario:contrasenia
  ### en usuario:contrasenia puedes sustituir a tu gusto las credenciales, pero debe salir de esa manera
  juan:123
  
  ### para agregar más usuarios: 
	cd /etc/mosquitto
	sudo nano password.txt 
	usuarionuevo:contraseña

### luego se encripta la información

	mosquitto_passwd -U password.txt
  
  ### sentencias extra en la config de mosquitto (en la carpeta de mosquitto):
  	sudo nano mosquitto.conf
	allow_anonymous false
	password_file /etc/mosquitto/pass.txt
  
### para iniciar el broker con la conf editada

	sudo mosquitto -c /etc/mosquitto/mosquitto.conf
	sudo service mosquitto start
### por si no les permite ingresar con usuario
	sudo service mosquitto stop
	sudo service mosquitto start
	
### Terminal 1
En la terminal 1, el usuario debe escribir en la terminal

	mosquitto_sub -h localhost -p 1883 -t "prueba" -u juan -P 123 
	
La terminal quedará en espera para que alguien publique un mensaje

### Terminal 2
En la terminal 2, el usuario debe escribir en la terminal

	mosquitto_pub -h localhost -p 1883 -t "prueba" -u juan -P 123 -m "Hola servidor MQTT"
	
En la terminal 1 se arrojará el mensaje Hola servidor MQTT y rechazará conexiones que no tengan el usuario juan con contraseña 123
	
	
