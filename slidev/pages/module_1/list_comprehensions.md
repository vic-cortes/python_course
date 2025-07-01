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
