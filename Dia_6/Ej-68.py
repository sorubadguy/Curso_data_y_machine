"""
Ejercicio 68: Data Frames

* Utiliza el DataFrame datos_clima creado en el ejercicio anterior. 
* Aplica el método  describe() para explorar la estructura del DataFrame y obtener un resumen estadístico de las columnas numéricas.
* Asegurate de almacenar el resultado en una variable llamada  describe_df
"""

import pandas as pd

datos_clima = pd.read_csv("clima.csv")

describe_df = datos_clima.describe()