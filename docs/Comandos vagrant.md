
## Vagrant init
El comando `vagrant init` tiene como objetivo inicializar un nuevo proyecto de **Vagrant** en el directorio donde se ejecuta. Lo que hace específicamente es crear un archivo de configuración llamado `Vagrantfile`, que define cómo se va a configurar y gestionar la máquina virtual que vas a crear con Vagrant.

### Detalles de lo que hace `vagrant init`:

1. **Crea un archivo `Vagrantfile`**:
    
    - El archivo `Vagrantfile` es donde se definen las configuraciones de la máquina virtual que Vagrant va a gestionar, como:
        - La caja (o **box**) que se va a usar (por ejemplo, `ubuntu/trusty32`).
        - La cantidad de CPU y memoria a asignar.
        - Configuraciones de red (puertos, direcciones IP, etc.).
        - Carpetas compartidas entre la máquina anfitriona y la virtual.
        - Provisiones automáticas (como scripts o herramientas que quieras instalar automáticamente en la máquina virtual).
2. **Inicializa el proyecto con una caja especificada** (si usas el comando con un nombre de caja, como `vagrant init ubuntu/trusty32`):
    
    - Si proporcionas el nombre de una caja (box), como en el caso de `vagrant init ubuntu/trusty32`, Vagrant añade esa caja como referencia en el archivo `Vagrantfile` para que luego puedas descargarla y usarla.
    - No descarga la caja de inmediato, solo la define en el archivo de configuración.
3. **Prepara el entorno de desarrollo**:
    
    - Te da una base de configuración que luego puedes modificar según las necesidades de tu proyecto. Puedes editar el `Vagrantfile` para personalizar cómo será la máquina virtual.
4. **Configura la máquina virtual** (cuando la inicias con `vagrant up` después de `vagrant init`):
    
    - Posteriormente, cuando usas `vagrant up`, Vagrant leerá el archivo `Vagrantfile` y usará la configuración para descargar la caja y crear la máquina virtual con las especificaciones dadas.

## Comandos básicos

### 1. **`vagrant up`**

- Este es el comando que **levanta** (inicia) la máquina virtual definida en tu archivo `Vagrantfile`.
- Si la máquina virtual no existe todavía, Vagrant descarga la caja especificada (si no está ya descargada) y crea la máquina virtual.
- Si la máquina ya existe pero está detenida, este comando la enciende.
**Qué hace:**

- Descarga la caja (si es necesario).
- Crea y configura la máquina virtual.
- Inicia la máquina virtual.
- Ejecuta cualquier provisión (scripts o configuraciones) definidas en el `Vagrantfile`.

### 2. **`vagrant halt`**

- Este comando se utiliza para **apagar** la máquina virtual de forma segura, similar a un comando de "shutdown" en un sistema operativo.
- No destruye la máquina, solo la detiene. Los datos que tengas en ella no se pierden, simplemente queda apagada hasta que uses `vagrant up` para volver a encenderla.
- **Qué hace:**

- Detiene la máquina virtual de manera ordenada.
- Guarda el estado del sistema operativo, para que puedas reanudarlo más tarde.

**Es útil cuando** ya no necesitas la máquina en ejecución pero quieres preservarla para usarla más tarde sin perder nada.

### 3. **`vagrant destroy`**

- Este comando **destruye** completamente la máquina virtual, eliminando todos sus archivos y el estado de la misma.
- La caja base descargada no se elimina (sigue disponible para crear una nueva máquina virtual), pero todo lo que hiciste en esa máquina virtual (archivos, configuraciones, etc.) se pierde.
- Es útil si ya no necesitas la máquina y quieres liberar espacio en tu disco.
**Qué hace:**

- Elimina todos los archivos relacionados con la máquina virtual.
- Borra cualquier dato o configuración en la máquina.

**Es útil cuando** ya no necesitas la máquina virtual y quieres liberar recursos en tu sistema.

### 4. **Otros comandos útiles**

- **`vagrant suspend`**: Este comando **suspende** la máquina virtual. Es como poner la máquina en modo hibernación, guardando su estado en el disco para que puedas retomarla rápidamente más tarde. Usa menos recursos que tener la máquina encendida, pero no la destruye ni la apaga completamente.
- **`vagrant status`**: Este comando te da información sobre el **estado** actual de la máquina virtual (por ejemplo, si está apagada, en ejecución, suspendida, etc.).
- **`vagrant provision`**: Si has definido algún **provisioner** en el archivo `Vagrantfile` (como un script que instala software), puedes ejecutarlo en cualquier momento usando este comando, sin necesidad de reiniciar o destruir la máquina virtual.
Resumen
- **`vagrant up`**: Inicia o crea la máquina virtual.
- **`vagrant halt`**: Apaga la máquina virtual de forma segura.
- **`vagrant destroy`**: Destruye la máquina virtual y elimina todo su contenido.
- **`vagrant suspend`**: Suspende la máquina virtual, guardando su estado.
- **`vagrant status`**: Muestra el estado actual de la máquina virtual.
- **`vagrant provision`**: Ejecuta los scripts de aprovisionamiento definidos en el `Vagrantfile`.


## Vagrant status vs global-status
La diferencia entre **`vagrant status`** y **`vagrant global-status`** radica en el **alcance** de la información que proporcionan sobre las máquinas virtuales gestionadas por Vagrant.

### 1. **`vagrant status`**

- Muestra el **estado de la máquina virtual** asociada al directorio actual donde ejecutas el comando.
- Este comando es útil cuando estás trabajando en un directorio de un proyecto específico que tiene un archivo `Vagrantfile`. Te dice si la máquina está en ejecución, apagada, suspendida, o si no se ha creado aún.
**Lo que muestra:**

- Proporciona el estado de la máquina virtual en el directorio actual.
- Útil para verificar si la máquina en ese directorio está **en ejecución**, **apagada** o **suspendida**.

**Ejemplo de salida:**
Current machine states:

default                   running (virtualbox)

### 2. **`vagrant global-status`**

- Este comando proporciona el **estado de todas las máquinas virtuales** gestionadas por Vagrant en **todos los proyectos** de tu sistema, independientemente de en qué directorio te encuentres.
- Es útil si estás trabajando en múltiples proyectos con varias máquinas virtuales y quieres saber cuáles están activas o en qué estado se encuentran todas las máquinas que has creado.
**Lo que muestra:**

- Proporciona una lista de todas las máquinas virtuales en el sistema, junto con información clave como:
    - El ID único de cada máquina.
    - El nombre de la máquina.
    - El estado actual (ejecutándose, apagada, suspendida).
    - El proveedor (VirtualBox, VMware, etc.).
    - El directorio donde se encuentra el archivo `Vagrantfile` asociado.

**Ejemplo de salida:**
id       name    provider   state   directory
-------------------------------------------------------------------
a1b2c3   default virtualbox running /home/user/project1
d4e5f6   default virtualbox poweroff /home/user/project2
g7h8i9   vm1     virtualbox running /home/user/project3

Aquí se muestran tres máquinas virtuales en diferentes proyectos. Dos de ellas (`a1b2c3` y `g7h8i9`) están en ejecución, mientras que una (`d4e5f6`) está apagada.

### Resumen de las diferencias:

- **`vagrant status`**: Muestra el estado de **la máquina virtual** asociada al **directorio actual**.
- **`vagrant global-status`**: Muestra el estado de **todas las máquinas virtuales** gestionadas por Vagrant en **todos los proyectos** de tu sistema.

### Cuándo usar cada uno:

- Usa **`vagrant status`** cuando estás trabajando en un proyecto específico y solo necesitas conocer el estado de la máquina virtual asociada a ese proyecto.
- Usa **`vagrant global-status`** si necesitas una visión general de todas las máquinas virtuales que has creado en tu sistema, independientemente del proyecto o directorio en el que te encuentres.

## Vagrant boxes
vagrant box list
javier@javier-GF63-Thin-10SCXR:~/Escritorio/practicas/practica5/UbuntuEGC_box$ vagrant box list
cdcetsii/UbuntuEGC (virtualbox, 20241007, (amd64))
obihann/nginx      (virtualbox, 0.0.1)
ubuntu/jammy64     (virtualbox, 20241002.0.0)
ubuntu/trusty32    (virtualbox, 20191107.0.0)

vagrant box remove ubuntu/trusty32