# Generador de Contraseñas Descripción: Crea un programa que genere contraseñas seguras basándose en criterios especificados por el usuario (longitud, inclusión de caracteres especiales, etc.). Conceptos Clave: Listas, generación de números aleatorios, estructuras de control.

import random
import string

print("\t Generador de Contraseñas.")
longitud = int(input("Longitud de la Contraseña: "))
especiales = input("¿Incluir caracteres especiales? (s/n): ")
if especiales == "s":
    caracteres = string.ascii_letters + string.digits + string.punctuation
else:
    caracteres = string.ascii_letters + string.digits
contraseña = "".join(random.choice(caracteres) for i in range(longitud))
print(f"Contraseña Generada: {contraseña}")