import matplotlib.pyplot as plt

def collatz(n):
    """Calcula la secuencia de Collatz para un número dado y devuelve el número de iteraciones."""
    iterations = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        iterations += 1
    return iterations

def main():
    n_values = []  # Almacenará el número n de inicio de la secuencia
    iterations_values = []  # Almacenará el número de iteraciones

    for n in range(1, 10001):
        iterations = collatz(n)
        n_values.append(n)
        iterations_values.append(iterations)

    # Crear el gráfico
    plt.scatter(n_values, iterations_values, s=5, c='blue', alpha=0.5)
    plt.title('Conjetura de Collatz')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Número inicial (n)')
    plt.show()

if __name__ == "__main__":
    main()