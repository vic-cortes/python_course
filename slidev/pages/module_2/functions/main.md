
# 1. Función básica


````md magic-move 
```python
def saludar():
    print("¡Hola mundo!")

saludar()
```

```python
# 🐍✨ Pythonic
def saludar() -> None:
    """
    Función que imprime saludo
    """
    print("¡Hola mundo!")

saludar()
```
````

---

# 2. Función con parámetros

````md magic-move 
```python
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Lucía")  # Hola, Lucía
```

```python
# 🐍✨ Pythonic
def saludar(nombre: str) -> None:
    """
    Función que imprime saludo con nombre
    """
    print(f"Hola, {nombre}")

saludar("Lucía")  # Hola, Lucía
# f string son introducidas en python 3.8
```

```python
# 3.7
def saludar(nombre: str) -> None:
    """
    Función que imprime saludo con nombre
    """
    print("Hola, {}".format(nombre))

saludar("Lucía")  # Hola, Lucía
```
````




---

# 3. Parámetros con valor por defecto

````md magic-move
```python
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}")

saludar()          # Hola, amigo
saludar("Luis")    # Hola, Luis
```

```python
# 🐍✨ Pythonic
def saludar(nombre: str ="amigo") -> None:
    """
    Función que acepta nombre pero tiene valor
    por defecto.
    """
    print(f"Hola, {nombre}")

saludar()          # Hola, amigo
saludar("Luis")    # Hola, Luis
```
````

---

# 4. `*args`: argumentos variables (tupla)

````md magic-move
```python
def sumar(first, second, third):
    total = sum([first, second, third])
    print(f"Total: {total}")

sumar(1, 2, 3)  # Total: 6
```
```python
def sumar(*numeros):
    total = sum(numeros)
    print(f"Total: {total}")

sumar(1, 2, 3)  # Total: 6
```
```python
def sumar(*args):
    total = sum(args)
    print(f"Total: {total}")

sumar(1, 2, 3)  # Total: 6
```
````

---

# 5. `**kwargs`: argumentos nombrados variables (diccionario)

````md magic-move
```python
def mostrar_info(nombre, edad):
    value = f"nombre: {nombre}\nedad: {edad}"
    print(value)

mostrar_info(nombre="Ana", edad=30)
# nombre: Ana
# edad: 30
```

```python
def mostrar_info(nombre, edad):
    value = f"nombre: {nombre}\nedad: {edad}"
    print(value)

mostrar_info(nombre="Ana", edad=30, apellido="Perez")
# nombre: Ana
# edad: 30
```

```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30)
# nombre: Ana
# edad: 30
```
```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, apellido="Perez")
# nombre: Ana
# edad: 30
# apellido: Perez

```
```python
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, apellido="Perez")
# nombre: Ana
# edad: 30
# apellido: Perez
```
````

---

# 6. Función con tipado estático (typing)

````md magic-move
```python
# 3.7, 3.8
from typing import List

def promedio(numeros: List[float]) -> float:
    return sum(numeros) / len(numeros)

print(promedio([5.0, 7.5, 10]))  # 7.5
```
```python
# >= 3.9
def promedio(numeros: list[float]) -> float:
    return sum(numeros) / len(numeros)

print(promedio([5.0, 7.5, 10]))  # 7.5
```
````

---

### 7. Función que retorna un valor

```python
def cuadrado(n):
    return n * n

resultado = cuadrado(5)
print(resultado)  # 25
```