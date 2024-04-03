#sumar todos los valores y restar por no se que yyy suma desde uno hasta cinco, restamos ambas sumas entre elloas y se obtiene el valor faltante.
#condición que pregunte si el número mayor al anterior es mayor por 1 o mas valores y asi se obtiene el valor faltante
# def missing_number(n, 1):
  # return ((2 * (n + 1)) // 2) - sum(1)
  
# assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
  #2*(n+1)/2   eso da la sumatoria de 1 a n

def missing_number(n, lista):
      
      valor_faltante = ((n * (n + 1)) // 2) - sum(lista)
      print(f"El valor faltante es: {valor_faltante}")
      return valor_faltante
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"

# def missing_number(x, lista):

#   for valor_en_la_lista in range(len(lista) ):
#     if lista[valor_en_la_lista] >=  lista[valor_en_la_lista + 1]: 
#       print(f"valor no faltante: {lista[valor_en_la_lista]}")
#     else :
#       print(f"El valor faltante en la lista es {lista[valor_en_la_lista]}")


# assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
# def missing_number(x, lista):
  
#   for k in range(len(lista) - 1):
#     if k >= lista[k + 1]:
#       print(f"valor no faltante: {lista[k]}")
#     else:
#       print(f"valor faltante: {lista[k]}")

# assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
