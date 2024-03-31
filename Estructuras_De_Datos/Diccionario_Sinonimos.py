#Diccionario de Sinónimos : Implementa un pequeño diccionario de sinónimos, donde el usuario puede ingresar una palabra y obtener sinónimos de esa palabra.
print("\t Diccionario de Sinónimos.")
sinonimos = {
    "feliz": ["contento", "alegre", "gozoso"],
    "triste": ["deprimido", "melancólico", "apenado"],
    "enojado": ["furioso", "iracundo", "molesto"],
    "asustado": ["atemorizado", "espantado", "aterrado"],
    "cansado": ["fatigado", "agotado", "extenuado"]
}
while True:
    palabra = input("Ingrese una palabra (o 'fin' para terminar): ")
    if palabra.lower() == "fin":
        break
    if palabra in sinonimos:
        print(f"Sinónimos de {palabra}:")
        for sinonimo in sinonimos[palabra]:
            print(sinonimo)
    else:
        print("Palabra no encontrada en el diccionario de sinónimos.")