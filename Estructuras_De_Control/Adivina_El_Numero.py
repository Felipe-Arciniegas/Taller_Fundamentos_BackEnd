#Adivina el Número : Escribe un programa que genere un número aleatorio y pida al usuario que lo adivine. Si el usuario no acierta, indica si su número es demasiado alto o demasiado bajo.
import random
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