burbuja = eval(input("Ingrese lista: "))
i = 0
largo = len(burbuja)
comparaciones = 0
intercambios = 0

while i < largo:
    j = largo - 1
    while j > i:
        comparaciones += 1
        if burbuja[j] < burbuja[j - 1]:
            aux = burbuja[j]
            burbuja[j] = burbuja[j - 1]
            burbuja[j - 1] = aux
            intercambios += 1
        j = j - 1
    i = i + 1

print("Lista ordenada:", burbuja)
print("Comparaciones:", comparaciones)
print("Intercambios:", intercambios)