# ========== FUNCIONES PRINCIPALES ==========

def promedio(notas):
    """Calcula el promedio de una lista de notas"""
    suma = 0
    cantidad = 0
    
    for nota in notas:
        suma = suma + nota
        cantidad = cantidad + 1
    
    return suma / cantidad


def mayor(notas):
    """Encuentra la nota más alta (sin usar max())"""
    # Asumimos que la primera nota es la mayor
    mayor_nota = notas[0]
    
    # Recorremos desde la segunda nota (índice 1)
    for i in range(1, len(notas)):
        if notas[i] > mayor_nota:
            mayor_nota = notas[i]
    
    return mayor_nota


def menor(notas):
    """Encuentra la nota más baja (sin usar min())"""
    # Asumimos que la primera nota es la menor
    menor_nota = notas[0]
    
    # Recorremos desde la segunda nota
    for i in range(1, len(notas)):
        if notas[i] < menor_nota:
            menor_nota = notas[i]
    
    return menor_nota


def contar_aprobados(notas, minimo=61):
    """Cuenta cuántas notas son mayores o iguales al mínimo"""
    aprobados = 0
    
    for nota in notas:
        if nota >= minimo:
            aprobados = aprobados + 1
    
    return aprobados


def reporte(notas):
    """Genera un reporte completo usando todas las funciones"""
    print("\n" + "=" * 55)
    print("        REPORTE DE CALIFICACIONES")
    print("=" * 55)
    print(f"\n📋 Lista de notas: {notas}")
    print("-" * 55)
    
    # Usar las funciones que creamos
    prom = promedio(notas)
    max_nota = mayor(notas)
    min_nota = menor(notas)
    aprobados = contar_aprobados(notas)
    reprobados = len(notas) - aprobados
    
    print(f"📊 ESTADÍSTICAS:")
    print(f"   • Promedio general: {prom:.2f}")
    print(f"   • Nota más alta: {max_nota}")
    print(f"   • Nota más baja: {min_nota}")
    print(f"   • Estudiantes aprobados (≥61): {aprobados}")
    print(f"   • Estudiantes reprobados: {reprobados}")
    print("-" * 55)
    
    # Mostrar aprobados uno por uno
    print("\n✅ NOTAS APROBADAS:")
    aprobadas_lista = []
    for nota in notas:
        if nota >= 61:
            aprobadas_lista.append(nota)
    
    if aprobadas_lista:
        for nota in aprobadas_lista:
            print(f"   • {nota}")
    else:
        print("   • Ninguna nota aprobada")
    
    # Mostrar reprobados uno por uno
    print("\n❌ NOTAS REPROBADAS:")
    reprobadas_lista = []
    for nota in notas:
        if nota < 61:
            reprobadas_lista.append(nota)
    
    if reprobadas_lista:
        for nota in reprobadas_lista:
            print(f"   • {nota}")
    else:
        print("   • Ninguna nota reprobada")
    
    print("\n" + "=" * 55)


# ========== PROGRAMA PRINCIPAL CON INPUT ==========

def obtener_notas_del_usuario():
    """Permite al usuario ingresar notas manualmente"""
    print("\n📝 INGRESO DE NOTAS")
    print("-" * 40)
    print("Instrucciones:")
    print("  • Ingresa una nota por línea")
    print("  • Presiona ENTER sin escribir nada para terminar")
    print("-" * 40)
    
    notas = []
    contador = 1
    
    while True:
        entrada = input(f"Nota {contador}: ")
        
        if entrada == "":
            if len(notas) == 0:
                print("❌ Debes ingresar al menos una nota.")
                continue
            else:
                break
        
        try:
            nota = float(entrada)
            if 0 <= nota <= 100:
                notas.append(nota)
                contador = contador + 1
            else:
                print("❌ La nota debe estar entre 0 y 100")
        except ValueError:
            print("❌ Debes ingresar un número válido")
    
    return notas


# ========== PROGRAMA PRINCIPAL ==========

print("\n" + "🎓" * 28)
print("   SISTEMA DE ANÁLISIS DE CALIFICACIONES")
print("🎓" * 28)

# Opción 1: Usar notas predefinidas
print("\n¿Qué deseas hacer?")
print("  1. Usar notas de ejemplo [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]")
print("  2. Ingresar mis propias notas")
print("  3. Salir")

opcion = input("\n👉 Elige una opción (1/2/3): ")

if opcion == "1":
    # Notas del ejercicio
    notas_ejemplo = [85, 42, 73, 61, 55, 90, 38, 77, 95, 60]
    reporte(notas_ejemplo)
    
    # Mostrar resultados individuales
    print("\n" + "=" * 55)
    print("🔍 PRUEBAS INDIVIDUALES DE CADA FUNCIÓN:")
    print("=" * 55)
    print(f"promedio(notas) = {promedio(notas_ejemplo):.2f}")
    print(f"mayor(notas) = {mayor(notas_ejemplo)}")
    print(f"menor(notas) = {menor(notas_ejemplo)}")
    print(f"contar_aprobados(notas) = {contar_aprobados(notas_ejemplo)}")
    print(f"contar_aprobados(notas, 70) = {contar_aprobados(notas_ejemplo, 70)}")

elif opcion == "2":
    # Ingresar notas manualmente
    notas_usuario = obtener_notas_del_usuario()
    print(f"\n✅ Notas ingresadas: {notas_usuario}")
    reporte(notas_usuario)

elif opcion == "3":
    print("\n👋 ¡Hasta luego!")

else:
    print("\n❌ Opción no válida")