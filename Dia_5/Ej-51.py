"""
Ejercicio-51: Loop FOR

* Escribe un programa que use bucles anidados para imprimir todas las combinaciones posibles de colores y prendas de vestir. Define dos listas: una que contenga:
* colores = ['rojo', 'azul', 'verde']
* y otra que contenga prendas de vestir:
* prendas = ['camisa', 'pantalones', 'sombrero']
* Dentro de los bucles anidados, imprime cada combinación de prenda   y color.
"""

colores = ['rojo', 'azul', 'verde']
prendas = ['camisa', 'pantalones', 'sombrero']

for i in colores:
    for j in prendas:
        print(f"{j} {i}")