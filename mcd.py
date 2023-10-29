def calcular_mcd(a, b):
    while b:
        print(f"{a} = {b} * {a // b} + {a % b}")
        a, b = b, a % b
    return a

numero1 = 35
numero2 = 19

print(f"Calculando el MCD de {numero1} y {numero2}:")
mcd = calcular_mcd(numero1, numero2)
print(f"El MCD de {numero1} y {numero2} es {mcd}.")