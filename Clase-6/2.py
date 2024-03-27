#sumar todos los valores y restar por no se que yyy suma desde uno hasta cinco, restamos ambas sumas entre elloas y se obtiene el valor faltante.
#condición que pregunte si el número mayor al anterior es mayor por 1 o mas valores y asi se obtiene el valor faltante
def missing_number(n, 1):
  return ((2 * (n + 1)) // 2) - sum(1)
  
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
  #2*(n+1)/2   eso da la sumatoria de 1 a n