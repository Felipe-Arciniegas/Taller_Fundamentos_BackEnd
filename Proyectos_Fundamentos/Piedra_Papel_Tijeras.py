# Juego de Piedra, Papel o Tijeras Descripción: Desarrolla una versión del clásico juego de Piedra, Papel o Tijeras, donde el usuario juega contra la computadora. El programa debe pedir al usuario su elección, generar una elección para la computadora y determinar el ganador. Conceptos Clave: Estructuras de control, entrada/salida, lógica del juego.

import random
def Piedra_Papel_Tijeras():
    print("\t Piedra, Papel o Tijeras.")
    opciones = ["piedra", "papel", "tijeras"]
    while True:
        computadora = random.choice(opciones)
        usuario = input("Elige piedra, papel o tijeras (o 'fin' para terminar): ").lower()
        if usuario == "fin":
            break
        elif usuario not in opciones:
            print("Opción inválida. Por favor, elige piedra, papel o tijeras.")
        else:
            print(f"Computadora: {computadora}")
            if usuario == computadora:
                print("Empate.")
            elif usuario == "piedra" and computadora == "tijeras":
                print("¡Ganaste!")
            elif usuario == "papel" and computadora == "piedra":
                print("¡Ganaste!")
            elif usuario == "tijeras" and computadora == "papel":
                print("¡Ganaste!")
            else:
                print("¡Perdiste!")
# Main
Piedra_Papel_Tijeras()
print("¡Hasta luego!")