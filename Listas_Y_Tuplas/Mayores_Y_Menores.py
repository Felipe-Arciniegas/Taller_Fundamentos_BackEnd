#Mayores y Menores : Dada una lista de números, encuentra el número más grande y el más pequeño en la lista.
print("\t Mayores y Menores.")
numeros = []
while True:
    try:
        numero = input("Ingrese un número (o 'fin' para terminar): ")
        if numero == "fin":
            break
        numeros.append(int(numero))
    except ValueError:
        print("Error: Ingrese un número entero válido.")
if numeros:
    print(f"El número más grande es {max(numeros)}.")
    print(f"El número más pequeño es {min(numeros)}.")
else:
    print("No se ingresaron números.")