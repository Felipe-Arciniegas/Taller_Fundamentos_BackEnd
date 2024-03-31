import random
import string

def generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_caracteres_especiales):
    caracteres = string.ascii_lowercase
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_numeros:
        caracteres += string.digits
    if usar_caracteres_especiales:
        caracteres += string.punctuation
    
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    longitud = int(input("Longitud de la contraseña: "))
    usar_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    usar_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    usar_caracteres_especiales = input("¿Incluir caracteres especiales? (s/n): ").lower() == 's'
    
    contrasena = generar_contrasena(longitud, usar_mayusculas, usar_numeros, usar_caracteres_especiales)
    print("Tu contraseña generada es:", contrasena)

if __name__ == "__main__":
    main()
