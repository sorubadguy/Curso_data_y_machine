"""
Ejercicio 73: Operaciones basicas Series

* Crea dos series de pandas utilizando listas de Python.
* Puedes crear ambas series con los números enteros de tu elección solamente asegurate de que la serie 1 y la serie 2 las almacenes en variables nombradas: serie1 y serie2 respectivamente.
* Luego, suma ambas series y asigna el resultado a una variable llamada serie_sumada. Imprime el resultado de serie_sumada.
"""

import pandas as pd

serie1 = pd.Series([1,2,3,4,5])
serie2 = pd.Series([6,7,8,9,0])

serie_sumada = serie1 + serie2

print(serie_sumada)