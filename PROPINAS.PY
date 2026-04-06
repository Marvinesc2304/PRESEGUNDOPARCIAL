
# Calculadora de propinas 
# ------------------------------------------------------------

def calcular_propina(subtotal, porcentaje):
    propina = subtotal * porcentaje / 100
    return propina

def calcular_total(subtotal, propina):
    total = subtotal + propina
    return total

def dividir_cuenta(total, personas):
    if personas <= 0:
        return "Error: El numero de personas debe ser mayor que cero"
    else:
        cada_uno = total / personas
        return cada_uno

def aplicar_descuento(subtotal, descuento_pct):
    nuevo_subtotal = subtotal * (100 - descuento_pct) / 100
    return nuevo_subtotal

# ------------------------------------------------------------
print("Bienvenido a la calculadora de propinas")
print()

while True:
    print("--- Menú ---")
    print("1. Calcular propina")
    print("2. Dividir la cuenta entre personas")
    print("3. Aplicar descuento y luego propina")
    print("4. Salir")
    print()

    opcion = input("Elige una opcion (1,2,3,4): ")

    if opcion == "1":
        print()
        print("--- Calcular propina ---")
        subtotal = float(input("Cuanto es el subtotal de la cuenta? Q"))
        porcentaje = float(input("Que porcentage de propina quieres dar? (ejemplo: 15) "))
        print()
        
        propina = calcular_propina(subtotal, porcentaje)
        total = calcular_total(subtotal, propina)
        
        print("Propina: Q", propina)
        print("Total a pagar: Q", total)
        print()

    elif opcion == "2":
        print()
        print("--- Dividir la cuenta ---")
        total = float(input("Cual es el total de la cuenta? Q"))
        personas = int(input("Cuantas personas van a pagar? "))
        print()
        
        resultado = dividir_cuenta(total, personas)
        print("Cada persona paga: Q", resultado)
        print()

    elif opcion == "3":
        print()
        print("--- Aplicar descuento y luego propina ---")
        subtotal = float(input("Subtotal original: Q"))
        descuento = float(input("Porcentaje de descuento: "))
        print()
        
        subtotal_con_descuento = aplicar_descuento(subtotal, descuento)
        print("Subtotal con descuento: Q", subtotal_con_descuento)
        print()
        
        porcentaje_propina = float(input("Porcentaje de propina (sobre el subtotal con descuento): "))
        propina = calcular_propina(subtotal_con_descuento, porcentaje_propina)
        total_final = calcular_total(subtotal_con_descuento, propina)
        
        print("Propina: Q", propina)
        print("Total final a pagar: Q", total_final)
        print()

    elif opcion == "4":
        print()
        print("Gracias por usar la calculadora! Hasta luego.")
        break

    else:
        print("Opcion no valida. Elige 1,2,3 o 4.")
        print()
