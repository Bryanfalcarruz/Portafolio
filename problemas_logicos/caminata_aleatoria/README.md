# Caminata Aleatoria en 2D

Este programa simula una **caminata aleatoria** sobre una cuadrícula de tamaño `2n + 1` puntos de lado, comenzando desde el origen `(0, 0)` y avanzando hasta llegar a cualquiera de los bordes.

---

## 📌 Descripción

En cada paso, el caminante puede moverse **arriba**, **abajo**, **izquierda** o **derecha** con igual probabilidad (`0.25`).  
La simulación termina cuando se alcanza cualquier punto en el borde de la cuadrícula.

El programa muestra:
1. La lista de coordenadas visitadas en el orden en que fueron recorridas.
2. Una representación gráfica de la caminata, donde:
   - `x` = punto visitado.
   - `o` = punto no visitado.

---

## 🔹 Estructura del código

- **`genera_caminata(n)`**  
  Genera la lista de coordenadas recorridas desde `(0, 0)` hasta un borde de la cuadrícula.

- **`grafica_caminata(n, coordenadas)`**  
  Crea una representación en texto de la cuadrícula y marca los puntos visitados.

- **Bloque principal**  
  - Solicita al usuario un entero positivo `n`.
  - Llama a las funciones para generar y graficar la caminata.
  - Muestra los resultados por consola.

---

## 💻 Ejemplo de ejecución

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

## 📊 Complejidad
- La simulación no tiene un número fijo de pasos; la cantidad depende de `n` y de las decisiones aleatorias.
- En promedio, el tiempo de ejecución crece de forma proporcional al área de la cuadrícula.

---

## ▶️ Ejecución

En consola:
```bash
python caminata.py
```
Luego ingrese un número entero positivo para iniciar la simulación.

---

## 📂 Ubicación sugerida en el portafolio
```
problemas_logicos/
└── caminata_aleatoria/
    ├── caminata.py
    └── README.md
```
