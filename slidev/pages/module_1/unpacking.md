## 2. Desempaquetado de variables (Unpacking)

<br>

<v-click>

<PythonLogo/>

```python
# Desempaquetar una tupla
a, b = (1, 2)
print(a)  # 1
print(b)  # 2

# Intercambio de valores
a, b = b, a
```

</v-click>

<br>

<v-click>
<CsharpLogo/>


```csharp
// 🔸 C# (hasta C# 7.0+)
// Desempaquetar tuplas (C# 7.0+)
(int a, int b) = (1, 2);
Console.WriteLine(a);  // 1
Console.WriteLine(b);  // 2

// Intercambio de valores
(a, b) = (b, a);
```
</v-click>

---

## 2. Desempaquetado de variables (Unpacking)

Desempaquetado parcial con `*`

```python
a, *b = [1, 2, 3, 4]
print(a)  # 1
print(b)  # [2, 3, 4]

*a, b = [1, 2, 3, 4]
print(a)  # [1, 2, 3]
print(b)  # 4
```

En `loops`

```python
puntos = [(1, 2), (3, 4), (5, 6)]

for x, y in puntos:
    print(f"x={x}, y={y}")
```

---

Desempaquetar diccionarios (claves, valores)

```python
d = {'a': 1, 'b': 2}

# Desempaquetar claves
x, y = d
print(x, y)  # 'a' 'b'

# Desempaquetar ítems
for clave, valor in d.items():
    print(clave, valor)
```

Con funciones

```python
def coordenadas():
    return (10, 20)

x, y = coordenadas()
```