"""
Ejercicio 66: Tipos de datos Pandas

* La columna nombre debe contener los nombres de tres empleados: 'Ana', 'Luis' y 'Carlos'
* La columna edad debe contener las edades correspondientes: 30, 25 y 40
* Utiliza el método adecuado para seleccionar solo la columna edad y almacénala en una variable llamada edades.
* Luego, muestra el contenido de edades utilizando la función print().
* Asegúrate de demostrar que el tipo de dato de edades es una Serie de Pandas. Utilizando la función type().
"""

import pandas as pd

empleados = {"nombre" : ["Ana", "Luis", "Carlos"], "edad" : [30, 25, 40]}

df_empleados = pd.DataFrame(empleados)

shape_df = df_empleados.shape
columns_df = df_empleados.columns
index_df = df_empleados.index

print(shape_df)
print(columns_df)
print(index_df)