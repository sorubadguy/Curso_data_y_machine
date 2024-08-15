"""
Ejercicio 62: Funciones que llaman Funciones

* Escribe dos funciones:
* pedir_numeros() debe solicitar al usuario que ingrese dos números (uno a la vez) y retornar estos números como enteros.
* La segunda función, sumar(), debe llamar a pedir_numeros(), sumar los dos números obtenidos e imprimir el resultado de la suma.
* Asegúrate de que sumar() imprima el resultado en formato de texto, por ejemplo:
* "La suma es 10" para una suma de 5 y 5.
* Para ello puedes usar una cadena literal del tipo f"La suma es {resultado}"  para imprimir el mensaje.
"""

def pedir_numeros():
    num1 = int(input("ingrese un numero"))
    num2 = int(input("ingrese otro numero"))
    return num1, num2

def sumar():
    num1, num2 = pedir_numeros()
    print(f"La suma es {num1 + num2}")