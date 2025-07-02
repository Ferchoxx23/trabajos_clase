# %%
def imprime_nombres(misnombres: list, repetir: int, *args):
    for item in misnombres:
        print(item, ' ', '*'*repetir)
    print(args)
    if "Pepito" in args:
        print("Pepito esta !!!!")


misnombres = ['Daniel', 'Andres', 'Joaquin', 'Facundo', 'Marcela', 'Aldana']
imprime_nombres(repetir=5, misnombres=misnombres)
imprime_nombres(misnombres, 7, "Pepito", "Hola")

# %%


def operaciones(a: int, *args, b: int | None = 1):
    print(args)
    if "suma" in args:
        if b:
            print(f"La suma de a + b es {a + b}")
    if "resta" in args:
        if b:
            print(f"La resta de a - b es {a - b}")
    if "multi" in args:
        if b:
            print(f"La multiplicación de a * b es {a * b}")
    if len(args) == 0:
        print("No se cargo ninguna operacion para realizar")

opera = ['suma', 'resta', 'multi']
nombres = [
    'María', 'Ana', 'Carmen', 'Isabel', 'Dolores', 'Pilar', 'Teresa', 'Rosa',
    'Francisca', 'Antonia', 'Josefa', 'Concepción', 'Mercedes', 'Esperanza',
    'Ángeles', 'Manuela', 'Encarnación', 'Rosario', 'Cristina', 'Montserrat',
    'Consuelo', 'Amparo', 'Asunción', 'Remedios', 'Milagros', 'Dolores',
    'Soledad', 'Gloria', 'Purificación', 'Natividad', 'Inmaculada', 'Vicenta',
    'Presentación', 'Consolación', 'Adoración', 'Visitación', 'Ascensión',
    'Magdalena', 'Salud', 'Esperanza', 'Paz', 'Felicidad', 'Caridad',
    'Virtudes', 'Milagros', 'Socorro', 'Amparo', 'Nieves', 'Rocío',
    'Luz', 'Esperanza', 'Fe', 'Caridad', 'Prudencia'
]

apellido = [
    'García', 'Martínez', 'López', 'Sánchez', 'Pérez', 'González', 'Rodríguez', 'Fernández',
    'Ruiz', 'Gómez', 'Díaz', 'Álvarez', 'Moreno', 'Muñoz', 'Romero', 'Alonso',
    'Gutiérrez', 'Navarro', 'Torres', 'Domínguez', 'Vázquez', 'Ramos', 'Gil', 'Serrano',
    'Molina', 'Blanco', 'Morales', 'Suárez', 'Ortega', 'Delgado', 'Castro', 'Ortiz',
    'Rubio', 'Marín', 'Sanz', 'Iglesias', 'Núñez', 'Medina', 'Garrido', 'Cruz',
    'Santos', 'Castillo', 'Cortés', 'Lozano', 'Guerrero', 'Cano', 'Prieto', 'Méndez',
    'Flores', 'Herrera'
]

# operaciones(5, 20, "multi", "suma")
operaciones(6, "resta",b=3)
# operaciones(25, 100, '2')
# operaciones(
#     int(input('Ingrese el primer numero')), 
#     int(input('Ingrese el segundo numero')),
#     *[opera[0], opera[2]]
# )

# %%
