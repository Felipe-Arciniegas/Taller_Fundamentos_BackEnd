#Analizador de Log : Desarrolla un script que lea un archivo de registro (log) y encuentre e informe sobre ciertos patrones de error.
print("\t Analizador de Log.")
archivo = input("Ingrese el nombre del archivo de log: ")
errores = 0
with open(archivo, "r") as log:
    for linea in log:
        if "error" in linea.lower():
            errores += 1
print(f"El archivo de log tiene {errores} errores.")
print("¡Hasta luego!")