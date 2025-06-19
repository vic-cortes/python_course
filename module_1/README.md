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


> 🔍 **NOTA**  
> En python se puede definir el tipo con el modulo `typing`. Más en siguientes módulos


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
> 🔍 **NOTA**  
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



### 1. 🔢 Tipos de Datos Primitivos

| Concepto   | Python                  | C#                        |
|------------|--------------------------|----------------------------|
| Entero     | `int`                   | `int`                     |
| Decimal    | `float`                 | `float`, `double`         |
| Cadena     | `str`                   | `string`                  |
| Booleano   | `bool` (`True/False`)   | `bool` (`true/false`)     |


```python
# Python
x = 10        # int
pi = 3.14     # float
texto = "Hola"
activo = True
```

```csharp
// C#
int x = 10;
double pi = 3.14;
string texto = "Hola";
bool activo = true;
```

### 2. 📦 Estructuras de Datos Compuestas

 Tipo        | Python               | C#                                |
|-------------|-----------------------|------------------------------------|
| Lista       | `list`               | `List<T>`                         |
| Tupla       | `tuple`              | `Tuple<T1, T2>`                   |
| Diccionario | `dict`               | `Dictionary<TKey, TValue>`       |
| Conjunto    | `set`                | `HashSet<T>`                      |


```python
# Python
lista = [1, 2, 3]
tupla = (1, 2)
dic = {"a": 1, "b": 2}
conjunto = {1, 2, 3}
```

```csharp
// C#
List<int> lista = new List<int> { 1, 2, 3 };
Tuple<int, int> tupla = new Tuple<int, int>(1, 2);
Dictionary<string, int> dic = new Dictionary<string, int> { { "a", 1 }, { "b", 2 } };
HashSet<int> conjunto = new HashSet<int> { 1, 2, 3 };
```

### 🔁 3. Estructuras de control

#### `if/else`

```python
# Python
if x > 5:
    print("Mayor")
else:
    print("Menor o igual")
```

```csharp
// C#
if (x > 5)
{
    Console.WriteLine("Mayor");
}
else
{
    Console.WriteLine("Menor o igual");
}
```

#### `for`

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

#### `while`

```python
# Python
i = 0
while i < 5:
    print(i)
    i += 1
```

```csharp
// C#
int i = 0;
while (i < 5)
{
    Console.WriteLine(i);
    i++;
}
```

#### `switch`

🔸 Python ≥3.10 tiene match (similar a switch):

```python
# Python 3.10+
match x:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case _:
        print("Otro")
```

```csharp
// C# 8+
switch (x)
{
    case 1:
        Console.WriteLine("Uno");
        break;
    case 2:
        Console.WriteLine("Dos");
        break;
    default:
        Console.WriteLine("Otro");
        break;
}
```

## List comprehensions y desempaquetado de variables

### 1. List Comprehensions

```python
# Python
# Crear una lista con los cuadrados del 0 al 9
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, ..., 81]
```

```csharp
// 🔸 C# (con LINQ)
using System;
using System.Linq;
using System.Collections.Generic;

var cuadrados = Enumerable.Range(0, 10)
                          .Select(x => x * x)
                          .ToList();

Console.WriteLine(string.Join(", ", cuadrados)); // 0, 1, 4, ..., 81
```

> 🔍 **NOTA**   
> -	Python es más conciso con list comprehensions.
> -	C# usa Enumerable.Range y Select (LINQ).

### 2. Desempaquetado de variables (Unpacking)

```python
# Desempaquetar una tupla
a, b = (1, 2)
print(a)  # 1
print(b)  # 2

# Intercambio de valores
a, b = b, a
```

```csharp
// 🔸 C# (hasta C# 7.0+)
// Desempaquetar tuplas (C# 7.0+)
(int a, int b) = (1, 2);
Console.WriteLine(a);  // 1
Console.WriteLine(b);  // 2

// Intercambio de valores
(a, b) = (b, a);
```