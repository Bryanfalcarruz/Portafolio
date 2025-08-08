from random import choice

def genera_caminata(n):
    x, y = 0, 0
    coordenadas = [[x, y]]
    direcciones = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    while -n < x < n and -n < y < n:
        paso = choice(direcciones)
        x += paso[0]
        y += paso[1]
        coordenadas.append([x, y])
    return coordenadas

def grafica_caminata(n, coordenadas):
    tamaño = 2 * n + 1
    mapa = []
    i = 0
    while i < tamaño:
        fila = []
        j = 0
        while j < tamaño:
            fila.append("o")
            j += 1
        mapa.append(fila)
        i += 1
    k = 0
    while k < len(coordenadas):
        x, y = coordenadas[k]
        fila = y + n
        columna = x + n
        if 0 <= fila < tamaño and 0 <= columna < tamaño:
            mapa[fila][columna] = "x"
        k += 1
    resultado = ""
    i = 0
    while i < len(mapa):
        j = 0
        fila_str = ""
        while j < len(mapa[i]):
            fila_str += mapa[i][j]
            j += 1
        resultado += fila_str + "\n"
        i += 1
    return resultado

# BLOQUE PRINCIPAL
# ENTRADA
numero = int(input("Ingrese un número entero positivo: "))
# PROCESO
caminata = genera_caminata(numero)
grafico = grafica_caminata(numero, caminata)
# SALIDA
print("La lista de puntos visitados en la caminata es:")
print(caminata)
print("La representación gráfica de la caminata es:")
print(grafico)