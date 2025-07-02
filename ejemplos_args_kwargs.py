"""
Ejemplos de funciones con *args y **kwargs en Python
====================================================
"""

print("=== EJEMPLOS DE *args ===")
print()

# Ejemplo 1: Función que suma números variables
def sumar_numeros(*args):
    """Suma todos los números que se pasen como argumentos"""
    total = 0
    for numero in args:
        total += numero
    return total

# Pruebas con *args
print("1. Función que suma números variables:")
print(f"sumar_numeros(1, 2, 3) = {sumar_numeros(1, 2, 3)}")
print(f"sumar_numeros(10, 20) = {sumar_numeros(10, 20)}")
print(f"sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) = {sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")
print()

# Ejemplo 2: Función que encuentra el máximo
def encontrar_maximo(*args):
    """Encuentra el número máximo entre los argumentos"""
    if not args:
        return None
    return max(args)

print("2. Función que encuentra el máximo:")
print(f"encontrar_maximo(5, 2, 8, 1, 9) = {encontrar_maximo(5, 2, 8, 1, 9)}")
print(f"encontrar_maximo(100, 50, 75) = {encontrar_maximo(100, 50, 75)}")
print()

# Ejemplo 3: Función que imprime nombres
def saludar_personas(*nombres):
    """Saluda a todas las personas que se pasen como argumentos"""
    if not nombres:
        print("No hay nadie a quien saludar")
    else:
        for nombre in nombres:
            print(f"¡Hola, {nombre}!")

print("3. Función que saluda a varias personas:")
saludar_personas("Ana", "Carlos", "María", "Pedro")
print()

print("=== EJEMPLOS DE **kwargs ===")
print()

# Ejemplo 4: Función que muestra información de una persona
def mostrar_info_persona(**kwargs):
    """Muestra información de una persona usando argumentos con nombre"""
    print("Información de la persona:")
    for clave, valor in kwargs.items():
        print(f"  {clave.capitalize()}: {valor}")
    print()

print("4. Función que muestra información de una persona:")
mostrar_info_persona(nombre="Juan", edad=25, ciudad="Madrid", profesion="Ingeniero")
mostrar_info_persona(nombre="Ana", edad=30, pais="España")
print()

# Ejemplo 5: Función que crea un perfil de usuario
def crear_perfil_usuario(nombre, **kwargs):
    """Crea un perfil de usuario con información básica y adicional"""
    perfil = {"nombre": nombre}
    
    # Agregar información adicional del kwargs
    for clave, valor in kwargs.items():
        perfil[clave] = valor
    
    return perfil

print("5. Función que crea un perfil de usuario:")
perfil1 = crear_perfil_usuario("Carlos", edad=28, email="carlos@email.com", hobby="programación")
perfil2 = crear_perfil_usuario("María", edad=32, ciudad="Barcelona", trabajo="Doctora")

print("Perfil 1:", perfil1)
print("Perfil 2:", perfil2)
print()

print("=== EJEMPLOS COMBINANDO *args y **kwargs ===")
print()

# Ejemplo 6: Función que combina ambos
def funcion_completa(nombre, *args, **kwargs):
    """Ejemplo que combina parámetro normal, *args y **kwargs"""
    print(f"Nombre: {nombre}")
    
    if args:
        print("Argumentos posicionales adicionales:")
        for i, arg in enumerate(args, 1):
            print(f"  Arg {i}: {arg}")
    
    if kwargs:
        print("Argumentos con nombre:")
        for clave, valor in kwargs.items():
            print(f"  {clave}: {valor}")
    print()

print("6. Función que combina todo:")
funcion_completa("Pedro", "dato1", "dato2", edad=25, ciudad="Valencia")
funcion_completa("Lucía", profesion="Artista", hobby="pintura")
print()

# Ejemplo 7: Función que simula una calculadora
def calculadora(operacion, *numeros, **opciones):
    """Calculadora que puede realizar diferentes operaciones"""
    if not numeros:
        return "Error: Se necesitan números para calcular"
    
    precision = opciones.get('precision', 2)
    mostrar_proceso = opciones.get('mostrar_proceso', False)
    
    if operacion == "suma":
        resultado = sum(numeros)
        if mostrar_proceso:
            print(f"Sumando: {' + '.join(map(str, numeros))} = {resultado}") # type: ignore
    elif operacion == "multiplicacion":
        resultado = 1
        for num in numeros:
            resultado *= num
        if mostrar_proceso:
            print(f"Multiplicando: {' × '.join(map(str, numeros))} = {resultado}")
    elif operacion == "promedio":
        resultado = sum(numeros) / len(numeros)
        if mostrar_proceso:
            print(f"Promedio de {numeros} = {resultado}")
    else:
        return "Operación no soportada"
    
    return round(resultado, precision)

print("7. Calculadora flexible:")
print(f"Suma: {calculadora('suma', 10, 20, 30, 40)}")
print(f"Multiplicación: {calculadora('multiplicacion', 2, 3, 4, mostrar_proceso=True)}")
print(f"Promedio: {calculadora('promedio', 85, 90, 78, 92, precision=1, mostrar_proceso=True)}")
print()

# Ejemplo 8: Función que registra eventos
def registrar_evento(tipo_evento, *detalles, **metadatos):
    """Registra un evento con detalles y metadatos"""
    print(f"🔔 EVENTO: {tipo_evento.upper()}")
    
    if detalles:
        print("   Detalles:")
        for detalle in detalles:
            print(f"   - {detalle}")
    
    if metadatos:
        print("   Metadatos:")
        for clave, valor in metadatos.items():
            print(f"   - {clave}: {valor}")
    
    print("-" * 40)

print("8. Sistema de registro de eventos:")
registrar_evento("login", "Usuario conectado", "IP verificada", 
                usuario="admin", tiempo="14:30", dispositivo="laptop")

registrar_evento("error", "Conexión fallida", "Timeout después de 30s",
                codigo=500, modulo="database", prioridad="alta")
print()

print("=== CONSEJOS Y BUENAS PRÁCTICAS ===")
print()
print("• *args permite pasar cualquier cantidad de argumentos posicionales")
print("• **kwargs permite pasar cualquier cantidad de argumentos con nombre")
print("• Se pueden combinar parámetros normales, *args y **kwargs")
print("• El orden debe ser: parámetros normales, *args, **kwargs")
print("• Son útiles para crear funciones flexibles y extensibles")
print("• 'args' y 'kwargs' son solo nombres convencionales, puedes usar otros nombres")
