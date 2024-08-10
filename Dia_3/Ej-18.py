"""
Ejercicio 18: String

* Crea un programa que tome la frase "Python es divertido" y realice las siguientes operaciones en orden, utilizando métodos de string correspondientes: 
* 1. Remplaza la palabra "divertido" por la palabra "genial". Deberás investigar cuál método de string sirve para reemplazar una palabra por otra. Puedes hacerlo con el método dir(), pero ten en cuenta que no podrás usarlo en esta plataforma, sino en tus cuadernos Jupyter.
* 2. Almacena el resultado en una variable llamada frase_modificada
* 3. Imprime el resultado en pantalla.
"""

frase = "Python es divertido"
frase1 = frase.split()
frase1[2] = "genial"
frase = ""
for p in frase1:
    frase = f"{frase} {p}"
print(frase.lstrip())