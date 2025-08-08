insercion = eval(input("Ingrese lista: "))
i = 1
comparaciones = 0
intercambios = 0

while i < len(insercion):
    clave = insercion[i]
    j = i - 1
    while j >= 0 and insercion[j] > clave:
        comparaciones += 1
        insercion[j + 1] = insercion[j]
        intercambios += 1
        j = j - 1
    if j >= 0:
        comparaciones += 1
    insercion[j + 1] = clave
    intercambios += 1
    i = i + 1

print("Lista ordenada:", insercion)
print("Comparaciones:", comparaciones)
print("Intercambios:", intercambios)
