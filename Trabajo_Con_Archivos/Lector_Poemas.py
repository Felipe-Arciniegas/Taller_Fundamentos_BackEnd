#Lector de Poemas : Crea un programa que lea un archivo de texto con un poema y lo muestre en la consola.
print("\t Lector de Poemas.")
archivo = input("Ingrese el nombre del archivo con el poema: ")
with open(archivo, "r") as poema:
    for linea in poema:
        print(linea, end="")
print("\n Poema leído.")
print("¡Hasta luego!")