
GitHub Actions es una herramienta de integración continua (CI) y entrega continua (CD) proporcionada por GitHub, que permite automatizar flujos de trabajo de desarrollo de software directamente en tu repositorio. Con GitHub Actions, puedes definir tareas automáticas para ser ejecutadas en respuesta a eventos como push, pull requests, o creaciones de tags. También es útil para ejecutar pruebas, realizar despliegues automáticos, crear releases, entre otras muchas acciones.
Conceptos clave de GitHub Actions:
1. Workflows (Flujos de trabajo)

Un workflow es un conjunto de trabajos (jobs) que se ejecutan cuando ocurre un evento en tu repositorio (como un push o una pull request). Un workflow está definido en un archivo YAML y se encuentra en el directorio .github/workflows/ de tu repositorio.

Ejemplo de un archivo de workflow:
```yaml
name: CI Pipeline

on: [push, pull_request]

jobs:
  build:
	runs-on: ubuntu-latest
	steps:
	  - uses: actions/checkout@v2
	  - name: Configurar Node.js
		uses: actions/setup-node@v2
		with:
		  node-version: '14'
	  - run: npm install
	  - run: npm test

Este workflow se ejecuta cuando hay un push o una pull request. Instala las dependencias de Node.js y ejecuta los tests.
2. Events (Eventos)

Los eventos son los desencadenantes que hacen que un workflow comience a ejecutarse. Algunos ejemplos de eventos comunes son:

    push: Se ejecuta cuando se hace un push a cualquier rama del repositorio o una rama específica.
    pull_request: Se ejecuta cuando se abre o actualiza un pull request.
    schedule: Permite ejecutar acciones de forma periódica (cron jobs).
    workflow_dispatch: Permite ejecutar manualmente un flujo de trabajo desde la interfaz de GitHub.

Ejemplo de usar un evento de schedule:

on:
  schedule:
    - cron: '0 0 * * *' # Se ejecuta todos los días a la medianoche

3. Jobs (Trabajos)

Un workflow puede contener uno o más jobs, que son unidades de trabajo que se ejecutan. Los jobs se ejecutan en runners, que son máquinas virtuales que pueden ser autohospedadas o proporcionadas por GitHub. Los jobs pueden ejecutarse en paralelo o en secuencia.

Cada job puede tener varias propiedades:

    runs-on: Define el sistema operativo en el que se ejecutará el trabajo (ejemplo: ubuntu-latest, windows-latest).
    steps: Son las acciones que se ejecutan en un job. Pueden ser comandos o el uso de acciones predefinidas de GitHub.

Ejemplo de múltiples jobs:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Compilando la aplicación"

  test:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Ejecutando tests"

4. Steps (Pasos)

Un job se divide en pasos (steps), que son las acciones específicas que se ejecutan dentro de un job. Los pasos pueden usar acciones o ejecutar comandos de shell.

Ejemplo de pasos:

steps:
  - name: Clonar el repositorio
    uses: actions/checkout@v2

  - name: Ejecutar script de prueba
    run: npm test

5. Actions (Acciones)

Las acciones son comandos o conjuntos de comandos reutilizables que puedes usar en tus steps. Existen muchas acciones predefinidas que puedes usar, y también puedes crear tus propias acciones. GitHub proporciona un marketplace donde puedes encontrar acciones de terceros para tareas comunes, como instalar dependencias, ejecutar pruebas, desplegar a servicios cloud, etc.

Ejemplo de usar una acción:

- name: Configurar Node.js
  uses: actions/setup-node@v2
  with:
    node-version: '14'

6. Runners

Los runners son las máquinas que ejecutan los jobs de tus workflows. GitHub ofrece runners alojados en la nube, donde puedes ejecutar tus jobs en diferentes sistemas operativos (ubuntu, windows, macOS). También puedes configurar runners autohospedados si deseas ejecutar los jobs en tu propia infraestructura.

Ejemplo de un runner:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Compilando en Ubuntu"

7. Secrets (Secretos)

Los secretos son valores sensibles, como claves API o credenciales, que no quieres exponer en tu código. GitHub Actions te permite almacenar secretos de manera segura y utilizarlos en los workflows. Puedes definir secretos en la configuración de tu repositorio y luego referenciarlos en los workflows.

Ejemplo de uso de un secreto:

- name: Desplegar a producción
  run: deploy.sh
  env:
    API_KEY: ${{ secrets.MY_API_KEY }}

8. Matrices

Las matrices te permiten ejecutar el mismo job con diferentes configuraciones, como diferentes versiones de un lenguaje de programación o en diferentes sistemas operativos.

Ejemplo de uso de matrices:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [12, 14, 16]
    steps:
      - uses: actions/checkout@v2
      - name: Configurar Node.js
        uses: actions/setup-node@v2
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm install
      - run: npm test

En este caso, se ejecutarán los tests con las versiones 12, 14 y 16 de Node.js.
Ventajas de usar GitHub Actions:

    Automatización de tareas: Puedes automatizar tests, compilaciones, despliegues y cualquier otra tarea repetitiva.
    Integración con GitHub: GitHub Actions está profundamente integrado con GitHub, lo que facilita responder a eventos del repositorio.
    Marketplace: Existe una gran cantidad de acciones ya creadas que puedes usar para realizar tareas comunes.
    Matrices: Ejecuta tus tests o compilaciones en diferentes entornos sin esfuerzo adicional.
    Alojamiento gratuito: GitHub proporciona runners gratuitos para proyectos públicos y cuotas gratuitas para proyectos privados.

Ejemplo completo

name: CI Pipeline

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9]
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python ${{ matrix.python-version }}
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -r requirements.txt
      - run: pytest

Este pipeline ejecuta tests en varias versiones de Python cuando se hace push o pull request al repositorio.

Con GitHub Actions, puedes construir flujos de trabajo personalizados para cualquier escenario, desde la ejecución de pruebas hasta el despliegue en producción, de manera automatizada y eficiente.

## Jobs

Los jobs son uno de los componentes clave en los workflows de GitHub Actions. Un job es un conjunto de pasos que se ejecutan en un entorno específico (como un contenedor, una máquina virtual o un runner autohospedado). Cada job se ejecuta en un entorno independiente y puede ser configurado para ejecutarse en paralelo o en secuencia con otros jobs dentro de un workflow.
Estructura Básica de un Job

Un job se define dentro de un workflow YAML bajo la clave jobs, y cada job tiene varias configuraciones que controlan cómo y dónde se ejecutará. Aquí te explico los componentes más importantes de un job:
1. Nombre del Job

Puedes darle un nombre a cada job, lo que facilita la lectura y comprensión del workflow.

jobs:
  build:
    name: Build and Test Application

En este ejemplo, el job se llama build y tiene el nombre descriptivo Build and Test Application.
2. Runner (Entorno de Ejecución)

Un job se ejecuta en un runner, que es el entorno donde se ejecutan las instrucciones de ese job. GitHub ofrece runners hospedados (por ejemplo, ubuntu-latest, windows-latest, macos-latest) que puedes usar, o puedes configurar tu propio runner autohospedado si necesitas más control.

Ejemplo de configuración de un job para que se ejecute en un runner con Ubuntu:

jobs:
  build:
    runs-on: ubuntu-latest

Otros valores comunes para runs-on son:

    ubuntu-latest (Ubuntu)
    windows-latest (Windows)
    macos-latest (macOS)

3. Steps (Pasos)

Dentro de cada job, puedes definir una serie de steps. Los steps son las acciones o comandos individuales que se ejecutan en ese job. Un step puede ser una acción predefinida (por ejemplo, actions/checkout) o un script personalizado.

Ejemplo de un job con varios pasos:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: |
          python -m unittest discover

En este ejemplo:

    El job tiene 4 pasos: hacer el checkout del código, configurar Python, instalar dependencias, y ejecutar las pruebas.
    uses se usa cuando se utiliza una acción predefinida, como actions/checkout o actions/setup-python.
    run se usa para ejecutar comandos o scripts personalizados, como instalar dependencias o ejecutar pruebas.

4. Condiciones de Ejecución (Dependencias entre Jobs)

Puedes definir dependencias entre jobs. Por defecto, los jobs se ejecutan en paralelo, pero si deseas que un job dependa de otro, puedes usar la clave needs. Esto indica que un job solo se ejecutará después de que otro haya terminado con éxito.

Ejemplo:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy application
        run: ./deploy.sh

En este ejemplo:

    El job deploy solo se ejecutará después de que el job build termine con éxito.

5. Condiciones de Ejecución con if

Puedes usar la condición if para ejecutar un job o un paso solo si se cumplen ciertas condiciones. Esto es útil para controlar la ejecución en base al resultado de otros jobs o al contexto del evento.

Ejemplo:

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Run tests
        run: |
          python -m unittest discover

  deploy:
    runs-on: ubuntu-latest
    needs: test
    if: success()  # Solo se ejecutará si el job "test" es exitoso
    steps:
      - name: Deploy to production
        run: ./deploy.sh

En este ejemplo:

    El job deploy solo se ejecutará si el job test se ha ejecutado correctamente.

6. Matrices (Matrix Builds)

Si necesitas ejecutar un job en varias configuraciones, como diferentes versiones de Python, puedes usar una matriz (matrix). Esto permite ejecutar el mismo conjunto de pasos en diferentes configuraciones de manera paralela.

Ejemplo de un job con una matriz para probar varias versiones de Python:

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9]
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: ${{ matrix.python-version }}

      - name: Run tests
        run: |
          python -m unittest discover

En este ejemplo:

    El job test se ejecutará 3 veces, cada vez con una versión diferente de Python (3.7, 3.8 y 3.9).

7. Artefactos

Un job puede generar artefactos (por ejemplo, archivos generados durante la ejecución del job) que pueden ser usados más adelante, incluso en otros jobs. Se puede usar la acción actions/upload-artifact para subir archivos y actions/download-artifact para descargarlos.

Ejemplo:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Build project
        run: make

      - name: Upload build artifact
        uses: actions/upload-artifact@v2
        with:
          name: build-artifact
          path: ./build/

En este ejemplo:

    Se compila el proyecto y se sube el directorio ./build/ como un artefacto.

Resumen de Componentes de un Job:

    runs-on: Define el entorno donde se ejecutará el job (por ejemplo, ubuntu-latest).
    steps: Define los pasos dentro del job, que pueden ser comandos, acciones predefinidas, o scripts personalizados.
    needs: Define dependencias entre jobs, asegurando que un job se ejecute solo después de otro.
    matrix: Permite ejecutar un job en múltiples configuraciones de forma paralela.
    if: Permite condiciones sobre la ejecución de jobs o pasos.
    artefactos: Se pueden usar para guardar y recuperar archivos generados durante los jobs.

Ejemplo Completo de Workflow con Jobs:

name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: python -m unittest discover

  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to production
        run: ./deploy.sh

En este workflow:

    El job build se ejecuta primero, y luego, si tiene éxito, el job deploy se ejecuta en segundo lugar.



## Create release workflow
```
name: Create release

on:
  push:
    tags:
      - "v*"

permissions:
  contents: write

jobs:
  release:
    name: Release pushed tag
    runs-on: ubuntu-22.04
    steps:
      - name: Create release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          tag: ${{ github.ref_name }}
        run: |
          gh release create "$tag" \
              --repo="$GITHUB_REPOSITORY" \
              --title="${tag#v}" \
              --generate-notes
```

1. on: push con tags

on:
  push:
    tags:
      - "v*"

    on: push: Este es un gatillo (trigger) para ejecutar el workflow. En este caso, el workflow se ejecutará cuando se haga un push (una actualización) en el repositorio.
    tags: ["v*"]: Aquí estamos especificando que el workflow solo se ejecutará cuando se haga push de tags que comiencen con "v". Por ejemplo, si empujas el tag v1.0.0, el workflow se ejecutará.

2. permissions: contents: write

permissions:
  contents: write

    Esta línea define los permisos necesarios para el workflow. En este caso, está otorgando permiso de escritura en el contenido del repositorio (contents: write).
    Esto es importante porque estamos creando una release, lo que implica escribir en el repositorio.

3. jobs y steps

jobs:
  release:
    name: Release pushed tag
    runs-on: ubuntu-22.04
    steps:
      - name: Create release
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          tag: ${{ github.ref_name }}
        run: |
          gh release create "$tag" \
              --repo="$GITHUB_REPOSITORY" \
              --title="${tag#v}" \
              --generate-notes

jobs y steps

    jobs define el conjunto de tareas (jobs) que el workflow debe ejecutar. En este caso, tenemos un único job llamado release.
    steps define las tareas específicas dentro del job. Cada paso es una acción que se ejecutará en el workflow. En este caso, el paso es crear la release.

env y variables

env:
  GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  tag: ${{ github.ref_name }}

    env:: Aquí estamos definiendo variables de entorno que estarán disponibles para los pasos en el job.
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}: GITHUB_TOKEN es un token especial proporcionado automáticamente por GitHub Actions. Se utiliza para autenticar el workflow y darle permisos para interactuar con la API de GitHub. En este caso, se obtiene de los secretos del repositorio (secrets.GITHUB_TOKEN).
        tag: ${{ github.ref_name }}: Esta es una variable de GitHub Actions que contiene el nombre de la referencia que activó el workflow. En este caso, como el workflow se activa por un push de tag, github.ref_name contendrá el nombre del tag (por ejemplo, v1.0.0).

Uso de $ en las variables

Cuando ves algo como ${{ github.ref_name }}, lo que está haciendo es referenciar una variable de contexto de GitHub Actions. Las variables de contexto están entre {{ }}, y pueden ser usadas para obtener información del repositorio, como el nombre del commit, el nombre del tag, el usuario que hizo el push, entre otros.

    $: La $ es una forma de referenciar el valor de la variable. Si ves algo como $tag, el valor de tag es el que se definió previamente en el entorno. En este caso, el valor de tag sería el nombre del tag que activó el workflow.

    Entonces, en este caso:

    gh release create "$tag"

    Esta línea va a usar el valor de tag (por ejemplo, v1.0.0) como el nombre de la release.

Explicación del comando gh release create

gh release create "$tag" \
    --repo="$GITHUB_REPOSITORY" \
    --title="${tag#v}" \
    --generate-notes

    gh release create: Este es el comando para crear una nueva release en GitHub utilizando la CLI de GitHub (gh).
    "$tag": El primer parámetro de este comando es el nombre del tag (como v1.0.0). Este es el tag que se acaba de hacer push, y se usa para crear la release.
    --repo="$GITHUB_REPOSITORY": Esta opción especifica el repositorio donde se creará la release. $GITHUB_REPOSITORY es una variable automática que contiene el nombre del repositorio en formato owner/repo (por ejemplo, mi-usuario/mi-repo).
    --title="${tag#v}": El título de la release. Aquí se está utilizando una operación de expansión de cadena de bash. tag#v elimina el prefijo "v" del nombre del tag. Así que si el tag es v1.0.0, el título de la release será 1.0.0 (sin la "v").
    --generate-notes: Esta opción genera automáticamente las notas de la release, que suelen ser un resumen de los cambios y mejoras.

Resumen

    El archivo de workflow configura un proceso para crear una release automáticamente cuando se hace un push de un tag que comienza con "v".
    Utiliza variables como ${{ github.ref_name }} para capturar el nombre del tag que activó el workflow.
    Usa el comando gh release create para crear la release en GitHub, asignándole el nombre del tag como nombre de la release y generando notas automáticamente.
    Las variables como GITHUB_TOKEN y $GITHUB_REPOSITORY son proporcionadas automáticamente por GitHub Actions para autenticar y gestionar el repositorio en el que se está ejecutando el workflow.

Con este flujo, puedes automatizar la creación de releases cada vez que se empuje un nuevo tag con el prefijo "v".
