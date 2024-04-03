# Defino el nombre de la función pasandole un valor como parametro a través de 'n'
def Weird_Algorithm(n):
# Inicializo una variable que almacena un arreglo 
  lista = []
# El arreglo 'ans' es rellenado con los valores de 'n'
  lista.append(n)
# Utilizo la estructura de control While para repetir la misma secuenccia hasta llegar al valor deseado
  while n != 1:
# Defino una condición, si 'n' es divisible por 2 su recidiuo debe ser igual a 0
    if n % 2 == 0:
# Almaceno en 'n' la división de 'n' entre 2    
      n = n // 2
# Defino otra condición en caso de que 'n' no sea divisible por 2      
    else:
# Almaceno en 'n' n multiplicado por 3 sumando 1 al resultado
      n = (n * 3) + 1
# Almaceno cada valor de 'n' en el arreglo 'ans'
    lista.append(n)
# Devuelve los valores que contiene 'ans'
  return lista
# Ejecuto la función pasandole el valor 3, cada valor que obtenga con la función se irá almacenando en la variable 'resultado'
resultado = Weird_Algorithm(3)
# Muestro por consola los valores que ha obtenido la variable 'resultado'
print(f"valores de ans: {resultado}")

# Verifico si la función me da los resultados que quiero dependiendo del valor que le estoy pasando a través de su parámetro
assert Weird_Algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en la secuencia"
assert Weird_Algorithm(5) == [5, 16, 8, 4, 2, 1], "Error en la secuencia"
assert Weird_Algorithm(4) == [4, 2, 1], "Error en la secuencia"
print("Ha pasado todas las prubeas")