# Actividad: ordenar tres números enteros

## Algoritmo funcionando

El programa está en `ordenar.py`. Para ejecutarlo desde esta carpeta:

```powershell
py ordenar.py
```

Introduce un entero por cada pregunta. Por ejemplo, con 7, 2 y 5 muestra `2 5 7`.
Se utiliza `int` para convertir la entrada y `print` para mostrar la salida, tal como requiere la plantilla. La lógica usa exclusivamente `if`, `else` y comparaciones, sin listas, ciclos ni `sorted()`.

## Explicación en tres líneas

1. Primero compara a con b para conocer el orden entre los dos primeros números.
2. Después compara el tercer número con los anteriores para determinar su posición.
3. Imprime los tres de menor a mayor; las comparaciones con `<=` también permiten repetidos.

## Registro de pruebas

Se probaron los archivos aportados por el estudiante, identificados como Gemini y Claude. Al fragmento de Claude se le agregaron las entradas que faltaban, conservando su ordenamiento.

| Caso | Entrada | Esperado | Tu algoritmo | Gemini | Claude |
| --- | --- | --- | --- | --- | --- |
| Desordenados | 7, 2, 5 | 2, 5, 7 | ✅ | ✅ | ✅ |
| Desordenados (al revés) | 9, 5, 1 | 1, 5, 9 | ✅ | ✅ | ✅ |
| Repetidos | 5, 1, 5 | 1, 5, 5 | ✅ | ✅ | ✅ |
| Negativos | -3, 5, -1 | -3, -1, 5 | ✅ | ✅ | ✅ |
| Todos iguales | 4, 4, 4 | 4, 4, 4 | ✅ | ✅ | ✅ |

Las cinco pruebas se ejecutaron con Python 3.15.0. También se comprobaron las 125 combinaciones posibles de tres enteros entre -2 y 2, y todas pasaron. El comprobador externo utilizó ciclos y `sorted()` como referencia; estos no aparecen en el algoritmo entregado.

## Comparación de las tres soluciones

Instrucción de referencia para las propuestas:

> Escribe un programa en Python que pida tres números enteros y los muestre de menor a mayor. Usa solo input, if, else y comparaciones: sin listas, ciclos ni sorted(). Explica en tres líneas cómo funciona.

Los tres programas pasaron los cinco casos de la tabla y las 125 combinaciones adicionales. Las marcas de acierto indican que la salida es correcta; el cumplimiento de las restricciones se analiza por separado.

| Solución | Archivo | Estrategia | Comparaciones por ejecución | Cumplimiento estricto |
| --- | --- | --- | --- | --- |
| Tu algoritmo | `ordenar.py` | Compara a y b y ubica c con decisiones anidadas | 2 o 3 | Sí |
| Gemini | `alternativa_a.py` | Ordena los pares a-b, a-c y b-c mediante intercambios | 3 | Usa asignación múltiple adicional |
| Claude | `alternativa_b.py` | Ordena los pares a-b, b-c y a-b mediante intercambios | 3 | Usa asignación múltiple adicional; se añadieron las entradas |

Ninguna solucion usa listas, ciclos ni `sorted()`. Gemini y Claude usan intercambios como `a, b = b, a`: son asignaciones multiples y no listas, pero incorporan una operación adicional a la logica de solo `if`, `else` y comparaciones solicitada. El algoritmo propio se ajusta a esa restricción sin intercambios.

### Gemini: explicacion en tres lineas

1. Compara a con b y los intercambia si a es mayor.
2. Compara a con c y los intercambia si hace falta, dejando el menor en a.
3. Compara b con c, ordena ese par e imprime a, b y c.

### Claude: explicacion en tres lineas

1. Compara a con b e intercambia sus valores si están desordenados.
2. Compara b con c y coloca el mayor de los tres en c.
3. Vuelve a comparar a con b para ordenar el par restante e imprime el resultado.

## Solucion elegida

Se elige `ordenar.py` porque pasa todas las pruebas y respeta la restriccion de resolver el orden mediante decisiones y comparaciones, sin intercambiar variables. Primero establece el orden entre a y b y despues ubica c, por lo que resulta facil de explicar a partir de la plantilla inicial. Gemini y Claude tambien producen las salidas correctas, pero emplean asignación múltiple y siempre hacen tres comparaciones; el algoritmo propio puede resolver algunas entradas con dos.

## Pregunta para discutir con el clan

Para garantizar el orden de tres números distintos se necesitan como mínimo **tres comparaciones en el peor caso**. Existen seis órdenes posibles: dos comparaciones solo distinguen hasta cuatro resultados y tres permiten hasta ocho. Este algoritmo realiza dos comparaciones en algunas entradas y tres en las demás.
