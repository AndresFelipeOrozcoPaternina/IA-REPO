# Entrega de ejercicios de inteligencia artificial

**Repositorio para entregar:** [AndresFelipeOrozcoPaternina/IA-REPO](https://github.com/AndresFelipeOrozcoPaternina/IA-REPO).

| Ejercicio | Carpeta | Entregable | Prompt |
| --- | --- | --- | --- |
| 1. Algoritmo | `actividad1/` | [Ordenar tres números](actividad1/ordenar.py) y [pruebas y explicación](actividad1/ENTREGA.md) | [Prompt de Python](actividad1/PROMPT.md) |
| 2. Archivo descargable | `actividad2/` | [Archivo original aportado](actividad2/archivo_descargable.txt) y [versión organizada](actividad2/ENTREGA.md) | Consultas incluidas en ambos archivos |
| 3. Página web con IA | `actividad3/` | [Código de la página](actividad3/proyecto/index.html) y [descripción del proyecto](actividad3/ENTREGA.md) | [Prompt utilizado con v0](actividad3/PROMPT.md) |

El algoritmo contempla repetidos, negativos y todos iguales. El archivo de texto del ejercicio 2 conserva sin cambios el contenido enviado para «Tres cupos, ocho estudiantes»; su versión organizada incluye la segunda respuesta resumida y la conclusión completada.

Para ejecutar la primera actividad desde la raíz del repositorio:

```powershell
py actividad1/ordenar.py
```

La herramienta utilizada en el ejercicio 3 fue **v0**. [Página compartida en Vercel](https://corecampus-3d-training-platform-1e4.vercel.app/) y [repositorio del proyecto del equipo](https://github.com/wiliend69/IA).

Para abrir la copia local de la página:

```powershell
py -m http.server 8000 --directory actividad3/proyecto
```

Abre `http://localhost:8000`. Requiere internet para las bibliotecas externas y un navegador compatible con WebGL. Detén el servidor con `Ctrl+C`.

## Cómo entregar

1. Sube estos archivos a GitHub y pega el enlace de este repositorio en el texto en línea.
2. Verifica que el TL pueda abrirlo: acceso público o permiso para su cuenta. Si es público, comprueba el enlace en una ventana privada.
3. Crea y sube el ZIP del repositorio en la plataforma de entrega.

La accesibilidad externa y la ejecución completa de la página en navegador no quedaron verificadas desde este entorno. Se comprobaron los enlaces locales y los recursos locales del HTML.

El ZIP final lo creará el estudiante. `actividad3/index.zip` es el archivo fuente recibido del proyecto web, no el ZIP final de la entrega.
