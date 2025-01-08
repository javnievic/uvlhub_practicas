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

