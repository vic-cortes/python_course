---
layout: center
---

# Módulo 1

Introducción y sintaxis moderna

---
transition: fade-out
---

## Filosofía de Python (Zen de Python)


```python
>>> import this

"""
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
"""
```

---
layout: center
transition: slide-up
---



# Sintaxis básica y diferencias con otros lenguajes

---
transition: slide-left
---

## 1. Declaración de variables
<br>

<div v-click>

<PythonLogo/>

```python
mensaje = "Hola mundo"
edad = 25
```
</div>

<div v-click>

<CsharpLogo/>

```csharp
string mensaje = "Hola mundo";
int edad = 25;
```
</div>

<br>

<v-click>
En python se puede definir el tipo con el modulo <span v-mark.red="4"><code>typing</code></span>. 

</v-click>

<div mt-20 v-click>

> Más en siguientes módulos

</div>

---
transition: slide-left
---

### 2. Funciones

<br>

<v-click>
<PythonLogo/>

```python
def saludar(nombre):
    print(f"Hola, {nombre}")
```
</v-click>

<v-click>
<CsharpLogo/>

```csharp
void Saludar(string nombre)
{
    Console.WriteLine($"Hola, {nombre}");
}
```
</v-click>


---
transition: slide-left
---

### 3. Condicionales
<br>
<v-click>
<PythonLogo/>
```python
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
```
</v-click>

<v-click>
<CsharpLogo/>
```csharp
if (edad >= 18)
{
    Console.WriteLine("Es mayor de edad");
}
else
{
    Console.WriteLine("Es menor de edad");
}
```
</v-click>

---
transition: slide-left
---

### 4. For loops

<br>
<v-click>
<PythonLogo/>

```python
for i in range(5):
    print(i)
```

</v-click>

<v-click>
<CsharpLogo/>

```csharp
for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}
```
</v-click>

---
transition: slide-left
---

### 5. Clases y métodos

<br>
<v-click>
<PythonLogo/>

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}")
```
</v-click>

<v-click>
<CsharpLogo/>

```csharp
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
</v-click>

---
transition: slide-down
layout: center
---

<br>

# Protip

<v-click>

<PythonLogo/>
Otra manera de declarar una clase en python es haciendo uso del módulo 
<span v-mark.red="2"><code>dataclass</code></span>
</v-click>

<v-click>

```python
from dataclass import dataclass

@dataclass
class Persona:
    nombre: str

    def saludar(self):
        print(f"Hola, soy {self.nombre}")
```
</v-click>

---
transition: slide-up
layout: center
---

## Tipos de datos y estructuras de control

---
transition: slide-left
layout: center
---

### 1. Tipos de Datos Primitivos

<br>

| Concepto   | <PythonLogo/>              | <CsharpLogo/>                        |
|------------|--------------------------|----------------------------|
| Entero     | `int`                   | `int`                     |
| Decimal    | `float`                 | `float`, `double`         |
| Cadena     | `str`                   | `string`                  |
| Booleano   | `bool` (`True/False`)   | `bool` (`true/false`)     |


---
transition: slide-left
---

### 1. Tipos de Datos Primitivos

<br>
<v-click>
<PythonLogo/>


```python
x = 10        # int
pi = 3.14     # float
texto = "Hola"
activo = True
```

</v-click>

<v-click>
<CsharpLogo/>

```csharp
int x = 10;
double pi = 3.14;
string texto = "Hola";
bool activo = true;
```

</v-click>


---
transition: slide-left
layout: center
---

### 2. Estructuras de Datos Compuestas

 Tipo        | <PythonLogo/>              | <CsharpLogo/>                           |
|-------------|-----------------------|------------------------------------|
| Lista       | `list`               | `List<T>`                         |
| Tupla       | `tuple`              | `Tuple<T1, T2>`                   |
| Diccionario | `dict`               | `Dictionary<TKey, TValue>`       |
| Conjunto    | `set`                | `HashSet<T>`                      |


---
transition: slide-left
---

### 2. Estructuras de Datos Compuestas

<br>
<v-click>
<PythonLogo/>

```python
lista = [1, 2, 3] # list
tupla = (1, 2) # tuple
dic = {"a": 1, "b": 2} # dictionary
conjunto = {1, 2, 3} # set
```
</v-click>

<v-click>
<br>
<CsharpLogo/>

```csharp
List<int> lista = new List<int> { 1, 2, 3 };
Tuple<int, int> tupla = new Tuple<int, int>(1, 2);
Dictionary<string, int> dic = new Dictionary<string, int> { { "a", 1 }, { "b", 2 } };
HashSet<int> conjunto = new HashSet<int> { 1, 2, 3 };
```
</v-click>

---
transition: slide-left
---

### 3. Estructuras de control

<br>

`if/else`

<v-click>
<PythonLogo/>


```python
if x > 5:
    print("Mayor")
else:
    print("Menor o igual")
```

</v-click>

<v-click>
<br>
<CsharpLogo/>

```csharp
if (x > 5)
{
    Console.WriteLine("Mayor");
}
else
{
    Console.WriteLine("Menor o igual");
}
```
</v-click>

---
transition: slide-left
---

### 3. Estructuras de control

<br>

`for`

<v-click>
<PythonLogo/>


```python
for i in range(5):
    print(i)
```
</v-click>

<v-click>
<br>
<CsharpLogo/>


```csharp
for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}
```
</v-click>

---
transition: slide-left
---

### 3. Estructuras de control

<br>

`while`

<v-click>
<PythonLogo/>


```python
i = 0
while i < 5:
    print(i)
    i += 1
```
</v-click>

<v-click>
<br>
<CsharpLogo/>


```csharp
int i = 0;
while (i < 5)
{
    Console.WriteLine(i);
    i++;
}
```
</v-click>

---
transition: slide-left
---

### 3. Estructuras de control

<br>

`switch`


<div grid="~ cols-2 gap-2" m="t-2">

<v-click>
<div>
<PythonLogo/>

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
</div>
</v-click>

<v-click>
<div>
<CsharpLogo/>

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
</div>
</v-click>

</div>


---
layout: center
---

## List comprehensions y desempaquetado de variables

---

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
---

> 🔍 **NOTA**   
> -	Python es más conciso con list comprehensions.
> -	C# usa Enumerable.Range y Select (LINQ).

---

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

---

# Recursos

- [PEP-20](https://peps.python.org/pep-0020/)
- [PEP-8](https://peps.python.org/pep-0008/)


---