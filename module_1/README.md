# Introducción y sintaxis moderna

## Filosofía de Python (Zen de Python)

[PEP-20](https://peps.python.org/pep-0020/)

```
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

[PEP-8](https://peps.python.org/pep-0008/)

## Sintaxis básica y diferencias con otros lenguajes

### 1. Declaración de variables

```python
# Python (tipado dinámico)
mensaje = "Hola mundo"
edad = 25
```

```csharp
// C# (tipado estático)
string mensaje = "Hola mundo";
int edad = 25;
```


> NOTA: En python se puede definir el tipo con el modulo `typing`. Más en siguientes módulos


### 2. Funciones

```python
# Python
def saludar(nombre):
    print(f"Hola, {nombre}")
```

```csharp
// C#
void Saludar(string nombre)
{
    Console.WriteLine($"Hola, {nombre}");
}
```

### 3. Condicionales

```python
# Python
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
```

```csharp
// C#
if (edad >= 18)
{
    Console.WriteLine("Es mayor de edad");
}
else
{
    Console.WriteLine("Es menor de edad");
}
```

### 4. For loops

```python
# Python
for i in range(5):
    print(i)
```

```csharp
// C#
for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}
```

### 5. Clases y métodos

```python
# Python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")
```

```csharp
// C#
class Persona
{
    public string Nombre { get; set; }

    public Persona(string nombre)
    {
        Nombre = nombre;
    }

    public void Saludar()
    {
        Console.WriteLine($"Hola, soy {Nombre}");
    }
}
```

> Otra manera de declarar una clase en python es haciendo uso del modulo `dataclass`
> Ejemplo:
> ```python
> from dataclass import dataclass
> 
> @dataclass
> class Persona:
>     nombre: str
> 
>     def saludar(self):
>         print(f"Hola, soy {self.nombre}")
> ```


## Tipos de datos y estructuras de control
## List comprehensions y desempaquetado de variables