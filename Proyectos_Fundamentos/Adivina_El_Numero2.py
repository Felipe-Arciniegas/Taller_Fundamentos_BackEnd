import random

def juego_usuario_adivina():
    print("Bienvenido al juego de Adivina el Número!")
    numero_secreto = random.randint(1, 100)
    intentos = 0
    
    while True:
        intento = int(input("Introduce tu número: "))
        intentos += 1
        
        if intento < numero_secreto:
            print("El número es más alto. Intenta de nuevo.")
        elif intento > numero_secreto:
            print("El número es más bajo. Intenta de nuevo.")
        else:
            print(f"Felicidades! Adivinaste el número en {intentos} intentos.")
            break

def juego_computadora_adivina():
    print("Piensa en un número del 1 al 100 y yo intentaré adivinarlo.")
    input("Presiona Enter cuando estés listo...")
    
    limite_inferior = 1
    limite_superior = 100
    intentos = 0
    
    while True:
        intento = random.randint(limite_inferior, limite_superior)
        print(f"¿Es {intento} tu número?")
        respuesta = input("Indica si es 'sí', 'más bajo' o 'más alto': ").lower()
        intentos += 1
        
        if respuesta == "sí":
            print(f"¡Genial! Adiviné tu número en {intentos} intentos.")
            break
        elif respuesta == "más bajo":
            limite_superior = intento - 1
        elif respuesta == "más alto":
            limite_inferior = intento + 1
        else:
            print("Por favor, responde 'sí', 'más bajo' o 'más alto'.")

# Main
print("Selecciona el modo de juego:")
print("1. Adivina el número (Usuario)")
print("2. Adivina el número (Computadora)")

modo = input("Ingresa el número del modo de juego: ")

if modo == "1":
    juego_usuario_adivina()
elif modo == "2":
    juego_computadora_adivina()
else:
    print("Modo de juego no válido. Por favor, elige 1 o 2.")
