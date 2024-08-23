"""
Ejercicio 65: Tipos de datos pandas

* Utilizando la biblioteca Pandas, crea un DataFrame llamado df_empleados que contenga dos columnas: nombre y edad.
* La columna nombre debe contener los nombres de tres empleados: 'Ana', 'Luis' y 'Carlos'
* La columna edad debe contener las edades correspondientes: 30, 25 y 40
* Finalmente, muestra el DataFrame df_empleados utilizando la función print().
"""

import pandas as pd

empleados = {"nombre" : ["Ana", "Luis", "Carlos"], "edad" : [30, 25, 40]}

df_empleados = pd.DataFrame(empleados)

print(df_empleados)