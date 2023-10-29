import math

print ("Si sabemos que las placas de los vehículos de Guatemala están formadas por 3 dígitos seguidos por 3 letras ¿Cuántas placas pueden emitirse en el país?  ")
digitos = 10
letras = 27
placas = pow(digitos, 3) * pow(letras, 3)

print("Si sabemos que hay 10 digitos del 0 al 9 y 27 letras de la A a la Z entonces:  ")

print( f"{digitos} * {digitos} * {digitos} * {letras} * {letras} * {letras} = {placas} " )

print(f"R//En en pais se pueden emitir {placas} placas")