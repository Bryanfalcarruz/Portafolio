busqueda_lineal = (eval(input("ingrese numero a buscar: ")))
coleccion_lineal = (eval(input("ingrese lista: ")))
encontrado = False
i = 0
contador = 0
while i < len(coleccion_lineal) and not encontrado:
  if coleccion_lineal[i] == busqueda_lineal:
    encontrado = True
  i = i + 1
  contador += 1
print(encontrado)
print("la busqueda realizo", contador, "comparaciones")