#%%

import funciones
from funciones import misfunciones
print("Visual Studio Code is running Python code in this file.")

pepito = "Daniel"

if pepito == "Daniel":
    print("Pepito is Daniel")

print(pepito.index("ie"), pepito[3:])

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    
    def __repr__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
persona1 = Persona("Pepito", 20)
print(persona1)

print(funciones.Texto("Hola Mundo"))  # Llama a la función Texto del módulo funciones
print(misfunciones.Uno())  # Llama a la función Uno del módulo funciones
# %%
