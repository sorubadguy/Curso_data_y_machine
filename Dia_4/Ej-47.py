"""
Ejercicio 47: If-Elif-Else

* Escribe un programa donde declares una variable llamada calificacion inicializala con un número del 0 al 10. El programa debe imprimir:

* "Calificación no válida" para calificaciones mayores a 10.
* "Sobresaliente" para calificaciones de 9 o 10.
* "Notable" para calificaciones entre 7 y 8.
* "Aprobado" para calificaciones de 5 a 6.
* "Insuficiente" para calificaciones menores a 5.
"""

calificacion = 5

if calificacion > 10:
    print("Calificación no válida")
elif calificacion >= 9:
    print("Sobresaliente")
elif calificacion >= 7:
    print("Notable")
elif calificacion >= 5:
    print("Aprobado")
else:
    print("Insuficiente")