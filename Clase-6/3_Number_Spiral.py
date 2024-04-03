#assert number_spiral(2, 2) == 3, "Error en el caso de prueba"

def number_spiral(x,y):
    matriz_spiral = [[1, 2, 9, 10, 25],
                     [4, 3, 8, 11, 24],
                     [5, 6, 7, 12, 23],
                     [16, 15, 14, 13, 22],
                     [17, 18, 19, 20, 21]]
    
    valor_en_coordenadas = (matriz_spiral[x -1][y -1])
    print(f"El valor en las cordenadas {x};{y} es: {valor_en_coordenadas}")
    return valor_en_coordenadas
assert number_spiral(2, 2) == 3, "Error en el caso de prueba"