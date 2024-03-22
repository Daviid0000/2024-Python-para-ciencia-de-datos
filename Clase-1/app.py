def factorial_sin_operador(numero):
    resultado = 1
    for i in range(2, numero + 1):
        resultado = multiplicacion_sin_operador(resultado, i)
    return resultado

def multiplicacion_sin_operador(numero, factor):
    resultado = 0
    for _ in range(factor):
        resultado += numero
    return resultado

numero = int(input("Ingrese el número para calcular su factorial: "))
resultado = factorial_sin_operador(numero)
print("El factorial de", numero, "es:", resultado)
