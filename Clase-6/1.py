
def sequence(n):
  ans = []

  ans.append(n)

  while n != 1:
    if n % 2 == 0:
      n = n // 2
    else:
      n *= 3 + 1

  return ans

assert sequence(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en la secuencia"
assert sequence(5) == [5, 16, 8, 4, 2, 1], "Error en la secuencia"
assert sequence(4) == [4, 2, 1], "Error en la secuencia"

# // devuelve la división entera