ordenamiento = eval(input("Ingrese lista: "))
i = 0
comparaciones = 0
intercambios = 0

while i < len(ordenamiento) - 1:
    min = i
    j = i + 1
    while j < len(ordenamiento):
        comparaciones += 1
        if ordenamiento[j] < ordenamiento[min]:
            min = j
        j = j + 1
    if min != i:
        aux = ordenamiento[i]
        ordenamiento[i] = ordenamiento[min]
        ordenamiento[min] = aux
        intercambios += 1
    i = i + 1

print("Lista ordenada:", ordenamiento)
print("Comparaciones:", comparaciones)
print("Intercambios:", intercambios)