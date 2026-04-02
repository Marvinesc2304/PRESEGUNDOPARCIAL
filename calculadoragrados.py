# ========== FUNCIONES BÁSICAS ==========

def celsius_a_fahrenheit(c):
    """Convierte Celsius a Fahrenheit"""
    return c * 9/5 + 32

def celsius_a_kelvin(c):
    """Convierte Celsius a Kelvin"""
    return c + 273.15

def fahrenheit_a_celsius(f):
    """Convierte Fahrenheit a Celsius"""
    return (f - 32) * 5/9

def kelvin_a_celsius(k):
    """Convierte Kelvin a Celsius"""
    return k - 273.15


# ========== FUNCIONES COMPUESTAS ==========

def fahrenheit_a_kelvin(f):
    """Convierte Fahrenheit a Kelvin (usando las funciones anteriores)"""
    celsius = fahrenheit_a_celsius(f)
    return celsius_a_kelvin(celsius)

def kelvin_a_fahrenheit(k):
    """Convierte Kelvin a Fahrenheit (usando las funciones anteriores)"""
    celsius = kelvin_a_celsius(k)
    return celsius_a_fahrenheit(celsius)


# ========== FUNCIÓN PRINCIPAL ==========

def convertir(valor, origen, destino):
    """
    Convierte una temperatura entre escalas.
    
    Parámetros:
    valor: número (la temperatura a convertir)
    origen: 'C', 'F' o 'K' (escala de origen)
    destino: 'C', 'F' o 'K' (escala de destino)
    
    Retorna: la temperatura convertida o None si es inválido
    """
    
    # Convertimos a mayúsculas para evitar errores
    origen = origen.upper()
    destino = destino.upper()
    
    # Misma escala
    if origen == destino:
        return valor
    
    # Desde Celsius (C)
    if origen == 'C':
        if destino == 'F':
            return celsius_a_fahrenheit(valor)
        elif destino == 'K':
            return celsius_a_kelvin(valor)
    
    # Desde Fahrenheit (F)
    if origen == 'F':
        if destino == 'C':
            return fahrenheit_a_celsius(valor)
        elif destino == 'K':
            return fahrenheit_a_kelvin(valor)
    
    # Desde Kelvin (K)
    if origen == 'K':
        if destino == 'C':
            return kelvin_a_celsius(valor)
        elif destino == 'F':
            return kelvin_a_fahrenheit(valor)
    
    # Si llegamos aquí, combinación no válida
    print(f"❌ Error: Combinación {origen} → {destino} no válida")
    return None


# ========== PROGRAMA PRINCIPAL CON MENÚ NUMÉRICO ==========

def mostrar_menu():
    print("\n" + "=" * 50)
    print("        CONVERSOR DE TEMPERATURAS")
    print("=" * 50)
    print("\n📋 OPCIONES DE CONVERSIÓN:")
    print("-" * 40)
    print("  1.  Celsius → Fahrenheit")
    print("  2.  Celsius → Kelvin")
    print("  3.  Fahrenheit → Celsius")
    print("  4.  Fahrenheit → Kelvin")
    print("  5.  Kelvin → Celsius")
    print("  6.  Kelvin → Fahrenheit")
    print("-" * 40)
    print("  0.  Salir del programa")
    print("=" * 50)


def obtener_opcion():
    """Pide al usuario que seleccione una opción del menú"""
    while True:
        try:
            opcion = int(input("\n👉 Elige una opción (0-6): "))
            if opcion >= 0 and opcion <= 6:
                return opcion
            else:
                print("❌ Opción no válida. Elige un número entre 0 y 6.")
        except ValueError:
            print("❌ Debes ingresar un número válido.")


def obtener_temperatura():
    """Pide al usuario que ingrese la temperatura"""
    while True:
        try:
            temperatura = float(input("\n🌡️  Ingresa la temperatura: "))
            return temperatura
        except ValueError:
            print("❌ Debes ingresar un número válido.")


def mostrar_resultado(valor, origen, destino, resultado):
    """Muestra el resultado de la conversión de forma bonita"""
    print("\n" + "=" * 50)
    print("📊 RESULTADO:")
    print("-" * 50)
    
    # Símbolos de grados según la escala
    simbolos = {'C': '°C', 'F': '°F', 'K': 'K'}
    
    resultado_redondeado = round(resultado, 2)
    print(f"   {valor} {simbolos[origen]}  =  {resultado_redondeado} {simbolos[destino]}")
    print("=" * 50)


# ========== PROGRAMA PRINCIPAL ==========

print("\n" + "🔥" * 25)
print("   BIENVENIDO AL CONVERSOR DE TEMPERATURAS")
print("🔥" * 25)

while True:
    mostrar_menu()
    opcion = obtener_opcion()
    
    # Opción 0: Salir
    if opcion == 0:
        print("\n👋 ¡Gracias por usar el conversor! Hasta luego.")
        break
    
    # Pedir la temperatura
    temperatura = obtener_temperatura()
    
    # Definir origen y destino según la opción
    if opcion == 1:  # Celsius → Fahrenheit
        origen = 'C'
        destino = 'F'
        resultado = convertir(temperatura, origen, destino)
        mostrar_resultado(temperatura, origen, destino, resultado)
    
    elif opcion == 2:  # Celsius → Kelvin
        origen = 'C'
        destino = 'K'
        resultado = convertir(temperatura, origen, destino)
        mostrar_resultado(temperatura, origen, destino, resultado)
    
    elif opcion == 3:  # Fahrenheit → Celsius
        origen = 'F'
        destino = 'C'
        resultado = convertir(temperatura, origen, destino)
        mostrar_resultado(temperatura, origen, destino, resultado)
    
    elif opcion == 4:  # Fahrenheit → Kelvin
        origen = 'F'
        destino = 'K'
        resultado = convertir(temperatura, origen, destino)
        mostrar_resultado(temperatura, origen, destino, resultado)
    
    elif opcion == 5:  # Kelvin → Celsius
        origen = 'K'
        destino = 'C'
        resultado = convertir(temperatura, origen, destino)
        mostrar_resultado(temperatura, origen, destino, resultado)
    
    elif opcion == 6:  # Kelvin → Fahrenheit
        origen = 'K'
        destino = 'F'
        resultado = convertir(temperatura, origen, destino)
        mostrar_resultado(temperatura, origen, destino, resultado)
    
    