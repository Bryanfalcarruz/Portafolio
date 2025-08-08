def metodo_heron(S, candidato, tolerancia):
    x = S / candidato
    candidato = (candidato + x) / 2
    
    while abs(S - (candidato * candidato)) > tolerancia:
        x = S / candidato
        candidato = (candidato + x) / 2
    
    return candidato


# Bloque principal
S = float(input("Ingrese el número positivo S: "))
candidato = float(input("Ingrese el valor inicial del candidato: "))
tolerancia = float(input("Ingrese la tolerancia: "))

resultado = metodo_heron(S, candidato, tolerancia)
print(f"La raíz cuadrada aproximada de {S} es: {resultado}")