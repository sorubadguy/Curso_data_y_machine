"""
Ejercicio 75: Operaciones basicas series

* Considera una serie de pandas llamada serie_grande que contiene los números del 1 al 10 o mayor al 10. Obten su item 9 y haya su raiz cuadrada.
* Imprime el resultado.
"""

import pandas as pd

serie_grande = pd.Series(range(1,30))

item_9 = serie_grande[8]

print(item_9 ** 0.5)