#  calificaciones 
# ----------------------------------

def promedio(notas):
    suma = 0
    cantidad = 0
    for nota in notas:
        suma = suma + nota
        cantidad = cantidad + 1
    return suma / cantidad

def mayor(notas):
    mayor_nota = notas[0]
    for i in range(1, len(notas)):
        if notas[i] > mayor_nota:
            mayor_nota = notas[i]
    return mayor_nota

def menor(notas):
    menor_nota = notas[0]
    for i in range(1, len(notas)):
        if notas[i] < menor_nota:
            menor_nota = notas[i]
    return menor_nota

def contar_aprobados(notas, minimo=61):
    aprobados = 0
    for nota in notas:
        if nota >= minimo:
            aprobados = aprobados + 1
    return aprobados

def reporte(notas):
    print()
    print("===================================")
    print("           REPORTE DE CALIFICACIONES")
    print("======================================")
    print()
    print("Lista de notas:", notas)
    print("------------------------------")
    
    prom = promedio(notas)
    max_nota = mayor(notas)
    min_nota = menor(notas)
    aprobados = contar_aprobados(notas)
    reprobados = len(notas) - aprobados
    
    print("ESTADISTICAS:")
    print("  Promedio general:", round(prom, 2))
    print("  Nota mas alta:", max_nota)
    print("  Nota mas baja:", min_nota)
    print("  Estudiantes aprobados (>=61):", aprobados)
    print("  Estudiantes reprobados:", reprobados)
    print("-----------------------------")
    
    print()
    print("NOTAS APROBADAS:")
    for nota in notas:
        if nota >= 61:
            print("  *", nota)
    
    print()
    print("NOTAS REPROBADAS:")
    for nota in notas:
        if nota < 61:
            print("  *", nota)
    
    print()
    print("==========================")
    print()

# -------------------------------------------
print("Bienvenido al sistema de analisis de calificaciones")
print()

while True:
    print("--- Menu ---")
    print("1. Usar notas de ejemplo")
    print("2. Ingresar mis propias notas")
    print("3. Salir")
    print()
    
    opcion = input("Elige una opcion (1,2,3): ")
    print()
    
    if opcion == "1":
        notas_ejemplo = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]
        reporte(notas_ejemplo)
        
        print("--- Pruebas individuales de las funciones ---")
        print("promedio(notas) =", round(promedio(notas_ejemplo), 2))
        print("mayor(notas) =", mayor(notas_ejemplo))
        print("menor(notas) =", menor(notas_ejemplo))
        print("contar_aprobados(notas) =", contar_aprobados(notas_ejemplo))
        print("contar_aprobados(notas, 70) =", contar_aprobados(notas_ejemplo, 70))
        print()
        
    elif opcion == "2":
        print("--- Ingreso de notas ---")
        print("Escribe una nota por linea. Presiona ENTER solo para terminar.")
        print()
        
        notas_usuario = []
        contador = 1
        
        while True:
            entrada = input("Nota " + str(contador) + ": ")
            if entrada == "":
                if len(notas_usuario) == 0:
                    print("Debes ingresar al menos una nota.")
                    print()
                    continue
                else:
                    break
            
            try:
                nota = float(entrada)
                if 0 <= nota <= 100:
                    notas_usuario.append(nota)
                    contador = contador + 1
                else:
                    print("La nota debe estar entre 0 y 100")
            except:
                print("Debes ingresar un numero valido")
        
        print()
        print("Notas ingresadas:", notas_usuario)
        reporte(notas_usuario)
        
    elif opcion == "3":
        print("Gracias por usar el sistema. Hasta luego!")
        break
        
    else:
        print("Opcion no valida. Elige 1, 2 o 3.")
        print()
