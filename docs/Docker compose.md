Docker Compose es una herramienta que permite definir y gestionar aplicaciones multicontenedor. Es ideal para aplicaciones que constan de varios servicios, como bases de datos, aplicaciones web, proxies inversos, etc. Con Docker Compose, puedes definir toda la infraestructura de la aplicación en un archivo docker-compose.yml y gestionarla con comandos simples.
Conceptos clave de Docker Compose

    Servicios: Un servicio es un contenedor de Docker que ejecuta una parte de tu aplicación. Cada servicio puede tener sus propias configuraciones, variables de entorno, volúmenes, redes, etc.

    Contenedores: Los servicios en Docker Compose están respaldados por contenedores de Docker. Docker Compose gestiona el ciclo de vida de estos contenedores.

    Redes: Docker Compose crea automáticamente una red para facilitar la comunicación entre los contenedores que forman parte de la misma aplicación.

    Volúmenes: Los volúmenes permiten que los datos persistan entre reinicios de contenedores, y Docker Compose facilita la definición y la administración de volúmenes compartidos entre servicios.

Estructura de un archivo docker-compose.yml

El archivo docker-compose.yml define toda la configuración de tu aplicación. A continuación, te explico los bloques más esenciales que puedes usar:

version: '3.8' # Versión de Compose

services:
  web:                    # Nombre del servicio
    image: nginx           # Imagen de Docker que usará
    ports:
      - "8080:80"          # Mapea el puerto 80 del contenedor al puerto 8080 del host
    volumes:
      - ./html:/usr/share/nginx/html  # Mapea un directorio local a un directorio dentro del contenedor
    environment:           # Variables de entorno
      - NGINX_HOST=foobar.com
      - NGINX_PORT=80
    networks:
      - my_network

  database:                # Otro servicio (en este caso, una base de datos)
    image: postgres
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - db_data:/var/lib/postgresql/data
    networks:
      - my_network

volumes:
  db_data:                 # Definición de un volumen para persistir datos

networks:
  my_network:              # Definición de una red para conectar los servicios

Elementos Esenciales del Archivo docker-compose.yml

    Version: Define la versión de la especificación de Compose. Las versiones más recientes ofrecen más funcionalidades, como redes personalizadas.

    Services: Define los servicios de tu aplicación. Cada servicio es un contenedor independiente, y puedes definir tantos como necesites.
        Image: Especifica la imagen de Docker que se va a utilizar para ese servicio.
        Build: Si deseas construir una imagen desde un Dockerfile, especificas la ruta.
        Ports: Permite el mapeo de puertos entre el contenedor y el host.
        Volumes: Mapea volúmenes para persistir datos o compartir archivos entre el host y los contenedores.
        Environment: Configura variables de entorno.
        Depends_on: Define dependencias entre servicios, indicando el orden en que deben iniciarse.

    Volumes: Define volúmenes compartidos y persistentes entre los contenedores. Esto es útil para almacenar datos que sobrevivan a reinicios de contenedores.

    Networks: Gestiona la red privada en la que se ejecutan los contenedores. Todos los servicios definidos en un mismo Compose compartirán esta red a menos que especifiques lo contrario.

Comandos esenciales de Docker Compose

    docker-compose up
        Levanta y ejecuta los contenedores definidos en el archivo docker-compose.yml.

docker-compose up

    Para ejecutar en segundo plano:

    docker-compose up -d

docker-compose down

    Detiene y elimina los contenedores, redes y volúmenes creados por docker-compose up.

docker-compose down

docker-compose build

    Construye las imágenes de Docker especificadas en el archivo docker-compose.yml.

docker-compose build

docker-compose logs

    Muestra los logs de todos los servicios.

docker-compose logs

docker-compose ps

    Lista los contenedores gestionados por Docker Compose.

docker-compose ps

docker-compose stop

    Detiene los contenedores sin eliminarlos.

docker-compose stop

docker-compose restart

    Reinicia todos los servicios.

docker-compose restart

docker-compose exec

    Ejecuta un comando en un contenedor en ejecución.

docker-compose exec service_name command

    Ejemplo:

        docker-compose exec web bash

Variables de entorno en Docker Compose

Puedes usar variables de entorno en el archivo docker-compose.yml para parametrizar configuraciones. Existen dos maneras de hacerlo:

    Directamente en el archivo docker-compose.yml con el bloque environment.
    A través de un archivo .env: Docker Compose automáticamente lee las variables definidas en este archivo y las sustituye en el docker-compose.yml.

Ejemplo de un archivo .env:

POSTGRES_USER=user
POSTGRES_PASSWORD=password

Y en el docker-compose.yml:

version: '3.8'

services:
  db:
    image: postgres
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}

Escenarios comunes con Docker Compose

    Aplicaciones multicontenedor: Si tienes una aplicación web con una base de datos, como en el ejemplo anterior, puedes definir ambos servicios en el archivo docker-compose.yml, conectarlos mediante una red compartida, y ejecutarlos juntos con docker-compose up.

    Desarrollo local: Puedes usar Docker Compose para definir entornos de desarrollo replicables y de fácil despliegue, asegurando que todos los desarrolladores usen el mismo entorno.

    Testing: Compose es útil para configurar y ejecutar pruebas automáticas en entornos reproducibles.

    Despliegue: Aunque Docker Compose se usa principalmente en desarrollo, también puede usarse para desplegar aplicaciones en producción, sobre todo en configuraciones más simples. Para producción a gran escala, herramientas como Kubernetes suelen ser más adecuadas.

Conclusión

Docker Compose es una herramienta poderosa que simplifica la creación, configuración y gestión de aplicaciones multicontenedor. Con un simple archivo YAML, puedes definir cómo deben ejecutarse todos los servicios de tu aplicación, cómo deben comunicarse entre ellos, qué volúmenes y puertos deben usar, entre otras configuraciones. Esto facilita enormemente el desarrollo, pruebas y despliegue de aplicaciones más complejas.


## Docker-compose.dev.yml
Este archivo docker-compose.yml define una aplicación multicontenedor con tres servicios: web, db, y nginx. A continuación, te explico cada bloque del archivo en detalle:
1. Servicio web

Este servicio define el contenedor para una aplicación web que se ejecutará en el contenedor web_app_container.

    container_name: web_app_container: Asigna un nombre específico al contenedor para que sea más fácil de identificar (en este caso, web_app_container).

    image: drorganvidez/uvlhub:dev: Especifica la imagen de Docker que se utilizará para crear el contenedor, en este caso, una imagen personalizada de uvlhub en su versión dev.

    env_file: - ../.env: Carga un archivo de variables de entorno .env desde un directorio anterior (../) al que contiene este archivo docker-compose.yml. Esto permite parametrizar el contenedor con variables externas.

    expose: - "5000": Expone el puerto 5000 dentro del contenedor. A diferencia de ports, este comando no realiza un mapeo al host, sino que permite que otros contenedores en la misma red accedan a este puerto.

    depends_on: - db: Indica que este servicio depende del servicio db (base de datos), por lo que Docker Compose iniciará primero el contenedor de la base de datos antes de iniciar web.

    build:
        context: ../: Indica que el contexto de construcción está en el directorio padre del archivo docker-compose.yml. Aquí es donde Docker buscará el Dockerfile y otros archivos relacionados con la construcción de la imagen.
        dockerfile: docker/images/Dockerfile.dev: Especifica la ruta al Dockerfile que se utilizará para construir la imagen de este servicio, en este caso, el archivo Dockerfile.dev dentro de docker/images/.

    volumes:
        ../:/app: Mapea el directorio padre (../) del host al directorio /app dentro del contenedor. Esto permite que el código del host esté disponible dentro del contenedor, facilitando el desarrollo (puedes hacer cambios en el código sin tener que reconstruir el contenedor).
        /var/run/docker.sock:/var/run/docker.sock: Mapea el archivo de socket de Docker desde el host al contenedor. Esto permite que el contenedor se comunique con el demonio de Docker del host, útil si la aplicación necesita interactuar con Docker.

    command:
        [ "sh", "-c", "sh /app/docker/entrypoints/development_entrypoint.sh" ]: Ejecuta un comando de shell dentro del contenedor. En este caso, está ejecutando un script llamado development_entrypoint.sh, ubicado en el directorio /app/docker/entrypoints/. Este script probablemente contiene las instrucciones para arrancar la aplicación web en un entorno de desarrollo.

    networks: - uvlhub_network: Conecta este servicio a la red uvlhub_network, que está definida más abajo.

2. Servicio db

Este servicio define un contenedor de base de datos MariaDB que se ejecutará en el contenedor mariadb_container.

    container_name: mariadb_container: Nombre del contenedor para la base de datos MariaDB.

    env_file: - ../.env: También usa el archivo .env para configurar variables de entorno relacionadas con la base de datos (como el nombre de la base de datos, usuario, contraseña, etc.).

    build:
        context: ../: El contexto de construcción está en el directorio padre.
        dockerfile: docker/images/Dockerfile.mariadb: El Dockerfile específico para MariaDB se encuentra en docker/images/Dockerfile.mariadb.

    restart: always: Configura el contenedor para que siempre se reinicie si falla o si el host se reinicia.

    ports: - "3306:3306": Mapea el puerto 3306 del contenedor (donde MariaDB escucha por defecto) al puerto 3306 del host. Esto permite que la base de datos sea accesible desde el host.

    volumes: - db_data:/var/lib/mysql: Define un volumen llamado db_data que almacena los datos de MariaDB en el directorio /var/lib/mysql dentro del contenedor. Esto asegura que los datos de la base de datos persistan entre reinicios o recreaciones del contenedor.

    networks: - uvlhub_network: Conecta este servicio a la red uvlhub_network.

3. Servicio nginx

Este servicio define un contenedor para un servidor Nginx que actuará como servidor web o proxy inverso.

    container_name: nginx_web_server_container: Nombre del contenedor Nginx.

    image: nginx:latest: Utiliza la imagen oficial de Nginx en su versión más reciente.

    volumes:
        ./nginx/nginx.dev.conf:/etc/nginx/nginx.conf: Mapea el archivo de configuración de Nginx (nginx.dev.conf) del host al archivo de configuración por defecto de Nginx dentro del contenedor (/etc/nginx/nginx.conf). Esto permite personalizar la configuración de Nginx.
        ./nginx/html:/usr/share/nginx/html: Mapea un directorio local donde se almacena el contenido HTML del sitio web a la ubicación donde Nginx busca los archivos HTML (/usr/share/nginx/html). Esto permite cambiar el contenido del sitio web sin modificar el contenedor.

    ports: - "80:80": Mapea el puerto 80 del contenedor al puerto 80 del host, permitiendo que el servidor Nginx sea accesible desde el navegador en el host.

    depends_on: - web: Indica que Nginx depende de que el servicio web esté corriendo, por lo que Nginx se iniciará después de que el servicio web esté disponible.

    networks: - uvlhub_network: Conecta este servicio a la red uvlhub_network.

4. Volúmenes

El bloque de volumes define un volumen persistente llamado db_data, que se usa en el servicio db para almacenar los datos de la base de datos MariaDB. Esto garantiza que los datos no se pierdan incluso si el contenedor de la base de datos se reinicia o elimina.
5. Redes

El bloque networks define una red llamada uvlhub_network que es utilizada por todos los servicios (web, db, y nginx). Esta red permite que los contenedores se comuniquen entre sí utilizando sus nombres de servicio como hostnames.
Resumen

Este archivo docker-compose.yml orquesta una aplicación que incluye:

    Un servicio web que usa la imagen personalizada drorganvidez/uvlhub:dev.
    Un servicio de base de datos MariaDB.
    Un servidor Nginx como proxy o servidor web.

Cada servicio está conectado a la misma red (uvlhub_network) para que puedan comunicarse entre ellos, y los datos de la base de datos se almacenan de manera persistente en el volumen db_data.