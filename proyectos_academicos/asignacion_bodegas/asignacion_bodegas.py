import numpy as np
import matplotlib.pyplot as plt

def leer_coordenadas(nombre_archivo):
    archivo = open(nombre_archivo)
    lista = []
    linea = archivo.readline()
    while linea != "":
        partes = linea.split()
        x = int(partes[0])
        y = int(partes[1])
        lista.append([x, y])
        linea = archivo.readline()
    archivo.close()
    return lista

def distancia(p1, p2):
    distanciacuadrada = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    return np.sqrt(distanciacuadrada)

def distancias_por_bodega(clientes, bodega):
    distancias = []
    i = 0
    while i < len(clientes):
        d = distancia(clientes[i], bodega)
        distancias.append(d)
        i += 1
    return distancias

def recorrido_optimo(bodega, clientes):
    clientes_restantes = clientes.copy()
    recorrido = [bodega]
    actual = bodega
    while len(clientes_restantes) > 0:
        menor_distancia = distancia(actual, clientes_restantes[0])
        mas_cercano = clientes_restantes[0]
        i = 1
        while i < len(clientes_restantes):
            d = distancia(actual, clientes_restantes[i])
            if d < menor_distancia:
                menor_distancia = d
                mas_cercano = clientes_restantes[i]
            i += 1
        recorrido.append(mas_cercano)
        clientes_restantes.remove(mas_cercano)
        actual = mas_cercano
    return recorrido

def graficar_puntos(clientes, bodegas):
    clientes_x = []
    clientes_y = []
    i = 0
    while i < len(clientes):
        clientes_x.append(clientes[i][0])
        clientes_y.append(clientes[i][1])
        i += 1
    bodegas_x = []
    bodegas_y = []
    i = 0
    while i < len(bodegas):
        bodegas_x.append(bodegas[i][0])
        bodegas_y.append(bodegas[i][1])
        i += 1
    plt.figure()
    plt.scatter(clientes_x, clientes_y, c='blue', label='Clientes')
    plt.scatter(bodegas_x, bodegas_y, c='red', marker='s', label='Bodegas')
    plt.title('Ubicación de clientes y bodegas')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=4)
    plt.tight_layout()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def graficar_asignacion(asignacion, bodegas):
    colores = ['blue', 'green', 'orange', 'purple', 'cyan', 'magenta', 'grey']
    plt.figure()
    i = 0
    while i < len(asignacion):
        clientes_x = []
        clientes_y = []
        j = 0
        while j < len(asignacion[i]):
            clientes_x.append(asignacion[i][j][0])
            clientes_y.append(asignacion[i][j][1])
            j += 1
        plt.scatter(clientes_x, clientes_y, c=colores[i % len(colores)], label="Bodega " + str(i+1))
        i += 1
    bodegas_x = [b[0] for b in bodegas]
    bodegas_y = [b[1] for b in bodegas]
    plt.scatter(bodegas_x, bodegas_y, c='red', marker='s', label='Bodegas')
    plt.title('Clientes asignados a cada bodega')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=4)
    plt.tight_layout()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def graficar_recorridos(bodegas, asignacion):
    colores = ['blue', 'green', 'orange', 'purple', 'cyan', 'magenta','grey']
    plt.figure()
    i = 0
    while i < len(bodegas):
        recorrido = recorrido_optimo(bodegas[i], asignacion[i])
        recorrido.append(bodegas[i])  # <- agrega la bodega al final del recorrido
        x_coords = []
        y_coords = []
        j = 0
        while j < len(recorrido):
            x_coords.append(recorrido[j][0])
            y_coords.append(recorrido[j][1])
            j += 1
        plt.plot(x_coords, y_coords, marker='o', label="Recorrido Bodega " + str(i+1), color=colores[i % len(colores)])
        i += 1
    bodegas_x = [b[0] for b in bodegas]
    bodegas_y = [b[1] for b in bodegas]
    plt.scatter(bodegas_x, bodegas_y, c='red', marker='s', s=100, label='Bodegas')
    plt.title('Recorridos por bodega')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=4)
    plt.tight_layout()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

#Entrada
nombre_bodegas = input("Ingrese nombre del archivo de bodegas: ")
nombre_clientes = input("Ingrese nombre del archivo de clientes: ")

#Leer coordenadas
bodegas = leer_coordenadas(nombre_bodegas)
clientes = leer_coordenadas(nombre_clientes)

#Gráfico inicial
graficar_puntos(clientes, bodegas)

#Calcular distancias
todas_las_distancias = []
i = 0
while i < len(bodegas):
    distancias = distancias_por_bodega(clientes, bodegas[i])
    distancias.sort()
    todas_las_distancias.append(distancias)
    i += 1

#Asignaciones
asignacion = []
asignados_por_bodega = []
i = 0
while i < len(bodegas):
    asignacion.append([])
    asignados_por_bodega.append(0)
    i += 1

#Limite de clientes por bodega
cantidad_clientes = len(clientes)
cantidad_bodegas = len(bodegas)
base = cantidad_clientes // cantidad_bodegas
extra = cantidad_clientes % cantidad_bodegas
limites = []
i = 0
while i < cantidad_bodegas:
    if i < extra:
        limites.append(base + 1)
    else:
        limites.append(base)
    i += 1

#Asignar clientes
cliente_actual = 0
while cliente_actual < len(clientes):
    distancias_cliente = []
    j = 0
    while j < len(bodegas):
        d = distancia(clientes[cliente_actual], bodegas[j])
        distancias_cliente.append((d, j))
        j += 1
    distancias_cliente.sort()
    k = 0
    asignado = False
    while k < len(distancias_cliente) and not asignado:
        indice = distancias_cliente[k][1]
        if asignados_por_bodega[indice] < limites[indice]:
            asignacion[indice].append(clientes[cliente_actual])
            asignados_por_bodega[indice] += 1
            asignado = True
        k += 1
    cliente_actual += 1

#mostrar asignaciones y graficar
i = 0
while i < len(asignacion):
    print("Bodega", i+1, "recibe", len(asignacion[i]), "clientes:", asignacion[i])
    i += 1
graficar_asignacion(asignacion, bodegas)

i = 0
while i < len(bodegas):
    recorrido = recorrido_optimo(bodegas[i], asignacion[i])
    print("Recorrido óptimo para bodega", i+1, ":", recorrido)
    i += 1
graficar_recorridos(bodegas, asignacion)