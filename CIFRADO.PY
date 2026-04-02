def cifrar_caracter(c, desplazamiento):
    if not c.isalpha():
        return c
    
    if c.islower():
        pos = ord(c) - ord('a')
        nueva_pos = (pos + desplazamiento) % 26
        return chr(nueva_pos + ord('a'))
    else:
        pos = ord(c) - ord('A')
        nueva_pos = (pos + desplazamiento) % 26
        return chr(nueva_pos + ord('A'))

def cifrar_mensaje(mensaje, desplazamiento):
    resultado = ""
    for caracter in mensaje:
        resultado += cifrar_caracter(caracter, desplazamiento)
    return resultado

def descifrar_mensaje(mensaje, desplazamiento):
    return cifrar_mensaje(mensaje, -desplazamiento)

# Pruebas
print("=== PRUEBAS ===")
print(cifrar_mensaje("hola", 3))        # krod
print(cifrar_mensaje("HOLA", 3))        # KROD
print(cifrar_mensaje("zapato", 1))      # abqbup
print(cifrar_mensaje("hola mundo", 5))  # mtqf rzsit

print("\n=== DESCIFRADO ===")
print(descifrar_mensaje("krod", 3))     # hola

# Programa con input
print("\n" + "=" * 40)
opcion = input("¿Quieres cifrar (C) o descifrar (D)? ").upper()

if opcion == 'C':
    msg = input("Mensaje a cifrar: ")
    d = int(input("Desplazamiento (1-25): "))
    print(f"Cifrado: {cifrar_mensaje(msg, d)}")
elif opcion == 'D':
    msg = input("Mensaje a descifrar: ")
    d = int(input("Desplazamiento (1-25): "))
    print(f"Descifrado: {descifrar_mensaje(msg, d)}")