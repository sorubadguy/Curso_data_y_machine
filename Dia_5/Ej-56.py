"""
Ejercicio 56: Loop WHILE

* Utilizando un bucle while, escribe un programa que cuente desde 0 hasta 15, pero que omita los números 5 y 10. 
* Usa la declaración continue para lograr este comportamiento, e imprime cada número en una línea nueva.
"""

i = 0
while i < 16:
    if (i != 5) and (i != 10):
        print(i)
    i += 1