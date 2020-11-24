# AWS IoT Greengrass
https://aws.amazon.com/greengrass/

Esta imagen ejecuta el software Greengrass Core dentro de un contenedor Docker.

_AWS IoT Greengrass es un software que extiende las capacidades de la nube de AWS a los dispositivos locales. Esto permite que los dispositivos recopilen y analicen datos más cerca de la fuente de información, reaccionen de forma autónoma a eventos locales y se comuniquen de forma segura entre sí en redes locales.

_Esta imagen se puede ejecutar en cualquier plataforma que admita contenedores Docker. La imagen se superpone a las imágenes base de amazonlinux: 2, alpine-x86-64, alpine-armv7l y alpine-aarch64. La imagen de Greengrass puede admitir la ejecución de AWS Lambdas escrito en Python-3.7, Nodejs-12.xy Java-8._

# Tags
La etiqueta más reciente es la última versión estable del software AWS IoT Greengrass instalado en la imagen base de amazonlinux: 2. Cada versión de software y plataforma de imagen base tiene una etiqueta correspondiente en el formato X.Y.Z-platform, p. Ej. 1.8.0-amazonlinux.

# Uso
Puede encontrar documentación adicional para esta imagen en la documentación de AWS IoT Greengrass. https://docs.aws.amazon.com/greengrass/latest/developerguide/run-gg-in-docker-container.html

Cuando se ejecuta directamente a través de Docker, la imagen debe poder acceder al demonio Docker del host para que funcione correctamente. La forma recomendada de hacer esto es enlazar en los directorios certs/config de Greengrass Core y, opcionalmente, en las carpetas de implementación y registro para los registros persistentes y los artefactos de implementación en las ejecuciones de contenedores.

```bash
docker run --rm --init -it --name aws-iot-greengrass --entrypoint /greengrass-entrypoint.sh -v $PWD/certs:/greengrass/certs -v $PWD/config:/greengrass/config -p 8883:8883 amazon/aws-iot-greengrass
```
# Updating
Puede actualizar a la imagen más reciente en Dockerhub ejecutando lo siguiente:

```bash
docker stop aws-iot-greengrass
docker rm aws-iot-greengrass
docker pull amazon/aws-iot-greengrass:latest
```

YEntonces deberías seguir el "Usage" instrucciones para volver a ejecutarlo.

# Source code
El código fuente está disponible para generar imágenes personalizadas: https://docs.aws.amazon.com/greengrass/latest/developerguide/ggc-docker-download.html

# Issues
Los problemas deben informarse en el foro de AWS IoT Greengrass: https://forums.aws.amazon.com/forum.jspa?forumID=254
