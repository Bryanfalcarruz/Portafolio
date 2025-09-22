# Caminata Aleatoria en 2D

Este programa simula una **caminata aleatoria** sobre una cuadrícula de tamaño `2n + 1` puntos de lado, comenzando desde el origen `(0, 0)` y avanzando hasta llegar a cualquiera de los bordes.

---

## Descripción

En cada paso, el caminante puede moverse **arriba**, **abajo**, **izquierda** o **derecha** con igual probabilidad (`0.25`).  
La simulación termina cuando se alcanza cualquier punto en el borde de la cuadrícula.

El programa muestra:
1. La lista de coordenadas visitadas en el orden en que fueron recorridas.
2. Una representación gráfica de la caminata, donde:
   - `x` = punto visitado.
   - `o` = punto no visitado.

---

## Estructura del código

- **`genera_caminata(n)`**  
  Genera la lista de coordenadas recorridas desde `(0, 0)` hasta un borde de la cuadrícula.

- **`grafica_caminata(n, coordenadas)`**  
  Crea una representación en texto de la cuadrícula y marca los puntos visitados.

- **Bloque principal**  
  - Solicita al usuario un entero positivo `n`.
  - Llama a las funciones para generar y graficar la caminata.
  - Muestra los resultados por consola.

---

## Ejemplo de ejecución

Entrada:
```
Ingrese un número entero positivo: 3
```

Salida:
```
La lista de puntos visitados en la caminata es:
[[0, 0], [-1, 0], [-1, -1], [0, -1], [-1, -1], [0, -1], [1, -1], [1, -2], [1, -3]]

La representación gráfica de la caminata es:
ooooooo
ooooooo
ooooooo
ooxxooo
ooxxxoo
ooooxoo
ooooxoo
```

---


## Ejecución

grese un número entero positivo `n`, que define la **distancia máxima desde el centro hasta cualquier borde de la cuadrícula**.  
El campo de juego tendrá un tamaño de `2n + 1` puntos por lado.  

Por ejemplo:
- Si `n = 3`, la cuadrícula abarcará desde la coordenada `(-3, -3)` hasta `(3, 3)`, formando un campo de 7 × 7 puntos.