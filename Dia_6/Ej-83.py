"""
Ejercicio 83: Agregacion de Series

* Dada lista con los siguientes valores de ventas diarias de una tienda en una semana:
* ventas = [120, 150, 90, 200, 210, 130, 160], realiza las siguientes tareas:
* Crea una serie de Pandas con los días de la semana como índice  (asumiendo que el primer valor corresponde al Lunes).
* Calcula y muestra la suma total de las ventas de la semana. Almacena este valor en una variable llamada: suma_total_ventas
* Encuentra y muestra el día de mayores ventas. Almacena este valor en una variable llamada: dia_mayores_ventas
* Calcula y muestra el promedio de ventas de la semana. Almacena este valor en una variable llamada: promedio_ventas
"""
import pandas as pd

ventas = [120, 150, 90, 200, 210, 130, 160]

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

ventas_x_dia = pd.Series(ventas, dias)

suma_total_ventas = ventas_x_dia.sum()

dia_mayores_ventas = ventas_x_dia.max()

promedio_ventas = ventas_x_dia.mean()