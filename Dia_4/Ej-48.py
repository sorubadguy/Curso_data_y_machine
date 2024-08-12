"""
Ejercicio 48: If-Elif-Else

* Declara tres variables x1, x2, x3, que contengan tres números enteros distintos. El programa debe imprimir los números en orden ascendente.

? El propósito de este ejercicio es fortalecer tu comprensión y habilidad para aplicar estructuras condicionales en Python, diseñando una solución que te permita practicar cómo controlar el flujo de un programa basado en condiciones específicas.

? Es importante mencionar que, aunque existen métodos más eficientes y directos para ordenar números en Python —tales como las funciones sorted() o el uso de listas—, el enfoque de este ejercicio es que desarrolles y apliques la lógica detrás de las estructuras condicionales. Este enfoque te ayudará a mejorar tu pensamiento lógico y tu capacidad para resolver problemas de programación de una manera más fundamental.
"""

x1, x2, x3 = 5, 6, 7

if x1 < x2 < x3:
    print(x1, x2, x3)
elif x1 < x3 < x2:
    print(x1, x3, x2)
elif x2 < x1 < x3:
    print(x2, x1, x3)
elif x2 < x3 < x1:
    print(x2, x3, x1)
elif x3 < x1 < x2:
    print(x3, x1, x2)
elif x3 < x2 < x1:
    print(x3, x2, x1)