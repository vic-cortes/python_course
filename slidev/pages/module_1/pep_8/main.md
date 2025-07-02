---
layout: cover
background: https://sli.dev/demo-cover.png
---

# PEP 8
Mejores prácticas en python

---

# 1. Indentación con 4 espacios

````md magic-move 
```python
# ❌ Wrong
def saludar(nombre):
  if nombre:
    print(f"Hola, {nombre}!")
```


```python
# ✅ Good
def saludar(nombre):
    # Se usa 4 espacios para la indentación
    if nombre:
        print(f"Hola, {nombre}!")
```
````

---

# 2. Longitud de línea menor a 79 caracteres

````md magic-move 
```python
mensaje = "Este mensaje está dentro del límite recomendado de caracteres."
```
```python
# ❌ Wrong
mensaje = "Este mensaje está dentro del límite recomendado de caracteres. Rebasa el limite de caracteres"
```
```python
# ✅ Good
mensaje = "Este mensaje está dentro del límite recomendado de caracteres." \
          "Rebasa el limite de caracteres"
```
````

---

# 3. Espacios en expresiones

````md magic-move 
```python
# ❌ Wrong
a=1
b=2
suma=a+b
```

```python
# ✅ Good
a = 1
b = 2
suma = a + b
```
````

---

# 4. Nombres de funciones, clases y constantes


````md magic-move 
```python
# ❌ Wrong
def calcularAreaCirculo(radio):
    return 3.1416 * radio**2


class figura_geometrica:
    pass


pi = 3.1416
```

```python
# ✅ Good
# Función: `snake_case`
def calcular_area_circulo(radio):
    return 3.1416 * radio**2


# Clase: CamelCase
class FiguraGeometrica:
    pass


# Constante: MAYÚSCULAS_CON_GUIONES_BAJOS
PI = 3.1416
```

```python
# 🐍✨ Modern Python

# Constante: MAYÚSCULAS_CON_GUIONES_BAJOS
PI = 3.1416

# Función: `snake_case`
def calcular_area_circulo(radio: float) -> float:
    return PI * radio**2


# Clase: CamelCase
class FiguraGeometrica:
    pass

```
````

---

# 5. Líneas en blanco entre funciones y clases

````md magic-move 
```python
# ❌ Wrong
def funcion_1():
    pass
def funcion_2():
    pass






class MiClase:
    pass
```

```python
# ✅ Good
def funcion_1():
    pass


def funcion_2():
    pass


class MiClase:
    pass
```
````

---

# 6. Importaciones ordenadas y separadas

````md magic-move 
```python
# ❌ Wrong
import requests
import os
from my_example_package.example import dummy_function
import sys

dummy_function()
```

```python
# ✅ Good
# Módulos estándar
import os
import sys

# Módulos de terceros
import requests

# Módulos locales
from my_example_package.example import dummy_function

dummy_function()
```
````
