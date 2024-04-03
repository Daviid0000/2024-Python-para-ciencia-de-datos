
from tkinter import W


def Weird_Algorithm(n):
  ans = []

  ans.append(n)

  while n != 1:
    

  # while n != 1:
  #   if n % 2 == 0:
  #     n = n // 2
  #   else:
  #     n = (n * 3) + 1
  #   print(f"valor de ans: {n}")
  #   ans.append(n)
  # return ans

  
 
assert Weird_Algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en la secuencia"
assert Weird_Algorithm(5) == [5, 16, 8, 4, 2, 1], "Error en la secuencia"
assert Weird_Algorithm(4) == [4, 2, 1], "Error en la secuencia"

print("Ha pasado todas las prubeas")
# // devuelve la división entera