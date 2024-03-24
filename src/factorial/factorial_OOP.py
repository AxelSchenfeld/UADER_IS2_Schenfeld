import sys

class Factorial:
    def __init__(self):
        pass
    
    def factorial(self, num):
        if num < 0:
            print("Factorial de un número negativo no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact
    
    def run(self, min_num, max_num):
        if min_num < 0 or max_num < 0:
            print("Los números deben ser no negativos.")
            return
        
        for num in range(min_num, max_num + 1):
            print("Factorial de", num, "! es", self.factorial(num))

if len(sys.argv) < 2:
    print("Debe ingresar dos números.")
    sys.exit(1)

numeros = sys.argv[1].split('-')
n1 = int(numeros[0])
n2 = int(numeros[1])

if n1 >= n2:
    print("El primer número debe ser menor que el segundo.")
    sys.exit(1)

factorial_calculator = Factorial()
factorial_calculator.run(n1, n2)