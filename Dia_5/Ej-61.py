"""
Ejercicio 61: Funciones que llaman Funciones

* Crea una función llamada solicitar_nombre() que pida al usuario su nombre utilizando input() y retorne este nombre.

* Luego, crea otra función llamada saludar() que llame a solicitar_nombre()  e imprima el siguiente saludo (reemplazando [nombre] por el nombre elegido por el usuario):
* ¡Hola [nombre]!
* Asegurate de usar cadena literales del tipo f"¡Hola {nombre}!"  para imprimir el mensaje.
"""

def solicitar_nombre():
    return input("Ingrese su nombre: ")
    
def saludar():
    nombre = solicitar_nombre()
    print(f"¡Hola {nombre}!")

saludar()