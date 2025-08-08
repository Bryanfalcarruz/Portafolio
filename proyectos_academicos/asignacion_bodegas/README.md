# Asignación de bodegas a clientes

Este proyecto fue desarrollado como parte de una asignatura de **Fundamentos de la Programación**, cuyo objetivo era introducir conceptos básicos de lógica computacional, estructuras de control y algoritmos.  
No fue pensado como un curso de Python, por lo que se evitó el uso de funciones avanzadas, bibliotecas externas o estructuras propias del lenguaje. Con la excepción de herramientas indispensables para la visualización —como matplotlib— se procuró mantener el código lo más general posible.

## Descripción del proyecto

Dado un conjunto de coordenadas de clientes y bodegas, el programa asigna cada cliente a la bodega más cercana, intentando mantener una distribución equitativa. Luego, genera gráficos para visualizar:

- Las ubicaciones originales
- Las asignaciones de clientes a bodegas
- Los recorridos óptimos de reparto

## Estructura de carpetas

asignacion_bodegas/
├── asignacion_bodegas.py
├── informe_asignacion_bodegas.pdf
├── README.md
└── datos/
├── coordenadas_clientes.txt
└── coordenadas_bodegas.txt

## Uso

1. Se requiere tener Python 3 instalado.

2. Los archivos de coordenadas deben estar ubicados dentro de la carpeta datos/.

3. El script se ejecuta desde una terminal o consola con el siguiente comando: 

<python asignacion_bodegas.py>

Cuando se te solicite, escribe solo el nombre del archivo sin la ruta ni extensión. Por ejemplo:

Nombre del archivo de coordenadas de clientes: clientes_1.txt
Nombre del archivo de coordenadas de bodegas: bodegas_1.txt

El programa generará tres gráficos que se mostrarán uno a uno:
-Ubicaciones iniciales
-Asignación de colores por bodega
-Recorridos óptimos

## Informe
El archivo informe_asignacion_bodegas.pdf contiene el análisis metodológico y explicación detallada del problema y su solución.
