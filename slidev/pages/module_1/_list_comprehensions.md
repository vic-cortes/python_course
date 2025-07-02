## 1. List Comprehensions

<br>


<PythonLogo/>

````md magic-move 
```python

# For loop
cuadrados = []

for x in range(10):
    cuadrados.append(x**2)

print(cuadrados)  # [0, 1, 4, 9, 16, ..., 81]
```

```python
# List comprehensions
# Crear una lista con los cuadrados del 0 al 9
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, ..., 81]
```
````

<br>

<v-click>
<CsharpLogo/>

```csharp
// (con LINQ)
using System;
using System.Linq;
using System.Collections.Generic;

var cuadrados = Enumerable.Range(0, 10)
                          .Select(x => x * x)
                          .ToList();

Console.WriteLine(string.Join(", ", cuadrados)); // 0, 1, 4, ..., 81
```

</v-click>

<v-click>

-	Python es más conciso con list comprehensions.
-	C# usa Enumerable.Range y Select (LINQ).

</v-click>

---

## 1. List Comprehensions

<br>


<PythonLogo/>

````md magic-move 
```python

# For loop
cuadrados_pares = []

for x in range(10):
    if x % 2 == 0:
        cuadrados_pares.append(x**2)

print(cuadrados_pares)  # [0, 4, 16, 36, 64]
```

```python
# List comprehensions
# Crear una lista con los cuadrados del 0 al 9
cuadrados_pares = [x**2 for x in range(10) if x % 2 == 0]
print(cuadrados_pares)  # [0, 4, 16, 36, 64]
```

```python
# List comprehensions
# Crear una lista con los cuadrados del 0 al 9
cuadrados_pares = [numero**2 for numero in range(10) if numero % 2 == 0]
print(cuadrados_pares)  # [0, 4, 16, 36, 64]
```

```python
# 🐍✨ Modern Python
# List comprehensions
# Crear una lista con los cuadrados del 0 al 9
def is_even(number: int) -> bool:
    """
    Computes if a given number is even
    """
    return number % 2 == 0


cuadrados_pares = [numero**2 for numero in range(10) if is_even(number)]
print(cuadrados_pares)  # [0, 4, 16, 36, 64]
```

```python
# List comprehensions
# Crear una lista con los cuadrados del 0 al 9
def is_even(number: int) -> bool:
    """
    Computes if a given number is even
    """
    return number % 2 == 0


cuadrados_pares = [numero**2 for numero in range(10) if is_even(number) and number != 4]
print(cuadrados_pares)  # [0, 4, 36, 64]
```


````
---

## Otros "Comprehensions"

<br>

`set` Comprehensions


````md magic-move 
```python
unique_words = set()

for word in ["hola", "mundo", "python", "hola"]:
    unique_words.add(word)

# {"mundo", "hola", "python"}
```

```python
unique_words = {word for word in ["hola", "mundo", "python", "hola"]}

# {"mundo", "hola", "python"}
```
````

`dict` Comprehensions


````md magic-move
```python
word_lengths = {}

for word in ["hola", "mundo", "python"]:
    word_lengths[word] = len(word)

# {"hola": 4, "mundo": 5, "python": 6}
```
```python
word_lengths = {word: len(word) for word in ["hola", "mundo", "python"]}

# {"hola": 4, "mundo": 5, "python": 6}
```

````