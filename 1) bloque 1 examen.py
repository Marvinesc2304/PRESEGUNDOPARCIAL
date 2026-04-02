def calcular_billetes(monto):
    print("ingresar un monto con multiplos de 20")
    monto = int(input("Monto: "))
    if monto % 20 != 0:
        print("Error: El monto debe ser múltiplo de 20")
        return None
    
    b200 = monto // 200
    resto = monto % 200
    
    b100 = resto // 100
    resto = resto % 100
    
    b50 = resto // 50
    resto = resto % 50
    
    b20 = resto // 20
    
    partes = []
    if b200 > 0:
        partes.append(f"{b200}x Q200")
    if b100 > 0:
        partes.append(f"{b100}x Q100")
    if b50 > 0:
        partes.append(f"{b50}x Q50")
    if b20 > 0:
        partes.append(f"{b20}x Q20")
    
    print(", ".join(partes))
    return (b200, b100, b50, b20)


# LLAMAMOS A LA FUNCIÓN (esto es lo que hace que se ejecute)
calcular_billetes(370)   # Probar con 370