print("Calcular la unión de dos conjuntos.")
print("Conjunto A: {Todos los elementos del sistema de numeración hexadecimal}")
print("Conjunto B: {Todos los números x tal que 7 < x < 12}")

ConjuntoA = set((0,1,2,3,4,5,6,7,8,9,"a",'b',"c","d","e","f"))
ConjuntoB = set((8,9,10,11))

print(f"\nConjunto A = {ConjuntoA}")
print(f"Conjunto B = {ConjuntoB}")

union = ConjuntoA.union(ConjuntoB)
print(f"\nLa unión de los conjuntos A y B es: {union}")
