"""
Ejercicio 79: Series en Pandas

* Crea una serie de Pandas llamada:  serie_numeros   que contenga los números del 1 al 20.
* Luego, escribe un código que filtre y muestre solo aquellos números que sean mayores que 10.
* Utiliza una variable llamada filtro para almacenar la serie  filtrada.
"""

import pandas as pd

serie_numeros = pd.Series(range(1, 21))
filtro = serie_numeros > 10
print(filtro)