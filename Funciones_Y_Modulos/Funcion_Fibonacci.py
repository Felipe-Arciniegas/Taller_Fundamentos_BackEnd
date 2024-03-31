#Función recursiva de Fibonacci : Implementa una función recursiva que calcula el n-ésimo número de Fibonacci.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
if __name__ == "__main__":
    print("\t Función Recursiva de Fibonacci.")
    while True:
        try:
            n = int(input("Ingrese un número entero: "))
            if n < 0:
                print("Error: Ingrese un número entero positivo.")
            else:
                print(f"El {n}-ésimo número de Fibonacci es {fibonacci(n)}.")
                break
        except ValueError:
            print("Error: Ingrese un número entero válido.")