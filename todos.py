while True:
  
    print("Menú de Selección:")
    print("1. Ejercicio Permutación")
    print("2. Ejercicio conjuntos")
    print("3. Ejercicio MCD")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")
  
    if opcion == "1":
        print ("Si sabemos que las placas de los vehículos de Guatemala están formadas por 3 dígitos seguidos por 3 letras ¿Cuántas placas pueden emitirse en el país?  \n")
        digitos = 10
        letras = 27
        placas = digitos*digitos*digitos*letras*letras*letras 

        print("Si sabemos que hay 10 digitos del 0 al 9 y 27 letras de la A a la Z entonces:  \n")

        print( f"{digitos} * {digitos} * {digitos} * {letras} * {letras} * {letras} = {placas} \n" )

        print(f"R//En en pais se pueden emitir {placas} placas")
     
    elif opcion == "2":
        print("Cual es el conjunto resultante de la Unión de los conjuntos conformados por A={x/x elementos del sistema de numeración hexadecimal} y B {x/x 12 > x < 7}")
        ConjuntoA = set((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f'))
        ConjuntoB = set((8, 9, 10, 11))
        print(f"A = {ConjuntoA}")
        print(f"B = {ConjuntoB}")
        print(f"A U B = {ConjuntoA.union(ConjuntoB)}")
    
    elif opcion == "3":
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

    elif opcion == "4":
        print("Saliendo del programa... ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
    
    continuar = input("¿Desea realizar otra operación? (s/n): ")
    if continuar.lower() != "s":
        print("Saliendo del programa... ¡Hasta luego!")
        break