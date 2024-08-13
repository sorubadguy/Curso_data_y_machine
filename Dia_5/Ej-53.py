"""
Ejercicio 53: Range

* Escribe un programa que use la función range() para sumar todos los números del 1 al 100.
* Para ello sigue los siguientes pasos:
* Inicializa la variable suma = 0.
* Usa un bucle for para iterar sobre cada número del 1 al 100, incluyendo el 100.
* Imprime el resultado de la suma empleando el siguiente mensaje:
* 'La suma de todos los números del 1 al 100 es: {suma}'
"""

suma = 0

for i in range(1, 101):
    suma += i
    
print(f"La suma de todos los números del 1 al 100 es: {suma}")