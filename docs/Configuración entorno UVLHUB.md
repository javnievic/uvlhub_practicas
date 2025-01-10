## Configuración inicial

Abrimos ev (https://ev.us.es/) y github ()
1. **Instalamos git** (No es necesario, ya existe)
	sudo apt install git (git -h (comprobamos que existe))
2. **Configurar tu nombre y correo en Git**:
	git config --global user.name "Javier Nieto" (Para verlo git config --global user.name)
	git config --global user.email javiernieto03.jnv@gmail.com (Para verlo git config --global user.email)
3. **Generar un par de claves SSH**:
`ssh-keygen -t rsa -b 4096`
Este comando genera un par de claves SSH (una clave pública y una privada). Las claves RSA de 4096 bits son seguras y se usan para autenticarte con GitHub sin necesidad de introducir tu contraseña cada vez que interactúas con un repositorio remoto.
4. **Ver la clave pública generada**:
	```
	cd ~/.ssh 
	cat id_rsa.pub
	
Este conjunto de comandos te lleva al directorio `~/.ssh`, donde se encuentran las claves SSH generadas. Luego, con `cat id_rsa.pub`, muestras el contenido de la clave pública (la que puedes compartir con otros servicios de forma segura).


5. **Copiar la clave pública a GitHub**: Para vincular tu clave SSH con GitHub y poder interactuar con tus repositorios sin tener que escribir tu contraseña cada vez, debes copiar tu clave pública a GitHub.

	1. En GitHub, ve a **Settings** (Configuración) en la esquina superior derecha, luego haz clic en **SSH and GPG keys** en el menú lateral. (https://github.com/settings/keys)
	2. Haz clic en **New SSH key**.
	3. En el campo para la clave, pega el contenido de tu clave pública (lo que copiaste con `cat id_rsa.pub`).
	4. Comprobamos que funciona con `ssh -T git@github.com` (Hay que poner "yes" primero)
6. Forkeamos
	      `github.com/<tuusuario>/uvlhub_practicas`
7. En la carpeta que queramos hacemos git clone  "git@github.com:javnievic/EGC2324-turno42-javnievic.git"
8. Activar las issues en https://github.com/javnievic/EGC2324-turno42-javnievic/settings
**¿Qué hace esta configuración?**

- **Generación de claves SSH**: Te permite autenticarte de manera segura con GitHub sin necesidad de contraseñas, usando la clave privada en tu máquina y la clave pública que has agregado a GitHub.
- **Vinculación de Git y GitHub**: Git usa tu clave SSH para establecer una conexión segura con GitHub, permitiéndote realizar acciones como "clonar", "push" o "pull" en tus repositorios.

## Configuración uvlhub
https://docs.uvlhub.io/installation/manual_installation

Pasos para migrar la base de datos: 
sudo mysql -u root -p

DROP DATABASE IF EXISTS uvlhubdb; 
DROP DATABASE IF EXISTS uvlhubdb_test; 
DROP USER IF EXISTS 'uvlhubdb_user'@'localhost'; 

CREATE DATABASE uvlhubdb; 
CREATE DATABASE uvlhubdb_test; 
CREATE USER 'uvlhubdb_user'@'localhost' IDENTIFIED BY 'uvlhubdb_password'; 
GRANT ALL PRIVILEGES ON uvlhubdb.* TO 'uvlhubdb_user'@'localhost';
GRANT ALL PRIVILEGES ON uvlhubdb_test.* TO 'uvlhubdb_user'@'localhost'; 
FLUSH PRIVILEGES; 
EXIT; 

flask db upgrade 
rosemary db:seed --reset


### Configuración mariadb
1. Mostrar las bases de datos disponibles:

Si no sabes qué bases de datos tienes en tu sistema, puedes listar todas las bases de datos con el siguiente comando:

`SHOW DATABASES;`

Esto te mostrará todas las bases de datos disponibles en tu servidor MariaDB/MySQL.
2. Seleccionar la base de datos:

Para poder ver las tablas, primero debes seleccionar la base de datos en la que quieres trabajar. Suponiendo que tu base de datos se llame mi_base_de_datos, el comando sería:

`USE mi_base_de_datos;`

Esto cambiará el contexto de trabajo a esa base de datos.
3. Mostrar las tablas de la base de datos seleccionada:

Una vez que hayas seleccionado la base de datos, puedes listar todas las tablas dentro de ella con el siguiente comando:

`SHOW TABLES;`

Esto te mostrará todas las tablas que existen en la base de datos seleccionada.
4. Ver la estructura de una tabla específica:

Si deseas ver la estructura de una tabla específica (es decir, las columnas y sus tipos de datos), puedes usar el siguiente comando, sustituyendo nombre_tabla por el nombre de la tabla que quieras inspeccionar:

`DESCRIBE nombre_tabla;`

También puedes usar:

`SHOW COLUMNS FROM nombre_tabla;`

5. Ver datos dentro de una tabla:

Si quieres ver los datos almacenados en una tabla, puedes hacer una consulta simple como:

SELECT * FROM nombre_tabla;

Resumen de los comandos a utilizar:

    SHOW DATABASES;
    USE mi_base_de_datos;
    SHOW TABLES;
    DESCRIBE nombre_tabla; o SHOW COLUMNS FROM nombre_tabla;
    SELECT * FROM nombre_tabla;

Esto te permitirá ver las tablas y la estructura de tu base de datos.








### 1. **Usar tu clave SSH en el otro ordenador**

Para poder autenticarte en GitHub desde otro ordenador, necesitarás tener tu clave privada en ese ordenador también, ya que es la que te permitirá acceder a tus repositorios. Sin embargo, esto implica ciertos riesgos si no tomas las precauciones adecuadas. Aquí te doy un par de opciones:

#### Opción A: Copiar tu clave privada de manera segura

1. **Copia la clave privada** desde tu ordenador personal al otro ordenador. La clave privada está en el archivo `~/.ssh/id_rsa` (en Linux/macOS) o en una ubicación similar en Windows.
    
    **Importante**: No debes compartir ni subir este archivo a ningún lugar no seguro. Asegúrate de transferirla de manera segura (por ejemplo, utilizando un USB cifrado o mediante un servicio de almacenamiento en la nube con cifrado).
    
2. **Pega la clave privada** en el mismo directorio (`~/.ssh/`) en el otro ordenador. Si el directorio `~/.ssh/` no existe, créalo.
    
3. **Asegúrate de que los permisos de la clave privada sean correctos**. Debes asegurarte de que sólo tú tengas acceso a la clave privada en el nuevo ordenador: chmod 600 ~/.ssh/id_rsa
4. **Configura Git para usar esa clave**. Si el nuevo ordenador no está configurado con tu usuario de GitHub, puedes configurarlo de la siguiente manera:
	git config --global user.name "Tu Nombre"
	git config --global user.email "tu.email@dominio.com"

Probar que funciona la conexión: ssh -T git@github.com

#### Opción B: Crear una nueva clave SSH para ese ordenador

Si no deseas transferir tu clave privada y prefieres no compartirla, puedes crear un nuevo par de claves SSH en el otro ordenador y añadir la nueva clave pública a tu cuenta de GitHub. Esto te permitirá acceder a tus repositorios desde ese ordenador de forma segura, sin comprometer la clave privada original.

Pasos:

	Genera un nuevo par de claves SSH en el otro ordenador:

ssh-keygen -t rsa -b 4096

Añadir la clave pública a GitHub:

    Dirígete a la carpeta ~/.ssh/ y encuentra el archivo id_rsa.pub (o el nombre que le hayas dado a tu clave pública).
    Copia el contenido de id_rsa.pub usando el siguiente comando:

    cat ~/.ssh/id_rsa.pub

    Ve a GitHub, en Settings > SSH and GPG keys, y agrega una nueva clave SSH, pegando el contenido de id_rsa.pub en el formulario.

Verifica la autenticación: Puedes probar que tu clave funciona correctamente con el siguiente comando:

ssh -T git@github.com


## Eliminar claves

Si todo está bien configurado, deberías ver un mensaje de bienvenida de GitHub.


Para eliminar las claves de tu PC:

    Eliminar la clave privada y la pública: Si ya no quieres usar estas claves, puedes eliminarlas con el siguiente comando:

rm id_rsa id_rsa.pub

Eliminar el archivo known_hosts: Si también deseas eliminar el registro de servidores conocidos (como GitHub), puedes eliminar el archivo known_hosts:

rm known_hosts

Si prefieres solo eliminar la entrada específica de GitHub, puedes editar el archivo known_hosts y eliminar esa línea. Usa un editor de texto como nano:

nano ~/.ssh/known_hosts

Una vez dentro, busca la línea que corresponde a GitHub (probablemente será algo relacionado con la dirección IP o el nombre github.com) y elimina esa línea. Luego guarda los cambios (Ctrl + O) y cierra el editor (Ctrl + X).

