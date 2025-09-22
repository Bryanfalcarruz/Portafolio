
Este programa implementa el **Método de Herón** (también conocido como Método de Héroe de Alejandría) para aproximar la raíz cuadrada de un número positivo.

---

## Descripción del algoritmo

El método consiste en:

1. **Inicialización:** Se comienza con un valor inicial positivo arbitrario (`candidato`), que será la estimación inicial de la raíz cuadrada.
2. **Promedio:** Se calcula el promedio entre el valor actual de `candidato` y el cociente `S / candidato`.
3. **Repetición:** El proceso se repite hasta que la diferencia absoluta entre `S` y `candidato²` sea menor o igual a la tolerancia establecida.

Este método es iterativo y converge rápidamente a la raíz cuadrada, incluso con un candidato inicial poco preciso.  
Si el candidato inicial está muy alejado del valor real, el algoritmo tardará algunas iteraciones más en converger, pero aun así alcanzará la precisión deseada gracias a su naturaleza iterativa.


---

## Ejemplo de ejecución

Entrada:
```
Ingrese el número positivo S: 25
Ingrese el valor inicial del candidato: 5
Ingrese la tolerancia: 0.0001
```

Salida:
```
La raíz cuadrada aproximada de 25.0 es: 5.0
```

---
## Ejecución
ingrese:
1. **S:** Número positivo del que se desea calcular la raíz cuadrada.
2. **Candidato:** Estimación inicial.
3. **Tolerancia:** Precisión deseada para la aproximación.

---
