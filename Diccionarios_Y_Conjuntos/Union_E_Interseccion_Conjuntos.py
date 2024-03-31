#Unión e Intersección de Conjuntos : Dados dos conjuntos, encuentra su unión e intersección.
print("\t Unión e Intersección de Conjuntos.")
set1 = set(input("Ingrese los elementos del primer conjunto separados por comas: ").split(","))
set2 = set(input("Ingrese los elementos del segundo conjunto separados por comas: ").split(","))
union = set1.union(set2)
interseccion = set1.intersection(set2)
print(f"Unión de Conjuntos: {union}")
print(f"Intersección de Conjuntos: {interseccion}")