---
layout: two-cols
---

# Dataclasses

- Introducción a @dataclass
- Campos y tipos
- Comparación con clases tradicionales
- Opciones de configuración

::right::

```python {all|1-3|5-8|10-14|all}
from typing import List

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    grades: List[float]

# Equivalente tradicional
class StudentTraditional:
    def __init__(self, name: str, grades: List[float]):
        self.name = name
        self.grades = grades
```

---

# Ventajas de Dataclasses vs Clases Tradicionales

| Característica | Dataclass | Clase Tradicional |
|----------------|-----------|-------------------|
| Código boilerplate | Mínimo | Extenso |
| Métodos especiales | Automáticos | Manual |
| Inmutabilidad | Soportada (frozen=True) | Manual |
| Comparaciones | Automáticas (order=True) | Manual |
| Type hints | Obligatorios | Opcionales |

---

```python {all|1-5|7-13|15-21|all}
# Clase tradicional (mucho código)
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __eq__(self, other):
        if not isinstance(other, Person):
            return NotImplemented
        return (
            self.name == other.name and 
            self.age == other.age
        )

# Dataclass (código conciso)
@dataclass(frozen=True, order=True)
class PersonDataclass:
    name: str
    age: int
    # __eq__, __lt__, etc. generados automáticamente
    # Inmutabilidad garantizada por frozen=True
```

---

# Ejemplos de Uso

```python {all|1-7|9-13|15-19|all}
# 1. Configuración con valores por defecto
@dataclass
class ServerConfig:
    host: str = "localhost"
    port: int = 8080
    debug: bool = False
    timeout: float = 30.0

# 2. Data Transfer Objects (DTO)
@dataclass
class UserDTO:
    id: int
    username: str

# 3. Value Objects
@dataclass(frozen=True)
class Money:
    amount: Decimal
    currency: str
```

---

# Comparación de Estructuras

```python {all|1-7|9-14|16-22|all}
# Clase tradicional
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

# Dataclass equivalente
@dataclass
class BookDataclass:
    title: str
    author: str
    year: int
    available: bool = True

# Dataclass con métodos
@dataclass
class Library:
    books: List[BookDataclass]
    
    def add_book(self, book: BookDataclass):
        self.books.append(book)
```

---

# Post-init y Validación

```python {all|1-7|9-16|18-23|all}
@dataclass
class Rectangle:
    width: float
    height: float

    def __post_init__(self):
        self.area = self.width * self.height

@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")

from dataclasses import field

@dataclass
class Cart:
    items: List[Product] = field(default_factory=list)
    total: float = field(init=False, default=0)
```