# Cifrado 
# ------------------------------------

def cifrar_caracter(caracter, desplazamiento):
    if not caracter.isalpha():
        return caracter
    
    if caracter.islower():
        posicion = ord(caracter) - ord('a')
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(nueva_posicion + ord('a'))
    else:
        posicion = ord(caracter) - ord('A')
        nueva_posicion = (posicion + desplazamiento) % 26
        return chr(nueva_posicion + ord('A'))

def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for letra in mensaje:
        resultado = resultado + cifrar_caracter(letra, desplazamiento)
    return resultado

def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)

# ------------------------------------
print("Bienvenido al Cifrado Cesar")
print()

while True:
    print("--- Menu ---")
    print("1. Cifrar un mensaje")
    print("2. Descifrar un mensaje")
    print("3. Ver ejemplos")
    print("4. Salir")
    print()
    
    opcion = input("Elige una opcion (1,2,3,4): ")
    print()
    
    if opcion == "1":
        print("--- Cifrar mensaje ---")
        mensaje = input("Mensaje a cifrar: ")
        desplazamiento = int(input("Desplazamiento (1 a 25): "))
        resultado = cifrar_mensaje(mensaje, desplazamiento)
        print()
        print("Mensaje cifrado:", resultado)
        print()
        
    elif opcion == "2":
        print("--- Descifrar mensaje ---")
        mensaje = input("Mensaje a descifrar: ")
        desplazamiento = int(input("Desplazamiento usado (1 a 25): "))
        resultado = descifrar_mensaje(mensaje, desplazamiento)
        print()
        print("Mensaje original:", resultado)
        print()
        
    elif opcion == "3":
        print("--- Ejemplos ---")
        print("Cifrar 'hola' con desplazamiento 3:")
        print("  Resultado:", cifrar_mensaje("hola", 3))
        print()
        print("Cifrar 'HOLA' con desplazamiento 3:")
        print("  Resultado:", cifrar_mensaje("HOLA", 3))
        print()
        print("Cifrar 'zapato' con desplazamiento 1:")
        print("  Resultado:", cifrar_mensaje("zapato", 1))
        print()
        print("Descifrar 'krod' con desplazamiento 3:")
        print("  Resultado:", descifrar_mensaje("krod", 3))
        print()
        
    elif opcion == "4":
        print("Gracias por usar el Cifrado Cesar. Hasta luego!")
        break
        
    else:
        print("Opcion no valida. Elige 1,2,3 o 4.")
        print()
