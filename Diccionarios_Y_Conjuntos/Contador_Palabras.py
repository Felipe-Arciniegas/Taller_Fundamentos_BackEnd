#Contador de Palabras : Dada una cadena de texto, cuenta cuántas veces aparece cada palabra y presenta los resultados en un diccionario.
print("\t Contador de Palabras.")
texto = input("Ingrese un texto: ")
palabras = texto.split()
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1
print("Contador de Palabras:")
for palabra, cantidad in contador.items():
    print(f"{palabra}: {cantidad}")