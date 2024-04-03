# Defino el nombre de la función y le paso 2 parámetros
def missing_number(n, lista):
# Utilizo el bucle for para iterar sobre los elementos de la lista desde el 1 al 5
    for valor_lista in range(1, n + 1):
# Evalúo si el valor que está iterando exite o no en la lista
        if valor_lista not in lista:
# Devuelvo el valor faltante de la lista
            return valor_lista

# Verifico si la función me da los resultados que quiero dependiendo del valor que le estoy pasando a través de su parámetro
assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
# Almaceno en la variable 'valor_faltante' el valor que me dió la ejecución de la función
valor_faltante = missing_number(5, [1, 2, 4, 5])

# Muestro por consola el valor faltante
print(f"El valor faltante es: {valor_faltante}")
print("Se han pasado las pruebas")