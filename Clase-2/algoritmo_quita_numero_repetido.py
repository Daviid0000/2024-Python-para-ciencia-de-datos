lista_numeros = [1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6]

numeros_sin_repetir = set(lista_numeros)
print(f"lista con números repetidos: {lista_numeros}")
print(f"lista con números sin repetir: {numeros_sin_repetir}")

for x in numeros_sin_repetir:

    cantidad = 0
    
    for j in lista_numeros:
    
     if x == j:
    
      cantidad += 1
    
    print(f"La cantidad de veces que se repite el número {x} es de: {cantidad}")
