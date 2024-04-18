# Importo libreria para crear DataFrames.
import random
import pandas as pd

# Creo una lista de edades a partir de un generador de números random.
y = random.sample(range(0, 61), 30)

# Con 'if y' evaluo si la lista está vacía, y con 'if all(isinstance (x, (int)) for x in y)' evalúo si la lista tiene todos sus valores numéricos.
# con 'isintance' evalúo si el valor que obtengo en x de la lista 'y' es un entero.
if y and all(isinstance (x, (int)) for x in y):

# Defino una función.
  def analisis_estadistico(y):
  
# Creo un objeto DataFrame con la lista 'y' se creará una columna 'fi' con los valores que estoy pasando desde la lista 'y'.
    x = pd.DataFrame({"fi": y})

# Implemento el cálculo del cual depende cada columna.
    x["Fi"] = x["fi"].cumsum()
    x["ri"] = x["fi"] / x["fi"].sum()
    x["Ri"] = x["ri"].cumsum()
    x["pi%"] = x["ri"] * 100
    x["Pi%"] = x["pi%"].cumsum()

# Copio en el portapapeles la tabla final.
    x.to_clipboard(
    decimal=','
  )

# Muestro por consola la tabla.
    print(x.head(n=30))

    return x

# Ejecuto la función pasandole como parámetro la lista 'y'.
  analisis_estadistico(y)

# En caso de un error en la lista, se muestra por consola este mensaje
else:
  print("Error en la lista.")
