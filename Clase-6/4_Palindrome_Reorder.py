# Defino el nombre de la función y le paso un parámetro.
def palindrome_reorder(palabra):
# Almaceno en la variable 'lista_caracteres' cada caracter de la cadena de carácteres encontrada en el parámetro 'palabra'.
    lista_caracteres=list(palabra)
# Almaceno una copia de la lista de carácteres en la variable 'copia_caracteres'.
    copia_caracteres=list(lista_caracteres)
# Invierto la lista de carácteres y la convierto en cadena de carácteres.
    copia_caracteres.reverse()
    cadena = ''.join(lista_caracteres)
# Evalúo si la lista invertida 'copia_caracteres' es igual a la lista normal 'lista_caracteres'.
    if copia_caracteres == lista_caracteres:
# Si ambas listas son iguales informo por consola que la palabra es un Polindromo.
        print(f'{cadena} - Es un Palíndromo ')
    else:
# Si las listas no son iguales informo por consola que la palabra no es Polindromo.
        print(f'{palabra} - No es un Palíndromo')
# Devuelvo a la función el valor de 'cadena'
    return cadena

# Verifico si la función me da los resultados que quiero dependiendo del valor que le estoy pasando a través de su parámetro.
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
print("Ha pasado todas las prubeas")
