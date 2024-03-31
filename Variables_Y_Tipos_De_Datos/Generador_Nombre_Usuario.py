# Generador de Nombre de Usuario : Solicita al usuario su nombre, apellido y año de nacimiento, y genera un nombre de usuario combinándolos (por ejemplo, "AnaSmith1990")..
print("\t Generador de Nombre de Usuario.")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
anio_nacimiento = input("Ingrese su año de nacimiento: ")
username = nombre + apellido + anio_nacimiento
print(f"Su nombre de usuario es: {username}")
