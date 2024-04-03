# def palindrome_reorder(n):
#     if 1 <= n <= 10^6
def palindrome_reorder(a):
    # Ordenar los caracteres en la cadena
    caracteres_ordenados = sorted(a)

    # Contar cuántas veces aparece cada caracter
    contador = {}
    for char in caracteres_ordenados:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1

    # Construir la parte izquierda del palíndromo
    izquierda = ''
    for char, count in contador.items():
        izquierda += char * (count // 2)

    # Construir la parte derecha del palíndromo invirtiendo la parte izquierda
    derecha = izquierda[::-1]

    # Si hay un solo caracter central, agregarlo al medio del palíndromo
    caracter_central = '' if len(a) % 2 == 0 else next(iter(contador))

    # Combinar las partes izquierda, central y derecha para formar el palíndromo final
    palindromo = izquierda + caracter_central + derecha

    return palindromo

# Prueba del código
assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"

# def palindrome_reorder(a):
#    for x in range(0, 10, 2):
#       if a[x] == a[x]:
#          valores_ordenados = []
#          valores_ordenados.append(a[x])
#          print(f"El valor es: {a[valores_ordenados]}")
      

# assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"