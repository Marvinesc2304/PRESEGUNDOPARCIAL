# Tablas 
# -------------------------------------------

def tabla(n):
    print()
    print("TABLA DEL", n)
    print("------------------")
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
    print("------------------")

def es_primo(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True

def tablas_primos(limite):
    print()
    print("=== TABLAS DE PRIMOS hasta", limite, "===")
    print()
    for numero in range(2, limite + 1):
        if es_primo(numero):
            tabla(numero)

# ------------------------------------------------------------
print("Bienvenido al generador de tablas de multiplicar")
print()

while True:
    print("--- Menu ---")
    print("1. Ver tablas de numeros primos (hasta un limite)")
    print("2. Ver tabla de un numero especifico")
    print("3. Verificar si un numero es primo")
    print("4. Salir")
    print()

    opcion = input("Elige una opcion (1,2,3,4): ")
    print()

    if opcion == "1":
        try:
            limite = int(input("Ingresa el limite (desde 2 hasta...): "))
            if limite >= 2:
                tablas_primos(limite)
            else:
                print("El limite debe ser mayor o igual a 2")
            print()
        except:
            print("Debes ingresar un numero entero")
            print()

    elif opcion == "2":
        try:
            num = int(input("Ingresa el numero para ver su tabla: "))
            tabla(num)
            print()
        except:
            print("Debes ingresar un numero entero")
            print()

    elif opcion == "3":
        try:
            num = int(input("Ingresa el numero para saber si es primo: "))
            if es_primo(num):
                print(num, "SI es un numero primo")
            else:
                print(num, "NO es primo")
            print()
        except:
            print("Debes ingresar un numero entero")
            print()

    elif opcion == "4":
        print("Gracias por usar el programa. Hasta luego!")
        break

    else:
        print("Opcion no valida. Elige 1,2,3 o 4.")
        print()
