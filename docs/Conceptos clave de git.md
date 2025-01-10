Conceptos Clave de Git
Working Directory (Directorio de trabajo)

		El directorio de trabajo es la carpeta donde están los archivos del proyecto en tu máquina local.
    Aquí es donde puedes modificar y trabajar con los archivos de tu proyecto.

Staging Area (Área de preparación)

    El área de preparación es como un "área intermedia" donde Git guarda los archivos que deseas incluir en el próximo commit.
    Antes de hacer un commit, debes agregar los archivos al área de preparación usando git add.
    Puedes ver el estado del área de preparación con el comando git status.

### Relación entre el Working Directory y Staging Area

- **Working Directory**: Aquí es donde trabajas con tus archivos. Puedes editarlos, eliminarlos o crearlos.
- **Staging Area**: Es una zona intermedia donde colocas los archivos que deseas incluir en el próximo commit. Es un paso previo a guardar definitivamente los cambios en el historial de Git.
- **Commit**: Solo los archivos que han sido añadidos al área de preparación con `git add` se incluirán en el commit. Los cambios no añadidos no se guardarán en el historial.

## Comandos clave de git
### `git init`

- **Descripción**: Inicializa un nuevo repositorio Git en el directorio actual.
- **Uso**:
- **Qué hace**: Crea una carpeta oculta llamada `.git` en tu directorio de trabajo, que contiene todos los metadatos del repositorio. A partir de aquí, tu directorio está bajo control de versiones de Git.
- **Ejemplo**: mkdir mi_proyecto cd mi_proyecto git init


### `git status`

- **Descripción**: Muestra el estado del repositorio, indicando qué archivos han cambiado, cuáles están listos para ser confirmados (committed) y cuáles no.
- **Uso**: git status
- **Qué muestra**:
    - Archivos **modificados**: Archivos que han sido modificados desde el último commit.
    - Archivos **no rastreados**: Archivos nuevos que Git aún no está siguiendo.
    - Archivos **en el área de preparación**: Archivos que han sido añadidos al área de preparación con `git add`, y están listos para ser confirmados.
- **Ejemplo**: Si editas un archivo llamado `index.html` y ejecutas `git status`, Git te mostrará que `index.html` está modificado pero aún no ha sido añadido al área de preparación.

(venv) javier@javier-GF63-Thin-10SCXR:~/Escritorio/uvlhub_practicas$ git status
En la rama git-pruebas
Tu rama está actualizada con 'origin/git-pruebas'.

Cambios no rastreados para el commit:
  (usa "git add "archivo"..." para actualizar lo que será confirmado)
  (usa "git restore "archivo"..." para descartar los cambios en el directorio de trabajo)
        modificados:     app/modules/notepad/templates/notepad/create.html

Archivos sin seguimiento:
  (usa "git add "archivo"..." para incluirlo a lo que será confirmado)
        app/modules/notepad/prueba.txt

sin cambios agregados al commit (usa "git add" y/o "git commit -a")


### `git add`

- **Descripción**: Añade archivos modificados o nuevos al área de preparación, lo que significa que estarán listos para ser incluidos en el próximo commit.
- **Uso**: git add "archivo"   # Añadir un archivo específico
	git add .           # Añadir todos los archivos modificados en el directorio actual

- **Qué hace**: Mueve los archivos que has modificado desde el directorio de trabajo al área de preparación. Estos archivos están listos para ser confirmados en el próximo commit.
    
- **Ejemplo**: git add index.html  # Añadir solo el archivo index.html
git add .           # Añadir todos los archivos modificados
- Para revertir esta acción se puede utilizar git reset <"archivo">, o git reset


# Git: `git fetch` y `git pull`

## `git fetch`

`git fetch` es un comando que se utiliza para **descargar** los cambios (commits, archivos, referencias) de un repositorio remoto, pero **sin aplicar** estos cambios a tu rama actual. Se limita a traer los datos actualizados a tu repositorio local, para que luego puedas revisarlos y decidir qué hacer con ellos.

### Características:

- **No modifica** tu Working Directory ni tu rama actual.
- Solo actualiza el estado de las referencias remotas (como `origin/master`).
- Permite ver qué cambios han ocurrido en el repositorio remoto antes de combinarlos.

git fetch origin

Este comando descarga todos los cambios desde el remoto `origin`, pero **no los aplica** automáticamente a tu proyecto local.

### Flujo de trabajo con `git fetch`:

1. Ejecutas `git fetch` para obtener los últimos cambios desde el remoto.
2. Puedes ver las diferencias entre tu rama local y la rama remota. git log origin/main
3. Si decides aplicar esos cambios, puedes hacerlo mediante un `git merge`: git merge origin/main

### ¿Qué pasa con `upstream` cuando usas `git fetch`?

Si tienes dos remotos configurados (como `origin` y `upstream`), aquí está lo que sucede:

1. **Si usas `git fetch` sin `--all`**:
    
    - Git actualizará solo las **referencias de `origin`**, que es tu repositorio remoto por defecto.
    - No se actualizarán las referencias de `upstream` (el repositorio original del que hiciste el fork).
    
    Si haces `git fetch`, solo se traerán las actualizaciones de las ramas del remoto `origin`.
    
2. **Si usas `git fetch --all`**:
    
    - Git actualizará las referencias de **ambos remotos**, es decir, tanto `origin` como `upstream`.
    - Esto traerá las actualizaciones de las ramas tanto de tu repositorio (`origin`) como del repositorio original (`upstream`).


## `git pull`

`git pull` es un comando que **combina** dos operaciones: `git fetch` + `git merge`. Descarga los cambios desde el repositorio remoto y **los aplica** directamente a tu rama actual.

### Características:

- Actualiza el Working Directory aplicando los cambios que trae del remoto.
- Si hay nuevos commits en el remoto que no tienes localmente, `git pull` los integrará en tu proyecto.
- Puede generar conflictos si has modificado archivos en tu rama local que también se han cambiado en la rama remota.

### Ejemplo de uso:
git pull origin main
Este comando descargará los cambios de la rama `main` en el remoto `origin` y los integrará con tu rama local.

### Flujo de trabajo con `git pull`:

1. Ejecutas `git pull` para **descargar y fusionar** los últimos cambios desde el remoto.
2. Git combinará automáticamente los cambios, a menos que haya conflictos.
3. Si hay conflictos, deberás resolverlos antes de poder completar el merge.

### Diferencia clave entre `git fetch` y `git pull`:

- `git fetch`: Solo descarga los cambios pero **no los aplica** automáticamente.
- `git pull`: Descarga y **aplica** los cambios automáticamente.



### Diferencias entre `git reset` y `git revert`

- **`git reset`**:
    
    - **Qué hace**: Deshace cambios en el historial moviendo el puntero de la rama actual a un commit anterior. Los cambios que se revierten pueden afectar tanto al índice (staging area) como al directorio de trabajo.
    - **Tipos**:
        - `--soft`: Solo mueve el puntero de la rama, dejando los archivos sin modificar.
        - `--mixed` (por defecto): Mueve el puntero de la rama y restablece el área de preparación (staging area), pero los archivos modificados permanecen en el directorio de trabajo.
        - `--hard`: Borra completamente todos los cambios en el historial, el índice y el directorio de trabajo.
    - **Consecuencia**: Modifica el historial, lo que puede ser problemático si los commits ya han sido compartidos con otros. No es seguro para usar en repositorios públicos.
    - **Uso típico**: Cuando deseas eliminar completamente commits no deseados o rehacer el historial local.
- **`git revert`**:
    
    - **Qué hace**: Crea un nuevo commit que deshace los cambios introducidos por un commit anterior sin alterar el historial existente.
    - **Consecuencia**: No modifica el historial, lo que lo hace seguro para usar en repositorios compartidos o públicos.
    - **Uso típico**: Cuando quieres deshacer cambios pero conservar el historial intacto para mantener un registro completo y transparente de lo que ha ocurrido.



## Origin/main y origin main
En Git, los comandos que interactúan con una rama remota (como `origin/main`) requieren una referencia explícita a esa rama. Aquí están algunos comandos comunes que puedes usar **con `origin/main`** y no con `origin main`:

### 1. **`git fetch origin main`**

- **Qué hace**: Descarga los cambios desde la rama `main` del repositorio remoto `origin` pero **sin integrarlos** en la rama local. Solo actualiza la referencia remota.

### 2. **`git pull origin main`**

- **Qué hace**: Combina dos acciones. Primero hace un `git fetch` para traer los cambios de `origin/main`, y luego un `git merge` para integrar esos cambios en la rama local.

### 3. **`git push origin main`**

- **Qué hace**: Sube los cambios desde tu rama local hacia la rama remota `main` en `origin`.

### 4. **`git checkout origin/main`**

- **Qué hace**: Cambia el contexto de tu trabajo a la versión remota de la rama `main` en `origin`. No cambia la rama local, sino que te permite ver el estado de `origin/main` sin afectarla.

### 5. **`git reset --hard origin/main`**

- **Qué hace**: Mueve el puntero de tu rama actual y el estado del working directory para que coincidan con la última versión de `origin/main`. Esto descarta cualquier cambio local.

### 6. **`git merge origin/main`**

- **Qué hace**: Combina los cambios de la rama remota `origin/main` con tu rama actual.

### 7. **`git rebase origin/main`**

- **Qué hace**: Reaplica tus cambios locales en la parte superior de los cambios traídos desde `origin/main`. Esto es útil para mantener un historial de commits más limpio.

### Diferencia entre `origin/main` y `origin main`:

- **`origin main`**: El primer término `origin` se refiere al repositorio remoto y el segundo `main` a la rama dentro de ese repositorio.
- **`origin/main`**: Este formato con la barra (`/`) se usa cuando estás **consultando o haciendo operaciones sobre las referencias remotas** (como en `git checkout origin/main` o `git log origin/main`).

Si intentas usar algo como `git push origin main`, estás enviando la rama `main` local al repositorio remoto `origin` y no refiriéndote directamente a `origin/main` como un destino explícito.