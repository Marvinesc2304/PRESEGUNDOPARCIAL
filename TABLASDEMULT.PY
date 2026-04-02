# Función 1: Tabla de multiplicar
def tabla(n):
    print(f"\nTABLA DEL {n}")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Función 2: Verificar si es primo
def es_primo(n):
    if n < 2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True

# Función 3: Tablas de números primos
def tablas_primos(limite):
    print(f"\n=== TABLAS DE PRIMOS hasta {limite} ===")
    for numero in range(2, limite + 1):
        if es_primo(numero):
            tabla(numero)

# Ejemplo de uso
print("=== EJEMPLO: tablas_primos(10) ===")
tablas_primos(10)

print("\n=== EJEMPLO: tablas_primos(20) ===")
tablas_primos(20)

# Con input del usuario
print("\n" + "=" * 40)
try:
    limite_usuario = int(input("Ingresa un límite para ver las tablas de primos: "))
    tablas_primos(limite_usuario)
except ValueError:
    print("Debes ingresar un número")