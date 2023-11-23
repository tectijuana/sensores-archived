MQTT (anteriormente conocido como MQ Telemetry Transport) es un protocolo de mensajería estándar definido por OASIS que se utiliza para conectar dispositivos e implementar comunicación de máquina a máquina (M2M). Es comúnmente utilizado como un protocolo de mensajería estándar en los dominios de Internet de las Cosas (IoT) e Internet Industrial de las Cosas (IIoT).

![](imagen/intro.png)

La primera versión del protocolo MQTT fue desarrollada por Andy Stanford Clark y Arlen Nipper de IBM en 1999 y recibió su nombre de la serie de productos MQ (Message Queue) de IBM. El objetivo era desarrollar un protocolo de mensajería ligero y adecuado para dispositivos como sensores y actuadores.

MQTT fue diseñado para ser altamente eficiente, lo que permite la transmisión de grandes cantidades de datos en redes más lentas y poco confiables, como enlaces por satélite comúnmente utilizados en la industria del petróleo y el gas en ese momento. Específicamente, se utilizaba para transmitir información entre sensores de baja potencia para monitorear oleoductos dentro del sistema de control y adquisición de datos industrial SCADA.

A pesar de su nombre, el componente "Message Queue" nunca se utilizó completamente en la nomenclatura del protocolo, ya que el protocolo MQTT se basa en un patrón de mensajería de publicación y suscripción, donde no se observa la encolación de mensajes en el sentido tradicional.

Versiones de MQTT
Las versiones más comunes de MQTT son 3.1, 3.1.1 y 5.0.

En 2013, IBM presentó MQTT v3.1 ante el cuerpo de especificaciones de OASIS, estipulando la aceptación de solo modificaciones menores a la especificación.
Posteriormente, OASIS asumió la responsabilidad de mantenimiento y lanzó v3.1.1 en 2014.
En 2019, se lanzó la última versión de MQTT, v5, que agrega varias características empresariales, como intervalo de caducidad de sesión/mensaje, código de motivo, alias de tema, propiedades de usuario y opciones de autenticación extendidas.
Además de las versiones mencionadas, existen otras versiones del protocolo MQTT diseñadas para aplicaciones de baja potencia, ancho de banda reducido y redes de sensores: MQTT-SN y MQTT-SN sobre UDP.

Continua el curso gratis por Mosquitto en https://cedalo.com/mqtt-academy/ completamente gratis y con animaciones
