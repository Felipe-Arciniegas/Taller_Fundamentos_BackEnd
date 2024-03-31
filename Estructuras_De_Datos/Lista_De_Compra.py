#Lista de la Compra : Crea un programa que permite al usuario ingresar una lista de compras, elemento por elemento, y luego imprime la lista completa al final.
print("\t Lista de la Compra.")
lista_compra = []
while True:
    item = input("Ingrese un elemento de la lista de compra (o 'fin' para terminar): ")
    if item.lower() == "fin":
        break
    lista_compra.append(item)
print("Lista de Compra:")
for item in lista_compra:
    print(item)