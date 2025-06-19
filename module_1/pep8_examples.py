# Ejemplos de buenas prácticas según PEP 8


#! 1. Indentación con 4 espacios
def saludar(nombre):
    # Se usa 4 espacios para la indentación
    if nombre:
        print(f"Hola, {nombre}!")


#! 2. Longitud de línea menor a 79 caracteres
mensaje = "Este mensaje está dentro del límite recomendado de caracteres."

#! 3. Espacios en expresiones
a = 1
b = 2
suma = a + b

#! 4. Nombres de funciones, clases y constantes


# Función: snake_case
def calcular_area_circulo(radio):
    return 3.1416 * radio**2


# Clase: CamelCase
class FiguraGeometrica:
    pass


# Constante: MAYÚSCULAS_CON_GUIONES_BAJOS
PI = 3.1416


#! 5. Líneas en blanco entre funciones y clases
def funcion_1():
    pass


def funcion_2():
    pass


class MiClase:
    pass


#! 6. Importaciones ordenadas y separadas

# Módulos estándar
import os
import sys

# Módulos de terceros
import requests

# Módulos locales
from my_example_package.example import dummy_function

dummy_function()
