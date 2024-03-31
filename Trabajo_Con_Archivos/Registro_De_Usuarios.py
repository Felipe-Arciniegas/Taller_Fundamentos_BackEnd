#Registro de Usuario : Escribe un programa que permita al usuario ingresar su nombre y edad, y guarda estos datos en un archivo.
print("\t Registro de Usuario.")
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
with open("usuarios.txt", "a") as archivo:
    archivo.write(f"{nombre},{edad}\n")
print("Datos guardados en usuarios.txt.")