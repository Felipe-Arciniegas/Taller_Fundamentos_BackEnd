#Función de Conversión de Divisas : Escribe una función que convierte una cantidad de dinero de una moneda a otra utilizando tasas de cambio dadas.
def conversion_divisas(cantidad, tasa_cambio):
    return cantidad * tasa_cambio

if __name__ == "__main__":
    print("\t Conversor de Divisas.")
    cantidad = float(input("Ingrese la cantidad de dinero: "))
    tasa_cambio = float(input("Ingrese la tasa de cambio: "))
    print(f"La cantidad convertida es: {conversion_divisas(cantidad, tasa_cambio)}")