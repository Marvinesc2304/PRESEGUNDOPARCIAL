# ========== FUNCIONES DE CÁLCULO ==========

def calcular_propina(subtotal, porcentaje):
    """Calcula el monto de la propina"""
    return subtotal * porcentaje / 100

def calcular_total(subtotal, propina):
    """Calcula el total a pagar (subtotal + propina)"""
    return subtotal + propina

def dividir_cuenta(total, personas):
    """Divide el total entre el número de personas"""
    if personas <= 0:
        return "❌ Error: El número de personas debe ser mayor a 0"
    return total / personas

def aplicar_descuento(subtotal, descuento_pct):
    """Aplica un descuento porcentual al subtotal"""
    if descuento_pct < 0 or descuento_pct > 100:
        return subtotal  # Si el descuento no es válido, no aplica nada
    return subtotal * (100 - descuento_pct) / 100


# ========== FUNCIONES DE MENÚ ==========

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "=" * 45)
    print("        🍽️  CALCULADORA DE PROPINAS  🍽️")
    print("=" * 45)
    print("  1. 💰 Calcular propina")
    print("  2. 👥 Dividir la cuenta entre personas")
    print("  3. 🎯 Aplicar descuento + propina")
    print("  4. 🚪 Salir")
    print("=" * 45)


def obtener_numero(mensaje):
    """Pide un número al usuario y valida que sea válido"""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("❌ Error: Debes ingresar un número válido")


def obtener_entero(mensaje):
    """Pide un número entero al usuario y valida"""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("❌ Error: Debes ingresar un número entero")


# ========== FUNCIONES DE CADA OPCIÓN ==========

def opcion_propina():
    """Opción 1: Calcular propina y total"""
    print("\n" + "-" * 40)
    print("   💰 CALCULAR PROPINA")
    print("-" * 40)
    
    subtotal = obtener_numero("  Subtotal de la cuenta: Q")
    
    print("\n  Porcentajes sugeridos:")
    print("    10% - Servicio regular")
    print("    15% - Buen servicio")
    print("    20% - Excelente servicio")
    
    porcentaje = obtener_numero("  Porcentaje de propina (%): ")
    
    propina = calcular_propina(subtotal, porcentaje)
    total = calcular_total(subtotal, propina)
    
    print("\n" + "-" * 40)
    print("📊 RESULTADO:")
    print(f"  Subtotal:    Q{subtotal:.2f}")
    print(f"  Propina ({porcentaje}%): Q{propina:.2f}")
    print(f"  Total a pagar: Q{total:.2f}")
    print("-" * 40)


def opcion_dividir():
    """Opción 2: Dividir la cuenta entre personas"""
    print("\n" + "-" * 40)
    print("   👥 DIVIDIR LA CUENTA")
    print("-" * 40)
    
    total = obtener_numero("  Total de la cuenta: Q")
    personas = obtener_entero("  Número de personas: ")
    
    resultado = dividir_cuenta(total, personas)
    
    print("\n" + "-" * 40)
    if isinstance(resultado, str):
        print(f"  {resultado}")
    else:
        print(f"  Total: Q{total:.2f}")
        print(f"  Personas: {personas}")
        print(f"  Cada uno paga: Q{resultado:.2f}")
    print("-" * 40)


def opcion_descuento():
    """Opción 3: Aplicar descuento + propina"""
    print("\n" + "-" * 40)
    print("   🎯 APLICAR DESCUENTO + PROPINA")
    print("-" * 40)
    
    subtotal = obtener_numero("  Subtotal de la cuenta: Q")
    descuento = obtener_numero("  Porcentaje de descuento (%): ")
    
    # Aplicar descuento
    subtotal_con_descuento = aplicar_descuento(subtotal, descuento)
    
    print(f"\n  Subtotal original: Q{subtotal:.2f}")
    print(f"  Descuento aplicado: {descuento}%")
    print(f"  Subtotal con descuento: Q{subtotal_con_descuento:.2f}")
    
    # Pedir propina (ahora sobre el subtotal con descuento)
    porcentaje_propina = obtener_numero("\n  Porcentaje de propina (%): ")
    
    propina = calcular_propina(subtotal_con_descuento, porcentaje_propina)
    total = calcular_total(subtotal_con_descuento, propina)
    
    print("\n" + "-" * 40)
    print("📊 RESULTADO FINAL:")
    print(f"  Subtotal con descuento: Q{subtotal_con_descuento:.2f}")
    print(f"  Propina ({porcentaje_propina}%): Q{propina:.2f}")
    print(f"  TOTAL FINAL: Q{total:.2f}")
    print("-" * 40)


# ========== FUNCIÓN PRINCIPAL ==========

def main():
    """Función principal que controla el flujo del programa"""
    print("\n" + "🍽️" * 20)
    print("   BIENVENIDO AL RESTAURANTE")
    print("🍽️" * 20)
    
    while True:
        mostrar_menu()
        opcion = input("\n👉 Elige una opción (1-4): ")
        
        if opcion == "1":
            opcion_propina()
        elif opcion == "2":
            opcion_dividir()
        elif opcion == "3":
            opcion_descuento()
        elif opcion == "4":
            print("\n👋 ¡Gracias por usar la calculadora! Buen provecho.")
            break
        else:
            print("❌ Opción no válida. Elige 1, 2, 3 o 4.")
        
        input("\n▶️  Presiona ENTER para continuar...")


# ========== EJECUTAR PROGRAMA ==========
if __name__ == "__main__":
    main()