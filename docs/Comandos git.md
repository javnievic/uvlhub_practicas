## Cherry-pick 

El comando `git cherry-pick` se utiliza en Git para aplicar cambios de un commit específico de una rama a otra. A diferencia de `git merge` o `git rebase`, que combinan todas las diferencias entre ramas, `git cherry-pick` permite seleccionar y aplicar un commit específico, sin necesidad de integrar toda la historia de cambios de la otra rama.

### ¿Cómo funciona `git cherry-pick`?

Cuando ejecutas `git cherry-pick <commit>`, Git realiza lo siguiente:

1. **Busca el commit** especificado en la historia de tu proyecto.
2. **Aplica los cambios** que introdujo ese commit sobre la rama actual.
3. Crea un nuevo commit con los cambios aplicados, manteniendo el contenido del commit original, pero con un nuevo hash de commit.

### Ejemplo de uso

1. Imagina que tienes dos ramas, `main` y `feature`.
    
2. En `feature` has realizado varios commits, pero solo quieres traer un commit específico a `main`.


## Rebase interactivo 

Ejemplo
git rebase -i HEAD~7 / "hash del commit al que queremos llegar"




### 1. **Configuración Inicial**

- `git config --global user.name "Tu Nombre"`: Establece tu nombre de usuario en Git.
- `git config --global user.email "tuemail@example.com"`: Establece tu correo electrónico para los commits.
- `git config --global core.editor "nombre_editor"`: Establece el editor de texto para Git (por ejemplo, Vim, Nano).

### 2. **Crear o Inicializar un Repositorio**

- `git init`: Inicializa un nuevo repositorio de Git en el directorio actual.
- `git clone <url>`: Clona un repositorio remoto a tu máquina local.

### 3. **Ramas (Branches)**

- `git branch`: Lista las ramas locales.
- `git branch -a`: Lista todas las ramas, incluidas las remotas.
- `git branch <nombre>`: Crea una nueva rama.
- `git checkout <rama>`: Cambia a una rama existente.
- `git checkout -b <nombre>`: Crea y cambia a una nueva rama.
- `git checkout --track origin/<nombre_rama>`: Crea una nueva rama local que rastrea una rama remota.
- `git branch -d <nombre>`: Elimina una rama local.
- `git branch -D <nombre>`: Fuerza la eliminación de una rama local.

### 4. **Añadir y Commitear Cambios**

- `git add <archivo>`: Añade un archivo al área de preparación (staging area).
- `git add .`: Añade todos los cambios en el directorio actual.
- `git commit -m "Mensaje del commit"`: Crea un commit con los cambios del área de preparación.
- `git commit --amend`: Modifica el último commit (útil para cambiar el mensaje o añadir cambios olvidados).

### 5. **Ver el Estado y Cambios**

- `git status`: Muestra el estado actual del repositorio, archivos cambiados, añadidos, etc.
- `git diff`: Muestra los cambios no añadidos al área de preparación.
- `git diff --staged`: Muestra los cambios que ya están en el área de preparación.

### 6. **Sincronización con Repositorios Remotos**

- `git remote -v`: Muestra las URLs de los repositorios remotos.
- `git remote add origin <url>`: Añade un repositorio remoto llamado `origin`.
- `git fetch`: Descarga los datos de las ramas remotas, pero no los fusiona.
- `git pull`: Descarga los cambios del repositorio remoto y los fusiona con tu rama actual.
- `git push`: Envía los cambios locales al repositorio remoto.
- `git push -u origin <rama>`: Sube una rama nueva al remoto y la configura para rastreo.

### 7. **Fusiones (Merges) y Rebases**

- `git merge <rama>`: Fusiona la rama especificada en la rama actual.
- `git merge --no-ff <rama>`: Realiza una fusión con commit explícito, incluso si es una fusión fast-forward.
- `git rebase <rama>`: Reaplica los commits de la rama actual sobre la rama especificada (útil para mantener un historial lineal).
- `git rebase --continue`: Continúa un rebase después de resolver conflictos.
- `git rebase --abort`: Cancela el rebase y vuelve al estado anterior.

### 8. **Revertir Cambios**

- `git reset <archivo>`: Quita un archivo del área de preparación.
- `git reset --hard <commit>`: Restaura el repositorio al estado del commit especificado, eliminando los cambios locales.
- `git revert <commit>`: Crea un nuevo commit que revierte los cambios de un commit anterior, manteniendo el historial.
- `git checkout -- <archivo>`: Descarta los cambios locales en un archivo.

### 9. **Historial**

- `git log`: Muestra el historial de commits.
- `git log --oneline`: Muestra el historial de commits en una sola línea por commit.
- `git log --graph --oneline`: Muestra el historial de commits en un gráfico con una línea por commit.
- `git log -p`: Muestra el historial junto con los cambios introducidos en cada commit.
- `git show <commit>`: Muestra los cambios y detalles de un commit específico.

### 10. **Stashing (Guardar Cambios Temporales)**

- `git stash`: Guarda los cambios actuales sin commitearlos.
- `git stash pop`: Aplica los cambios guardados con `git stash` y los elimina de la lista de stashes.
- `git stash list`: Muestra la lista de stashes.
- `git stash drop`: Elimina un stash específico.

### 11. **Etiquetas (Tags)**

- `git tag`: Lista las etiquetas del repositorio.
- `git tag <nombre>`: Crea una nueva etiqueta ligera.
- `git tag -a <nombre> -m "Mensaje de la etiqueta"`: Crea una etiqueta anotada con un mensaje.
- `git push origin <nombre_etiqueta>`: Sube una etiqueta al repositorio remoto.

### 12. **Revisión y Resolución de Conflictos**

- `git diff`: Ver las diferencias entre archivos antes de fusionar.
- `git merge --abort`: Aborta un proceso de fusión con conflictos.
- `git log --merge`: Ver qué archivos están causando conflictos durante una fusión.
- `git status`: Ver los archivos en conflicto durante una fusión.

### 13. **Submódulos (Submodules)**

- `git submodule add <url> <directorio>`: Añade un submódulo al proyecto.
- `git submodule init`: Inicializa los submódulos.
- `git submodule update`: Descarga los contenidos de los submódulos.

### 14. **Eliminar Archivos**

- `git rm <archivo>`: Elimina un archivo y lo añade al área de preparación.
- `git rm --cached <archivo>`: Elimina un archivo del repositorio pero lo mantiene en el disco local.

### 15. **Comandos Avanzados**

- `git cherry-pick <commit>`: Aplica los cambios de un commit específico en la rama actual.
- `git bisect start`: Inicia el proceso de búsqueda binaria para encontrar el commit que introdujo un error.
- `git reflog`: Muestra el historial de todos los comandos de Git que han afectado al repositorio.

Esta lista cubre la mayoría de las operaciones comunes en Git y sus variantes más importantes. Puedes profundizar en cada comando con `git <comando> --help` para más detalles.