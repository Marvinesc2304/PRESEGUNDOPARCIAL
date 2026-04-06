# Validador de contras
# ----------------------------
def tiene_largo_valido(password):
    if len(password) >= 8:
        return True
    else:
        return False

def tiene_mayuscula(password):
    for caracter in password:
        if caracter.isupper():
            return True
    return False

def tiene_digito(password):
    for caracter in password:
        if caracter.isdigit():
            return True
    return False

def tiene_especial(password):
    especiales = "!@#$%"
    for caracter in password:
        if caracter in especiales:
            return True
    return False

def validar_password(password):
    if tiene_largo_valido(password) and tiene_mayuscula(password) and tiene_digito(password) and tiene_especial(password):
        return True
    else:
        return False

def diagnosticar_password(password):
    print()
    print("Analizando contraseña:", password)
    
    if not tiene_largo_valido(password):
        print("Debe tener al menos 8 caracteres")
    
    if not tiene_mayuscula(password):
        print("Debe tener al menos una letra mayuscula")
    
    if not tiene_digito(password):
        print("Debe tener al menos un digito (0-9)")
    
    if not tiene_especial(password):
        print("Debe tener al menos un caracter especial (! @ # $ %)")
    
    if validar_password(password):
        print()
        print("CONTRASEÑA VALIDA!")
        return True
    else:
        print()
        print("Contraseña NO valida. Intenta de nuevo.")
        return False

# -------------------
print("           VALIDADOR DE CONTRASEÑAS")
print()
print("REGLAS:")
print("1. Minimo 8 caracteres")
print("2. Al menos una letra MAYUSCULA")
print("3. Al menos un numero (digito)")
print("4. Al menos un caracter especial (! @ # $ %)")

contrasena_valida = False

while contrasena_valida == False:
    print()
    password_usuario = input("Ingresa tu contraseña: ")
    contrasena_valida = diagnosticar_password(password_usuario)

print()
print("FELICIDADES! Contraseña aceptada.")
