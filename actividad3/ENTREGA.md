# Actividad 3: concurso de creación de una página con IA

## ¿En qué consistía la actividad?

Participamos en un concurso para crear una página web usando inteligencia artificial. Utilizamos **v0** y le dimos las instrucciones de una plataforma de formación corporativa en 3D. La idea era que una persona pudiera recorrer un campus con un avatar, entrar a clases, resolver retos y descansar con minijuegos.

## Proyecto presentado

**Nombre:** CoreCampus — plataforma de formación 3D.

- **IA utilizada:** v0, según lo reportado por el equipo.
- **Repositorio compartido:** [GitHub — wiliend69/IA](https://github.com/wiliend69/IA).
- **Página compartida:** [CoreCampus en Vercel](https://corecampus-3d-training-platform-1e4.vercel.app/).
- **Instrucciones del proyecto:** [requisitos y prompt](PROMPT.md).
- **Archivo recibido:** [index.zip](index.zip).
- **Código extraído:** [proyecto/index.html](proyecto/index.html).

## Lo que pedimos a la IA

Le pedimos una página con un mundo 3D visto desde arriba y una cámara que siguiera al personaje. Antes de entrar, el usuario debía escribir su nombre y personalizar su avatar.

El campus debía tener una zona central de descanso, un área de tecnología a la derecha, un área de inglés y habilidades blandas a la izquierda y una zona de juegos en el piso superior. También solicitamos retos de HTML e inglés, clasificaciones separadas y una barra de energía para limitar los juegos y motivar la participación en las clases.

## Material entregado

El ZIP contiene una página con **HTML, CSS y JavaScript**, con referencias a **Three.js y Bootstrap**. El código está separado en archivos para el avatar, el mundo, los retos, el contenido de clases, la interfaz, el estado del jugador y los minijuegos. El archivo de estado incluye guardado local del progreso y una energía inicial y máxima de 5; el de minijuegos define un costo de 2,5 por sesión.

Esta descripción corresponde a la revisión de los archivos recibidos. No representa una prueba completa del funcionamiento en navegador ni confirma que la versión publicada sea idéntica al ZIP. No se incluyen resultados ni posición en el concurso porque no fueron informados.

## Cómo abrir el proyecto localmente

Desde la raíz del repositorio:

```powershell
py -m http.server 8000 --directory actividad3/proyecto
```

Después abre `http://localhost:8000` en el navegador. Se necesita conexión a internet para cargar las bibliotecas externas y un navegador con WebGL. Para detener el servidor, presiona `Ctrl+C` en la terminal.

## Conclusión

En esta actividad usamos v0 para convertir una idea en una propuesta de página web. Nos tocó explicar qué espacios queríamos, cómo se movería el personaje y qué reglas tendrían las clases y los juegos. Aprendimos que dar instrucciones claras ayuda a orientar el resultado, pero también hay que revisar lo que genera la IA. Una página puede verse bien y aun así necesitar pruebas para comprobar que sus funciones cumplen lo solicitado.
