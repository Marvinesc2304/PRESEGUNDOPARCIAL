# ========== FUNCIONES AUXILIARES ==========

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


# ========== FUNCIÓN PRINCIPAL 1 ==========

def validar_password(password):
    if tiene_largo_valido(password) and tiene_mayuscula(password) and tiene_digito(password) and tiene_especial(password):
        return True
    else:
        return False


# ========== FUNCIÓN PRINCIPAL 2 ==========

def diagnosticar_password(password):
    print("\n" + "=" * 40)
    print(f"Analizando contraseña: '{password}'")
    print("=" * 40)
    
    if not tiene_largo_valido(password):
        print("❌ Debe tener al menos 8 caracteres")
    
    if not tiene_mayuscula(password):
        print("❌ Debe tener al menos una letra mayúscula")
    
    if not tiene_digito(password):
        print("❌ Debe tener al menos un dígito (0-9)")
    
    if not tiene_especial(password):
        print("❌ Debe tener al menos un carácter especial (! @ # $ %)")
    
    if validar_password(password):
        print("\n✅ ¡CONTRASEÑA VÁLIDA! ✅")
        return True
    else:
        print("\n❌ Contraseña NO válida. Intenta de nuevo.")
        return False


# ========== PROGRAMA PRINCIPAL ==========

print("=" * 50)
print("   VALIDADOR DE CONTRASEÑAS")
print("=" * 50)
print("\nREGLAS:")
print("1. Mínimo 8 caracteres")
print("2. Al menos una letra MAYÚSCULA")
print("3. Al menos un número (dígito)")
print("4. Al menos un carácter especial (! @ # $ %)")
print("=" * 50)

# Variable para controlar si la contraseña es válida
contrasena_valida = False

# Bucle: seguir pidiendo hasta que sea válida
while contrasena_valida == False:
    # Pedir al usuario que ingrese una contraseña
    password_usuario = input("\n👉 Ingresa tu contraseña: ")
    
    # Diagnosticar y guardar si es válida
    contrasena_valida = diagnosticar_password(password_usuario)

# Cuando sale del while, la contraseña es válida
print("\n" + "=" * 50)
print("🎉 ¡FELICIDADES! Contraseña aceptada. 🎉")
print("=" * 50)