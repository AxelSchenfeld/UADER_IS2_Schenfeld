#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2:
    print("Debe ingresar dos numeros")
    sys.exit(1)

numeros = sys.argv[1].split('-')
n1 = int(numeros[0])
n2 = int(numeros[1])

if n1 < 1:
    print("El límite inferior debe ser mayor o igual a 1.")
    sys.exit()

elif n2 > 60:
    print("El límite superior no puede ser mayor que 60.")
    sys.exit() 

if n1 >= n2:
    print("El primer digito debe ser menor que el segundo")
    sys.exit(1)

for num in range(n1, n2 + 1):
    print("Factorial de", num, "! es", factorial(num))