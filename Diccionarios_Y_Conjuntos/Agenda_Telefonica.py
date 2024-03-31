#Agenda Telefónica : Crea un programa que permite al usuario añadir, eliminar y buscar números de teléfono en un diccionario.
print("\t Agenda Telefónica.")
agenda = {}
while True:
    print("\nMenú:")
    print("1. Añadir Número.")
    print("2. Eliminar Número.")
    print("3. Buscar Número.")
    print("4. Salir.")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        numero = input("Ingrese el número: ")
        agenda[nombre] = numero
        print(f"Se añadió el número de {nombre}.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre: ")
        if nombre in agenda:
            del agenda[nombre]
            print(f"Se eliminó el número de {nombre}.")
        else:
            print(f"No se encontró el número de {nombre}.")
    elif opcion == "3":
        nombre = input("Ingrese el nombre: ")
        if nombre in agenda:
            print(f"El número de {nombre} es {agenda[nombre]}.")
        else:
            print(f"No se encontró el número de {nombre}.")
    elif opcion == "4":
        break
    else:
        print("Error: Seleccione una opción válida.")
print("¡Hasta luego!")