## Docker run y docker exec

### 1. **`docker run`**:

- **Crea y ejecuta un nuevo contenedor** a partir de una imagen.
- Se utiliza para **iniciar** un contenedor desde cero.
- Descarga la imagen si no está disponible localmente y la usa para crear un nuevo contenedor.
- Permite pasar argumentos y configuraciones para la creación del contenedor, como mapeo de puertos, volúmenes, variables de entorno, etc.
- Cada vez que se usa `docker run`, se crea un **nuevo contenedor**, aunque hayas ejecutado uno con la misma imagen antes.

por ejemplo: docker run -it ubuntu bash
- Esto crea un nuevo contenedor a partir de la imagen `ubuntu` y ejecuta una sesión interactiva con `bash`.

### 2. **`docker exec`**:

- Se utiliza para **ejecutar un comando en un contenedor que ya está en ejecución**.
- No crea un nuevo contenedor. En su lugar, accede a un contenedor existente y ejecuta un comando dentro de él.
- Útil si deseas acceder a la shell del contenedor o ejecutar un comando adicional sin detenerlo o reiniciarlo.

por ejemplo: docker exec -it <container_id> bash
- Esto te permite acceder a una terminal (`bash`) dentro de un contenedor que ya está corriendo.

### Diferencias clave:

1. **Crear vs. Acceder**:
    
    - **`docker run`**: Crea y ejecuta un nuevo contenedor.
    - **`docker exec`**: Ejecuta un comando dentro de un contenedor ya existente.
2. **Estado del contenedor**:
    
    - **`docker run`**: Inicia un nuevo contenedor a partir de una imagen.
    - **`docker exec`**: Solo se puede usar en un contenedor que ya está en ejecución.
3. **Reutilización**:
    
    - **`docker run`**: Siempre crea un contenedor nuevo y separado.
    - **`docker exec`**: Trabaja dentro de un contenedor que ya está funcionando.

## Bind mount
Un **bind mount** en Docker es una forma de vincular (montar) un directorio o archivo del sistema de archivos de tu **máquina anfitriona** (host) a un directorio o archivo dentro de un **contenedor** de Docker. Esto permite compartir datos entre el host y el contenedor, y cualquier cambio que realices en el directorio montado en el host se reflejará inmediatamente en el contenedor, y viceversa.

### Conceptos clave del bind mount:

- Con un bind mount, puedes especificar cualquier ubicación en el sistema de archivos del host para que se vincule a un directorio específico en el contenedor.
- Los bind mounts pueden ser útiles para desarrollar aplicaciones, ya que puedes modificar los archivos en tu host y ver los cambios en el contenedor sin necesidad de reconstruir la imagen o reiniciar el contenedor.
- Es diferente de los **volúmenes** de Docker, que son gestionados por Docker y no están directamente vinculados a un directorio específico del host.

### Ejemplo:
docker run -it --rm -d -p 8080:80 --name web -v ~/site-content:/usr/share/nginx/html nginx

### Explicación:

- **`docker run`**: Ejecuta un nuevo contenedor.
- **`-it`**: Abre una sesión interactiva y asigna una pseudo-terminal.
- **`--rm`**: Elimina el contenedor automáticamente cuando se detenga.
- **`-d`**: Ejecuta el contenedor en segundo plano (detached mode).
- **`-p 8080:80`**: Mapea el puerto 80 del contenedor al puerto 8080 del host, de forma que cuando accedas al puerto 8080 de tu máquina (host), será redirigido al puerto 80 del contenedor (donde corre el servidor web NGINX).
- **`--name web`**: Asigna un nombre al contenedor (en este caso, `web`).
- **`-v ~/site-content:/usr/share/nginx/html`**: Aquí es donde se realiza el **bind mount**.
    - **`~/site-content`**: Es el directorio en el sistema de archivos del host. Esto corresponde a la carpeta `site-content` que se encuentra en tu directorio personal (`~`).
    - **`/usr/share/nginx/html`**: Es el directorio dentro del contenedor NGINX donde se almacenan los archivos HTML que NGINX sirve por defecto.

### ¿Qué hace este comando?

1. **Crea un contenedor de NGINX** que está vinculado al directorio `~/site-content` en tu sistema host.
    
2. El contenido del directorio `~/site-content` en tu host se montará dentro del contenedor en la carpeta `/usr/share/nginx/html`, que es donde NGINX busca sus archivos para servir.
    
3. Cuando accedes a `http://localhost:8080`, NGINX servirá los archivos que se encuentran en el directorio `~/site-content` de tu host.
    
    Esto significa que si agregas, eliminas o modificas archivos en `~/site-content` en tu host, esos cambios se reflejarán instantáneamente en el contenedor, y NGINX los servirá cuando accedas al puerto 8080.
    

### ¿Cuándo usar bind mounts?

- Durante el **desarrollo**, para que puedas modificar archivos en tu máquina local y ver los cambios reflejados instantáneamente en el contenedor.
- Cuando necesitas compartir archivos entre el contenedor y el sistema de archivos del host.

### Ventajas:

- **Desarrollo rápido**: Puedes trabajar en tu máquina local y ver los cambios reflejados en tiempo real dentro del contenedor.
- **Flexibilidad**: Puedes elegir cualquier directorio o archivo de tu sistema de archivos y montarlo en cualquier ubicación del contenedor.

