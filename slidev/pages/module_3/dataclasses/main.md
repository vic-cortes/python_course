---
layout: two-cols
---

# Dataclasses

- Introducción a @dataclass
- Campos y tipos
- Comparación con clases tradicionales
- Opciones de configuración

::right::

```python {all|1-2|4-7|9-12|all}
from dataclasses import dataclass
from typing import List

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

# Ventajas de Dataclasses

```python {all|1-4|6-9|11-14|all}
@dataclass(frozen=True)  # Inmutable
class Point:
    x: float
    y: float

@dataclass(order=True)  # Habilita comparaciones
class Score:
    points: int
    player: str

@dataclass(repr=True)  # Representación automática
class Config:
    host: str = "localhost"
    port: int = 8080
```

---

# Comparación de Estructuras

```python {all|1-7|9-15|16-23|all}
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