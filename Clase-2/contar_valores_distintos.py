def contar_valores_distintos(valores):
    valores_distintos = set()

    for val in valores:
        valores_distintos.add(val)
    
    return len(valores_distintos)

assert contar_valores_distintos([2, 3, 2, 2, 3]) == 2, "Caso de prueba fallido"

print("Todos los casos de prueba han pasado correctamente")