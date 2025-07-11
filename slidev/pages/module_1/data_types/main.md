---
transition: slide-up
layout: cover
background: https://cover.sli.dev
---

# Tipos de datos
y estructuras de control

---
transition: slide-left
layout: center
---

## 1. Tipos de Datos Primitivos

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

## 2. Tipos de Datos Primitivos

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

<br>

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
src: ./_list_comprehensions.md
---

---
src: ./_unpacking.md
---

---


# Recursos

- [PEP-20](https://peps.python.org/pep-0020/)
- [PEP-8](https://peps.python.org/pep-0008/)
