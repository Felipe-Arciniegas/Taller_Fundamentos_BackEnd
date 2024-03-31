#Contador de Vocales : Desarrolla un programa que cuente la cantidad de vocales en una frase proporcionada por el usuario.
print("\t Contador de Vocales.")
frase = input("Ingrese una frase: ")
vocales = "aeiou"
contador = 0
for letra in frase:
    if letra.lower() in vocales:
        contador += 1
print(f"La frase tiene {contador} vocales.")