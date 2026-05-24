# Buenas Prácticas en Programación para Ciencia de Datos

Este proyecto muestra el proceso de optimización de un algoritmo para encontrar números primos, aplicando mejoras de rendimiento y documentando los resultados con medición de tiempos y profiling.

---

## Parte 1: Código Original (Sin Optimización)
- Crear `codigo_original.py` con un algoritmo que busca números primos en el rango de 1 a 100,000.
- Ejecutar el código y registrar el tiempo de ejecución mostrado en consola.

---

## Parte 2: Optimización del Código
- Crear una rama en Git llamada `optimizacion-codigo`.
- Aplicar las siguientes mejoras:
  - Iterar solo hasta la raíz cuadrada de *n*.
  - Usar **list comprehensions** para generar listas de manera eficiente.
  - Implementar **NumPy** para acelerar operaciones con arrays.
- Subir el código optimizado a GitHub con un commit descriptivo.

---

## Parte 3: Medición de Tiempos y Profiling
- Utilizar **cProfile** para analizar tiempos de ejecución y detectar funciones críticas.
- Comparar:
  - Tiempo del código original vs. optimizado.
  - Funciones que más tiempo consumen según `profiling_optimizado.prof`.
- Generar gráficos con **Matplotlib** para visualizar:
  - Distribución de tiempos de ejecución.
  - Comparativa entre código original y optimizado.

---

## Resultados Ejemplares
| Versión                                      | Tiempo (segundos) |
|----------------------------------------------|-------------------|
| Original (sin optimizar)                     | 73.22532 s        |
| Optimizado (raíz cuadrada + list comprehension + NumPy) | 0.0166 s         |

---

## Tecnologías utilizadas
- Python 3.13
- NumPy
- Matplotlib
- Git / GitHub
- cProfile & pstats
