# Conversor de temp
# -------------------------------

def celsius_a_fahrenheit(c):
    return c * 9/5 + 32

def celsius_a_kelvin(c):
    return c + 273.15

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def kelvin_a_celsius(k):
    return k - 273.15

def fahrenheit_a_kelvin(f):
    celsius = fahrenheit_a_celsius(f)
    return celsius_a_kelvin(celsius)

def kelvin_a_fahrenheit(k):
    celsius = kelvin_a_celsius(k)
    return celsius_a_fahrenheit(celsius)

def convertir(valor, origen, destino):
    origen = origen.upper()
    destino = destino.upper()
    
    if origen == destino:
        return valor
    
    if origen == 'C':
        if destino == 'F':
            return celsius_a_fahrenheit(valor)
        elif destino == 'K':
            return celsius_a_kelvin(valor)
    
    if origen == 'F':
        if destino == 'C':
            return fahrenheit_a_celsius(valor)
        elif destino == 'K':
            return fahrenheit_a_kelvin(valor)
    
    if origen == 'K':
        if destino == 'C':
            return kelvin_a_celsius(valor)
        elif destino == 'F':
            return kelvin_a_fahrenheit(valor)
    
    print("Error: combinacion", origen, "->", destino, "no valida")
    return None

# ------------------------------------------------------------
print("Bienvenido al conversor de temperaturas")
print()

while True:
    print("           CONVERSOR DE TEMPERATURAS")
    print()
    print("Opciones de conversion:")
    print("  1. Celsius -> Fahrenheit")
    print("  2. Celsius -> Kelvin")
    print("  3. Fahrenheit -> Celsius")
    print("  4. Fahrenheit -> Kelvin")
    print("  5. Kelvin -> Celsius")
    print("  6. Kelvin -> Fahrenheit")
    print("  0. Salir")
    print()
    
    try:
        opcion = int(input("Elige una opcion (0-6): "))
    except:
        print()
        print("Debes ingresar un numero entero")
        print()
        continue
    
    if opcion == 0:
        print()
        print("Gracias por usar el conversor. Hasta luego!")
        break
    
    if opcion < 1 or opcion > 6:
        print()
        print("Opcion no valida. Elige un numero entre 0 y 6.")
        print()
        continue
    
    try:
        temperatura = float(input("Ingresa la temperatura: "))
    except:
        print()
        print("Debes ingresar un numero valido")
        print()
        continue
    
    # Asignar origen y destino segun opcion
    if opcion == 1:
        origen = 'C'
        destino = 'F'
    elif opcion == 2:
        origen = 'C'
        destino = 'K'
    elif opcion == 3:
        origen = 'F'
        destino = 'C'
    elif opcion == 4:
        origen = 'F'
        destino = 'K'
    elif opcion == 5:
        origen = 'K'
        destino = 'C'
    elif opcion == 6:
        origen = 'K'
        destino = 'F'
    
    resultado = convertir(temperatura, origen, destino)
    
    if resultado is not None:
        resultado_redondeado = round(resultado, 2)
        print()
        print("RESULTADO:")
        print("  " + str(temperatura) + " " + origen + " = " + str(resultado_redondeado) + " " + destino)
        print()
    else:
        print()
        print("No se pudo realizar la conversion")
        print()    
