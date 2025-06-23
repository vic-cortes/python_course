---
marp: true
style: |
    .columns {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 1rem;
    }
---

# Módulo 2: Funciones, módulos y manejo de errores

---

## Funciones

---

### 🧠 Objetivo:

Crear una función que procese una lista de números, aplique una operación específica (como suma, media, etc.), use `*args/**kwargs`, maneje posibles errores, y esté tipada correctamente. Además, usaremos un módulo estándar (statistics) y uno externo opcional (numpy, si está disponible).


---

### 1. Función básica



```python
def saludar():
    print("¡Hola mundo!")

saludar()
```


### 2. Función con parámetros

```python
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Lucía")  # Hola, Lucía
```


> `f-strings` fueron introducidas en pyhthon 3.8

---

### 3. Parámetros con valor por defecto

```python
def saludar(nombre="amigo"):
    print(f"Hola, {nombre}")

saludar()          # Hola, amigo
saludar("Luis")    # Hola, Luis
```

### 4. `*args`: argumentos variables (tupla)

```python
def sumar(*numeros):
    total = sum(numeros)
    print(f"Total: {total}")

sumar(1, 2, 3)  # Total: 6
```

---

### 5. `**kwargs`: argumentos nombrados variables (diccionario)

```python
def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30)
# nombre: Ana
# edad: 30
```

### 6. Función con tipado estático (typing)

```python
from typing import List

def promedio(numeros: List[float]) -> float:
    return sum(numeros) / len(numeros)

print(promedio([5.0, 7.5, 10]))  # 7.5
```

---

### 7. Función que retorna un valor

```python
def cuadrado(n):
    return n * n

resultado = cuadrado(5)
print(resultado)  # 25
```