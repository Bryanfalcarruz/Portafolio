busqueda_binaria = (eval(input("ingrese numero a buscar: ")))
coleccion = (eval(input("ingrese lista: ")))
inferior = 0
superior = len(coleccion)-1
contador = 0
j = (inferior + superior) // 2
while coleccion[j] != busqueda_binaria and inferior <= superior:
  if busqueda_binaria < coleccion[j]:
    superior = j - 1
    contador = contador + 1
  else:
    inferior = j + 1
    contador = contador + 1
  j = (inferior + superior) // 2
if coleccion[j] == busqueda_binaria:
  print(True)
else:
  print(False)
print("la busqueda realizo", contador, "comparaciones")