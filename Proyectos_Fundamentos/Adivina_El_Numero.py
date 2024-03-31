# Juego de Adivina el Número Descripción : Implementa un juego donde el usuario intenta adivinar un número generado por la computadora, y otra variante donde la computadora intenta adivinar un número pensado por el usuario. Conceptos Clave : Estructuras de control, variables, entrada/salida.

import random
def Usuario_adivina():
    print("\t Adivina el Número.")
    numero = random.randint(1, 100)
    intentos = 0
    while True:
        intentos += 1
        guess = int(input("Adivina el número (1-100): "))
        if guess == numero:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break
        elif guess < numero:
            print("El número es demasiado bajo.")
        else:
            print("El número es demasiado alto.")

def Computadora_adivina():
        print("\t Adivina el Número (Variante: Computadora adivina)")
        numero_pensado = int(input("Piensa en un número (1-100): "))
        minimo = 1
        maximo = 100
        intentos = 0
        while True:
            intentos += 1
            guess = random.randint(minimo, maximo)
            print(f"¿Es {guess} tu número?")
            respuesta = input("Ingresa 's' si es demasiado bajo, 'a' si es demasiado alto, o 'c' si es correcto: ")
            if respuesta == 'c':
                print(f"¡La computadora adivinó tu número en {intentos} intentos!")
                break
            elif respuesta == 's':
                minimo = guess + 1
            elif respuesta == 'a':
                maximo = guess - 1
            else:
                print("Respuesta inválida. Ingresa 's', 'a' o 'c'.")
# Main
print("Selecciona el modo de juego:")
print("1. Adivina el número (Usuario)")
print("2. Adivina el número (Computadora)")

modo = input("Ingresa el número del modo de juego: ")

if modo == "1":
    Usuario_adivina()
elif modo == "2":
    Computadora_adivina()
else:
    print("Modo de juego no válido. Por favor, elige 1 o 2.")
print("¡Hasta luego!")

