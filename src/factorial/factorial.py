#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

# Definir una función para calcular el factorial de un número dado
def factorial(num):
    # Verificar si el número es negativo
    if num < 0:
        print("Factorial de un número negativo no existe")
    # Si el número es 0, el factorial es 1
    elif num == 0:
        return 1
    else:
        # Calcular el factorial utilizando un bucle while
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact

# Verificar si se proporcionan suficientes argumentos de línea de comandos
if len(sys.argv) < 2:
    # Si no se proporcionan suficientes argumentos, imprimir un mensaje y salir del programa
    print("Debe ingresar dos numeros")
    sys.exit(1)

# Separar los dos números proporcionados como un rango
numeros = sys.argv[1].split('-')
# Convertir los números a enteros
n1 = int(numeros[0])
n2 = int(numeros[1])

# Verificar si el límite inferior es mayor o igual a 1
if n1 < 1:
    print("El límite inferior debe ser mayor o igual a 1.")
    sys.exit()

# Verificar si el límite superior es menor o igual a 60
elif n2 > 60:
    print("El límite superior no puede ser mayor que 60.")
    sys.exit() 

# Verificar si el primer número es menor que el segundo número
if n1 >= n2:
    print("El primer digito debe ser menor que el segundo")
    sys.exit(1)

# Calcular y mostrar los factoriales de los números en el rango dado
for num in range(n1, n2 + 1):
    print("Factorial de", num, "! es", factorial(num))