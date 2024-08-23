"""
Ejercicio 69: Data Frames

* Utiliza el DataFrame datos_clima creado en el ejercicio anterior. Aplica los métodos correspondientes para:
? Extraer exactamente la primera fila de 'datos_clima'. Almacena el contenido en una variable llamada head_df
? Extraer exactamente la última fila de 'datos_clima'. Almacena el contenido en una variable llamada tail_df
"""

import pandas as pd

datos_clima = pd.read_csv("clima.csv")

head_df = datos_clima.head(1)
tail_df = datos_clima.tail(1)