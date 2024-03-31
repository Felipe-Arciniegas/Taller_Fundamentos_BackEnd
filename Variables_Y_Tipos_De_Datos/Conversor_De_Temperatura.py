# Conversor de Temperatura : Escribe un programa que convierta la temperatura de grados Celsius a Fahrenheit y viceversa. El usuario debe poder ingresar una temperatura y especificar a qué unidad desea convertirla.
print("\t Conversor de Temperatura: Celsius a Fahrenheit y viceversa.")
temperatura = float(input("Ingrese la temperatura: "))
unit = input("Ingrese la Unidad (C para Celsius, F para Fahrenheit): ")

if unit == "C":
    converted_temperatura = (temperatura * 9/5) + 32
    print(f"{temperatura} grados Celsius son iguales a {converted_temperatura} grados Fahrenheit.")
elif unit == "F":
    converted_temperatura = (temperatura - 32) * 5/9
    print(f"{temperatura} grados Fahrenheit son iguales a {converted_temperatura} grados Celsius.")
else:
    print("Caracter Invalido. Porfavor ingrese  C para Celsius o F para Fahrenheit.")