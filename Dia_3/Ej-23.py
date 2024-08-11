"""
Ejercicio 23: Strings

* Escribe un programa en el que declares una variable llamada frase y le asignes el texto que prefieras.
* Utiliza el método correspondiente para contar el número de palabras contenidas en ella, asegurándote de que todas estén separadas por un único espacio.
* Finalmente, muestra el resultado en pantalla.
"""

frase = " Habia una ves un desarrollador de Python  "
print(frase.strip().count(" ") + 1)