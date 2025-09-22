 Métodos de Ordenamiento (Selección, Inserción y Burbuja)

Este directorio incluye tres implementaciones clásicas de ordenamiento en Python y un resumen comparativo de su rendimiento en distintos casos.

- `seleccion.py` — Ordenamiento por **selección** (Selection sort)
- `insercion.py` — Ordenamiento por **inserción** (Insertion sort)
- `burbuja.py` — Ordenamiento **burbuja** (Bubble sort)

---

## Descripción breve de cada algoritmo

### Selección
- Recorre el arreglo buscando el mínimo en la parte no ordenada y lo coloca al inicio.


### Inserción
- Toma cada elemento y lo inserta en la posición correcta de la parte ya ordenada.


### Burbuja
- Compara pares adyacentes e intercambia si están en orden incorrecto; repite varias pasadas.


---

## Resultados empíricos (según planilla del laboratorio)

Listas de prueba (A, B, C) y conteo de **intercambios** y **comparaciones** por algoritmo.

**Intercambios**

| Algoritmo | A | B | C |
|-----------|---|---|---|
| Selección | 6 | 0 | 4 |
| Inserción | 23 | 7 | 28 |
| Burbuja   | 18 | 0 | 28 |

**Comparaciones**

| Algoritmo | A | B | C |
|-----------|---|---|---|
| Selección | 28 | 28 | 28 |
| Inserción | 25 | 7  | 35 |
| Burbuja   | 28 | 28 | 28 |

**Conclusiones rápidas**
- En la lista **B** (ya ordenada) Inserción realiza pocas comparaciones y pocos intercambios → muy eficiente cuando la entrada está casi ordenada.
- Selección y Burbuja realizan siempre un número parecido de comparaciones (≈ n²/2), independientemente del estado inicial.
- Burbuja puede ser competitivo con bandera de corte temprano; la versión de este laboratorio no incluye esa optimización.

---

---

## Criterio de uso

**Inserción**: cuando esperas datos casi ordenados o arreglos pequeños; además es estable.
**Selección**: simple para entender y con pocos movimientos de elementos; útil cuando copiar o intercambiar elementos cuesta en términos de recursos.
- **Burbuja**: no suele ser práctico en entornos reales debido a su baja eficiencia; con una bandera de optimización puede servir para detectar arrays ya ordenados.
---
