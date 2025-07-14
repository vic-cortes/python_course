---
layout: two-cols
---

# Decoradores en Python

- Funciones como decoradores
- Built-in decoradores (@property, @staticmethod)
- Creación de decoradores personalizados
- Decoradores con argumentos

::right::

```python {all|1-3|5-8|10-13|all}
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name):
    return f"Hello, {name}!"
```

---

# Métodos Especiales

```python {all|1-3|5-7|9-11|13-15|all}
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __str__(self):
        """Representación legible"""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        """Representación para debugging"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Sobrecarga del operador +"""
        return Vector(self.x + other.x, self.y + other.y)
```

---

# Properties

```python {all|1-4|6-9|11-14|16-19|all}
class Temperature:
    def __init__(self, celsius=0):
        """Almacena la temperatura en Celsius"""
        self._celsius = celsius
    
    @property
    def celsius(self):
        """Getter para celsius"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter para celsius"""
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Conversión automática a Fahrenheit"""
        return (self._celsius * 9/5) + 32
```

<!-- ---

# Decoradores con Argumentos

```python {all|1-4|6-9|11-16|all}
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def print_message(msg):
    print(msg)

# Equivalente a:
# print_message = repeat(times=3)(print_message) -->