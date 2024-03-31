#Inversión de Tupla : Escribe un programa que invierte los elementos de una tupla.
print("\t Inversión de Tupla.")
tupla = tuple(input("Ingrese los elementos de la tupla separados por comas: ").split(","))
inverted_tupla = tuple(reversed(tupla))
print(f"Tupla Original: {tupla}")
print(f"Tupla Invertida: {inverted_tupla}")