lista_numeros = [1, 2, 2, 2, 3, 4, 5, 5, 6, 6, 6]

numeros_sin_repetir = set(lista_numeros)

print(numeros_sin_repetir)

#def clean_list(n):
#   a = set(n)
#   return list(a)


for i, x in enumerate(numeros_sin_repetir):
  for j in lista_numeros:
    k = x == j
    if x == j:
      print(k)
# comparar lista de números sin repetir con lista con números repetidos
# x valor en cada indice
# j valor de cada indice en la lista de números con valores repetidos


#al commit