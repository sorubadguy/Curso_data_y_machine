"""
Ejercicio 63: Funciones que llaman Funciones

* Desarrolla un programa que incluya las siguientes funciones:
! Función 1:
* solicitar_numero() que pide al usuario ingresar un número entero positivo y lo retorna. Puedes usar un mensaje de input del tipo: input("Ingrese un número entero positivo: ")
* Recuerda convertir la entrada de usuario a un tipo de dato entero. utiliza int()

! Función 2:
* calcular_factorial(n) que recibe el número entero n   (devuelto por solicitar_numero() y retorna su factorial.
* El factorial de un número entero positivo n se define como el producto de todos los números enteros positivos desde 1 hasta n.
* Por ejemplo, el factorial de 5 (simbolizado como 5) es 1 * 2 * 3 * 4 * 5 = 120.
* Pista para Calcular el Factorial de un Número
* El factorial de un número entero positivo n se obtiene multiplicando todos los números enteros desde 1 hasta n. Para lograr esto mediante programación, puedes seguir estos pasos utilizando un bucle for:
* Inicializa tu Variable Acumuladora: Antes de empezar a iterar, necesitas una variable que almacene el resultado de las multiplicaciones sucesivas. Esta variable debe empezar en 1, ya que el factorial de un número se define como el producto de números enteros, y comenzar con 1 asegura que el resultado final sea correcto. Por ejemplo, factorial = 1.
* Crea un Bucle for para Iterar: Necesitas iterar sobre una secuencia de números desde 1 hasta n (incluyendo n). La función range(1, n+1) genera esta secuencia, empezando en 1 y terminando en n.
* Multiplica y Acumula: Dentro del bucle, multiplica la variable acumuladora por el número actual de la iteración. Esto acumula el producto de todos los números hasta n. En cada iteración del bucle, actualizas la variable acumuladora con el nuevo producto, por ejemplo, factorial *= i, donde i es el número actual de la secuencia.
* Retorna el Resultado: Después de completar todas las iteraciones del bucle, tu variable acumuladora contendrá el factorial de n. Ahora puedes retornar este valor.
! Función 3:
* mostrar_resultado() que llama a solicitar_numeros(), luego utiliza el número ingresado para llamar a calcular_factorial(n) y finalmente imprime el resultado en el formato
* "El factorial de {n} es {resultado}".
* Asegúrate de que tu programa maneje adecuadamente la entrada de números y que calcular_factorial(n) sea capaz de computar el factorial sin usar importaciones de módulos externos.
* Este ejercicio te ayudará a practicar la estructura de funciones que llaman a otras funciones y la lógica de programación con operaciones matemáticas básicas.
"""

def solicitar_numero():
    return int(input("Ingrese un numero entero positivo"))
    
def calcular_factorial(n):
    factorial=1
    for i in range(1, n+1):
        factorial *= i
    return factorial
    
def mostrar_resultado():
    n = solicitar_numero()
    print(f"El factorial de {n} es {calcular_factorial(n)}")