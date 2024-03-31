#Eliminación de Duplicados : Escribe un programa que tome una lista de números ingresados ​​por el usuario y elimine todos los números duplicados.
print("\t Eliminación de Duplicados.")
numeros = []
while True:
    try:
        numero = input("Ingrese un número (o 'fin' para terminar): ")
        if numero == "fin":
            break
        numeros.append(int(numero))
    except ValueError:
        print("Error: Ingrese un número entero válido.")
numeros = list(set(numeros))
print("Lista sin Duplicados:")
for numero in numeros:
    print(numero)