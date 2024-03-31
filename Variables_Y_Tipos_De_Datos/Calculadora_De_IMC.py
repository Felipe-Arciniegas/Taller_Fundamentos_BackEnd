# Calculadora de IMC : Crea un programa que calcula el Índice de Masa Corporal (IMC) a partir del peso (en kilogramos) y la altura (en metros) ingresados ​​por el usuario. El IMC se calcula dividiendo el peso del individuo por el cuadrado de su altura, y se clasifica de la siguiente manera:
# IMC Clasificación
# Menos de 18.5 Bajo peso
# 18.5–24.9 Normal
# 25.0–29.9 Sobrepeso
# 30.0 o más Obeso
print("\t Calculadora de IMC: Indice de Masa Corporal.")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"Su IMC es {imc} y usted tiene bajo peso.")
elif imc >= 18.5 and imc < 25:
    print(f"Su IMC es {imc} y usted tiene un peso normal.")
elif imc >= 25 and imc < 30:
    print(f"Su IMC es {imc} y usted tiene sobrepeso.")
else:
    print(f"Su IMC es {imc} y usted es obeso.")
