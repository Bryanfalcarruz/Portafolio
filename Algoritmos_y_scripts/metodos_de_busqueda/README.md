# Métodos de Búsqueda

Este directorio contiene dos implementaciones clásicas de algoritmos de búsqueda en Python:

- **Búsqueda lineal** (`lineal.py`)
- **Búsqueda binaria** (`binaria.py`)

---

## Descripción de los algoritmos

### Búsqueda lineal
- **Funcionamiento:** Recorre la lista elemento por elemento hasta encontrar el valor buscado o llegar al final.
- **Ventajas:** Funciona en listas ordenadas o desordenadas.
- **Desventajas:** Poco eficiente en listas grandes, ya que su complejidad es **O(n)**.

### Búsqueda binaria
- **Funcionamiento:** Requiere que la lista esté **ordenada**. Compara el elemento central y descarta la mitad de la lista en cada paso, repitiendo hasta encontrar el elemento o agotar las opciones.
- **Ventajas:** Muy eficiente para listas grandes, con complejidad **O(log n)**.
- **Desventajas:** Solo se puede aplicar en listas ordenadas.

---

## Comparación de rendimiento

| Algoritmo | Comparaciones en Lista A | Comparaciones en Lista B | Comparaciones en Lista C |
|-----------|--------------------------|--------------------------|--------------------------|
| Lineal    | 3                        | 7                        | 15                       |
| Binaria   | 2                        | 3                        | 4                        |

**Conclusión:** La **búsqueda binaria** realiza muchas menos comparaciones que la lineal, especialmente en listas grandes. Esto se debe a que divide el rango de búsqueda a la mitad en cada paso. Sin embargo, requiere que la lista esté previamente ordenada.

.....

## python lineal.py
## python binaria.py

## El programa pedirá:
    1.- El número a buscar 
    2.- La lista en la que buscar (por ejemplo: [4, 7, 23]).

Mostrará si el valor fue encontrado y el número de comparaciones realizadas.