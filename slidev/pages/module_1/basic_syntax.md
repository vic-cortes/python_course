---
layout: cover
transition: fade-out
background: https://cover.sli.dev
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

<v-click>

En python se puede <span v-mark.red="2">definir el tipo.</span>

```python
mensaje: str = "Hola mundo"
edad: int = 25
```
</v-click>


<div v-click>

<br>

<CsharpLogo/>

```csharp
string mensaje = "Hola mundo";
int edad = 25;
```
</div>

<br>

<div mt-20 v-click>

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

<br>

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

<br>

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

<br>

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
