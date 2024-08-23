"""
Ejercicio 78: Limpieza de datos

* Tu tabla de ventas, la columna "Precio" tiene algunos valores nulos.

? data = {
?     'ID': [1, 2, 3, 4],
?     'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
?     'Cantidad': [10, 20, 30, 40],
?     'Precio': [100, None, 300, None]
? }

* Escribe un código en Python usando Pandas para reemplazar los valores nulos en la columna Precio por el promedio de los precios no nulos de esa columna.
"""

import pandas as pd

data = {
    'ID': [1, 2, 3, 4],
    'Producto': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
    'Cantidad': [10, 20, 30, 40],
    'Precio': [100, None, 300, None]
}

df = pd.DataFrame(data)
valor_nuevo = {"Precio" : df['Precio'].mean()}

df.fillna(valor_nuevo)