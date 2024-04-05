# Defino el nombre de la función y le paso dos parámetros
def number_spiral(x,y):
# Creo la variable 'matriz_spiral' que almacena un array de arrays.
    matriz_spiral = [
        [1, 2, 9, 10, 25],
        [4, 3, 8, 11, 24],
        [5, 6, 7, 12, 23],
        [16, 15, 14, 13, 22],
        [17, 18, 19, 20, 21]]
# Almaceno el valor que se encuentra en dichas coordenadas restando 1 a cada parámetro para hacer que los indices empicen en 1 el lugar de 0.
    valor_en_coordenadas = (matriz_spiral[x -1][y -1])
# Muestro por consola el valor que se quiere obtener en dichas coordenadas
    print(f"En las cordenadas ({x};{y}) el valor es es: {valor_en_coordenadas}")
# Devuelvo a la función el valor de 'valor_en_coordenadas'
    return valor_en_coordenadas

# Verifico si la función me da los resultados que quiero dependiendo del valor que le estoy pasando a través de su parámetro
assert number_spiral(4, 1) == 3, "Error en el caso de prueba"
print("Ha pasado todas las prubeas")