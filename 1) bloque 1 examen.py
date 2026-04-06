# Cajero automatico
# -------------
def calcular_billetes():
    print()
    print("Ingresar un monto que sea multiplo de 20")
    monto = int(input("Monto: "))
    
    if monto % 20 != 0:
        print("Error: El monto debe ser multiplo de 20")
        return None
    
    billete200 = monto // 200
    resto = monto % 200
    
    billete100 = resto // 100
    resto = resto % 100
    
    billete50 = resto // 50
    resto = resto % 50
    
    billete20 = resto // 20
    
    partes = []
    if billete200 > 0:
        partes.append(f"{billete200}x Q200")
    if billete100 > 0:
        partes.append(f"{billete100}x Q100")
    if billete50 > 0:
        partes.append(f"{billete50}x Q50")
    if billete20 > 0:
        partes.append(f"{billete20}x Q20")
    
    print()
    print("Billetes necesarios:")
    print(", ".join(partes))
    print()
    return (billete200, billete100, billete50, billete20)

# -------
print("Bienvenido al cajero automatico")
print()

while True:
    print("--- Menu ---")
    print("1. Calcular billetes")
    print("2. Salir")
    print()
    
    opcion = input("Elige una opcion (1 o 2): ")
    
    if opcion == "1":
        calcular_billetes()
    elif opcion == "2":
        print()
        print("Gracias por usar el cajero. Hasta luego!")
        break
    else:
        print()
        print("Opcion no valida. Elige 1 o 2.")
        print()
