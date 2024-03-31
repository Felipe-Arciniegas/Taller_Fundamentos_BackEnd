#Calculadora de Factorial : Crea un programa que calcula el factorial de un número ingresado por el usuario. Utilice tanto un ciclo for como un ciclo while para realizar el cálculo.
print("\t Calculadora de Factorial.")
while True:
    try:
        numero = int(input("Ingrese un número: "))
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es {factorial}.")
        factorial = 1
        i = 1
        while i <= numero:
            factorial *= i
            i += 1
        print(f"El factorial de {numero} es {factorial}.")
        break
    except ValueError:
        print("Error: Ingrese un número entero válido.")
