---
layout: two-cols
---

# Clases en Python

- Definición de clases
- Atributos y métodos
- Constructor (__init__)
- Herencia y polimorfismo
- Encapsulamiento

::right::

```python {all|1|2-3|5-6|8-9|all}
class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass

    def __str__(self):
        return f"Animal: {self.name}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self):
        return "Woof!"
```

---
layout: default
---

# Herencia

```python {all|1-2|4-7|9-12|all}
# Herencia múltiple
class Pet:
    def is_vaccinated(self): ...

class ServiceDog(Dog, Pet):
    def __init__(self, name, breed, service_type):
        super().__init__(name, breed)
        self.service_type = service_type
    
    def perform_service(self):
        return f"{self.name} helps with {self.service_type}"
```

---

# Encapsulamiento

```python {all|1-3|5-6|8-11|13-16|all}
class BankAccount:
    def __init__(self):
        self.__balance = 0  # Atributo privado
    
    def deposit(self, amount):
        self.__balance += amount
    
    @property
    def balance(self):
        """Getter para el balance"""
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        """Setter para el balance"""
        self.__balance = max(0, value)
```

---

# Clases Abstractas

````md magic-move
```python
# Clase base simple
class Animal:
    def make_sound(self):
        pass  # No implementación
```

```python
# Clase base con método abstracto implícito
class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement abstract method")
```

```python
# Clase abstracta con ABC
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Este método debe ser implementado por las subclases"""
        pass
```

```python
# Implementación concreta
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        """Este método debe ser implementado por las subclases"""
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Esta línea causaría error:
# animal = Animal()  # TypeError: Can't instantiate abstract class
dog = Dog()  # Esto sí funciona
```
````