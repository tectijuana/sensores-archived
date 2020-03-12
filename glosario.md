# GitHub Glosario

_A continuación se muestra una lista de algunos términos específicos de Git y GitHub que usamos en nuestros sitios y documentación._

# "Blame" / Culpar

La característica "culpar" de Git describe la última modificación de cada línea de un archivo, que generalmente muestra la revisión, el autor y la hora. Esto es útil, por ejemplo, para rastrear cuándo se agregó una característica o qué commit llevó a un error en particular.

# "Branch" / Rama

Una rama es una versión paralela de un repositorio. Está contenido dentro del repositorio, pero no afecta a la rama primaria o master que le permite trabajar libremente sin interrumpir la versión "en vivo". Cuando haya realizado los cambios que desea realizar, puede volver a fusionar su sucursal en la sucursal master para publicar los cambios.

# Clon

Un clon es una copia de un repositorio que vive en su computadora en lugar de en el servidor de un sitio web en algún lugar, o el acto de hacer esa copia. Con su clon puede editar los archivos en su editor preferido y utilizar Git para realizar un seguimiento de sus cambios sin tener que estar en línea. Sin embargo, está conectado a la versión remota para que los cambios puedan sincronizarse entre los dos. Puede enviar sus cambios locales al control remoto para mantenerlos sincronizados cuando esté conectado.

# Colaborador

Un colaborador es una persona con acceso de lectura y escritura a un repositorio que ha sido invitado a contribuir por el propietario del repositorio.

# "Commit" / Cometer

Una confirmación, o "revisión", es un cambio individual a un archivo (o conjunto de archivos). Es como cuando guarda un archivo, excepto con Git, cada vez que lo guarda, crea un ID único (aka el "SHA" o "hash") que le permite mantener un registro de los cambios realizados cuando y por quién. Los compromisos usualmente contienen un mensaje de confirmación que es una breve descripción de los cambios realizados.

# Contribuyente

Un colaborador es alguien que ha contribuido a un proyecto al tener una solicitud de extracción fusionada pero no tiene acceso de colaborador.

# "Diff" / Diferencia

Un _diff_ es la diferencia en los cambios entre dos confirmaciones o cambios guardados. El diff describirá visualmente lo que se agregó o eliminó de un archivo desde su último commit.

# "Fetch" / Recuperar

Recuperar se refiere a obtener los últimos cambios desde un repositorio en línea sin fusionarlos. Una vez que se recuperen estos cambios, puede compararlos con sus sucursales locales (el código que reside en su máquina local).

# "Fork" / Tenedor

Un tenedor es una copia personal del repositorio de otro usuario que vive en su cuenta. Las horquillas le permiten realizar cambios en un proyecto sin afectar al original. Las horquillas permanecen unidas al original, lo que le permite enviar una solicitud de extracción al autor del original para actualizar con sus cambios. También puede mantener su tenedor al día tirando de actualizaciones de la original.

# Git

Git es un programa de código abierto para el seguimiento de los cambios en los archivos de texto. Fue escrito por el autor del sistema operativo Linux, y es la tecnología principal que GitHub, la interfaz social y de usuario, se construye encima de.

# "Issues" / Casos 

Se sugieren mejoras, tareas o preguntas relacionadas con el repositorio. Los casos o problemas pueden ser creados por cualquier persona (para los repositorios públicos) y son moderados por los colaboradores del repositorio. Cada edición contiene su propio foro de discusión, se puede etiquetar y asignar a un usuario.

# Markdown / Reducción

Markdown es un formato de archivo semántico simple, no muy diferente de .doc, .rtf y .txt. Markdown hace que sea fácil para aquellos que no tienen un fondo de publicación web escribir prosa (incluyendo con enlaces, listas, viñetas, etc.) y que se muestre como un sitio web. GitHub soporta Markdown, y usted puede aprender sobre la semántica .

# "Merge" / Unir

La fusión toma los cambios de una rama (en el mismo repositorio o de una bifurcación) y los aplica a otra. Esto suele ocurrir como una petición de extracción (que se puede considerar como una solicitud de combinación) o mediante la línea de comandos. Una fusión se puede hacer automáticamente a través de una solicitud de extracción a través de la interfaz web de GitHub si no hay cambios conflictivos, o siempre se puede hacer a través de la línea de comandos. Para obtener más información, consulte " Fusión de una solicitud de extracción ".

"Open Source" / Fuente abierta

El software de código abierto es un software que puede ser libremente utilizado, modificado y compartido (tanto en forma modificada como no modificada) por cualquier persona . Hoy en día el concepto de "código abierto" a menudo se extiende más allá del software, para representar una filosofía de colaboración en la que los materiales de trabajo se ponen a disposición en línea para cualquier persona a bifurcar, modificar, discutir y 
contribuir.

Para obtener más información sobre código abierto, específicamente cómo crear y crear un proyecto de código abierto, hemos creado Guías de código abierto que le ayudarán a fomentar una comunidad de código abierto saludable.

Organizaciones

Las organizaciones son cuentas compartidas donde las empresas y los proyectos de código abierto pueden colaborar en muchos proyectos a la vez. Los propietarios y administradores pueden administrar el acceso de los miembros a los datos y proyectos de la organización con sofisticadas funciones administrativas y de seguridad.

# "Private Reporsitory" / Repositorio privado

Los repositorios privados son repositorios que sólo pueden ser vistos o aportados por su creador y colaboradores que el creador especificó. Tienen un costo adicional a la cuenta. Por Git Classroom que aplico TecTijuana, esta abierto a los estudiantes.

# "Pull" / extracción

Pull se refiere a cuando se están buscando en los cambios y la fusión de ellos. Por ejemplo, si alguien ha editado el archivo remoto en el que ambos están trabajando, deseará introducir esos cambios en su copia local para que esté actualizada.

# "Pull request" / Solicitud de extracción

Las solicitudes de extracción son cambios propuestos a un repositorio presentado por un usuario y aceptado o rechazado por los colaboradores de un repositorio. Al igual que las cuestiones, las solicitudes de tirar cada uno tiene su propio foro de discusión. Para obtener más información, consulte " Acerca de las solicitudes de extracción ".

# "Push" / empujar

Empujar se refiere a enviar los cambios comprometidos a un repositorio remoto, como un repositorio alojado en GitHub. Por ejemplo, si cambia algo localmente, desearía pulsar esos cambios para que otros puedan acceder a ellos. Muy similar a un pila pues el último cambio es la cabeza (HEAD) del repo.

# Remoto

Esta es la versión de algo que está alojado en un servidor, probablemente GitHub. Puede conectarse a clones locales para que se puedan sincronizar los cambios.

# Repositorio

Un repositorio es el elemento más básico de GitHub. Son más fáciles de imaginar como la carpeta de un proyecto. Un repositorio contiene todos los archivos del proyecto (incluida la documentación) y almacena el historial de revisiones de cada archivo. Los repositorios pueden tener múltiples colaboradores y pueden ser públicos o privados.

# Clave SSH

Las claves SSH son una forma de identificarse a un servidor en línea, usando un mensaje encriptado. Es como si tu computadora tuviera su propia contraseña única para otro servicio. GitHub utiliza las claves SSH para transferir información de forma segura a su computadora.

# Equipo

Los equipos son grupos de miembros de la organización que reflejan la estructura de su empresa o grupo con permisos de acceso en cascada y menciones.

# "Uptream" / "Downstream"

Cuando se habla de una rama o un tenedor, la rama principal en el repositorio original a menudo se conoce como el "upstream", ya que ese es el lugar principal de los que vendrán otros cambios. La rama en la que está trabajando se llama "downstream".

# Usuario

Los usuarios son cuentas personales de GitHub. Cada usuario tiene un perfil personal, y puede poseer múltiples repositorios, públicos o privados. Pueden crear o ser invitados a unirse a organizaciones o colaborar en el repositorio de otro usuario.
Otras lecturas

# Proyectos
Proyectos en GitHub le ayudan a organizar y priorizar su trabajo. Puede crear paneles de proyecto para el trabajo de características específicas, hojas de ruta completas o incluso listas de verificación de lanzamiento. Con las **tarjetas Kanban** de proyecto, tiene la flexibilidad se adapten a sus necesidades, se componen de cuestiones, solicitudes de tracción y notas que se clasifican como tarjetas en columnas de su elección. Las tarjetas se pueden mover de **columna en columna y reordenarse de acuerdo a sus necesidades**, cada una tiene metadatos relevantes para los problemas y solicitudes de extracción, como etiquetas, cesionarios, el estado y quién lo abrió. Si la nota no es suficiente para sus necesidades, **puede convertirla en un Caso (Issue).**


# Proyectos
