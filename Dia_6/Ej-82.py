"""
Ejercicio 82: Agregacion de Series

* Crea una serie de Pandas a partir de la siguiente lista de edades = [23, 30, 26, 27, 22, 24, 25, 28]. 
* Luego, utiliza la función adecuada para calcular el promedio de estas edades. 
* Almacena el promedio en una variable llamada: promedio_edades
"""

import pandas as pd

# Lista de edades
edades = [23, 30, 26, 27, 22, 24, 25, 28]

promedio_edades = pd.Series(edades).mean()