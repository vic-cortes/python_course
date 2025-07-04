---
layout: cover
---

# Módulos estándar

---


## `os` – Interacción con el sistema operativo.

````md magic-move 
```python
import os
print(os.getcwd())  # Muestra el directorio actual
```


```python
import os

# Crear directorio si no existe
directorio = "mi_proyecto"
if not os.path.exists(directorio):
    os.makedirs(directorio)
    print(f"Directorio '{directorio}' creado")
```


```python
import os

# Información básica del sistema
print(f"Sistema: {os.name}")
print(f"Directorio actual: {os.getcwd()}")
print(f"Usuario: {os.environ.get('USER', 'No encontrado')}")

# Listar archivos del directorio actual
print("\nArchivos en directorio actual:")
for archivo in os.listdir("."):
    ruta = os.path.join(".", archivo)
    if os.path.isfile(ruta):
        size = os.path.getsize(ruta)
        print(f"📄 {archivo} ({size} bytes)")
    else:
        print(f"📁 {archivo}/")
```
```python
import os

# Trabajar con rutas
archivo_ejemplo = "datos.txt"
ruta_completa = os.path.join(directorio, archivo_ejemplo)
print(f"\nRuta completa: {ruta_completa}")

# Obtener información de archivo
if os.path.exists(ruta_completa):
    print(f"El archivo existe y pesa {os.path.getsize(ruta_completa)} bytes")
else:
    print("El archivo no existe")
```
````

---

# `datetime` - Manejo de fechas y horas.

````md magic-move
```python
from datetime import datetime, timedelta, date

# Fecha y hora actual
ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")
print(f"Solo fecha: {ahora.date()}")
print(f"Solo hora: {ahora.time()}")
```
```python
from datetime import datetime, timedelta, date

# Formatear fechas
print(f"Formato personalizado: {ahora.strftime('%d/%m/%Y %H:%M')}")
print(f"Formato completo: {ahora.strftime('%A %d de %B de %Y')}")

# Crear fechas específicas
mi_cumple = datetime(2024, 12, 25, 14, 30)
print(f"Mi cumpleaños: {mi_cumple.strftime('%d/%m/%Y a las %H:%M')}")

# Cálculos con fechas
hace_una_semana = ahora - timedelta(days=7)
en_30_dias = ahora + timedelta(days=30)

print(f"Hace una semana: {hace_una_semana.strftime('%d/%m/%Y')}")
print(f"En 30 días: {en_30_dias.strftime('%d/%m/%Y')}")
```

```python
from datetime import datetime, timedelta, date

ahora = datetime.now()
mi_cumple = datetime(2024, 12, 25, 14, 30)

# Calcular diferencias
diferencia = mi_cumple - ahora

if diferencia.days > 0:
    print(f"Faltan {diferencia.days} días para mi cumpleaños")
else:
    print(f"Mi cumpleaños fue hace {abs(diferencia.days)} días")

# Convertir texto a fecha
fecha_texto = "15/06/2024"
fecha_convertida = datetime.strptime(fecha_texto, "%d/%m/%Y")
print(f"Fecha convertida: {fecha_convertida.strftime('%A %d de %B')}")

# Timestamp (útil para APIs)
timestamp = ahora.timestamp()
print(f"Timestamp: {timestamp}") # Timestamp: 1751601817.871938
fecha_desde_timestamp = datetime.fromtimestamp(timestamp)
print(f"Desde timestamp: {fecha_desde_timestamp}")
```
````

---

# `json` - Leer y escribir datos en formato JSON.

````md magic-move

```python
import json

# Create a Python dictionary with user data
user_data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com",
    "skills": ["Python", "JavaScript", "SQL"],
    "is_active": True,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zip": "10001"
    }
}

print("Original Python dictionary:")
print(user_data)
```
```python
import json

# Convert Python dict to JSON string
json_string = json.dumps(user_data, indent=2)
print("\nConverted to JSON string:")
print(json_string)

# Save to JSON file
with open("user_data.json", "w") as file:
    json.dump(user_data, file, indent=2)

print("\nData saved to 'user_data.json' file")

# Read from JSON file
with open("user_data.json", "r") as file:
    loaded_data = json.load(file)
print("\nData loaded from file:")
print(f"Name: {loaded_data['name']}")
print(f"Skills: {', '.join(loaded_data['skills'])}")
```

```python
import json

# Convert JSON string back to Python dict
json_text = '{"product": "Laptop", "price": 899.99, "in_stock": true}'
parsed_data = json.loads(json_text)
print(f"\nParsed JSON: {parsed_data}")
print(f"Product: {parsed_data['product']}")
print(f"Price: ${parsed_data['price']}")

# Handle JSON with special characters
data_with_special = {
    "message": "Hello, world! 🌍",
    "unicode_text": "café naïve résumé"
}

json_with_unicode = json.dumps(data_with_special, ensure_ascii=False, indent=2)
print(f"\nJSON with Unicode characters:")
print(json_with_unicode)
```
```python
import json

# Error handling
try:
    invalid_json = '{"name": "John", "age": 30,}'  # Invalid JSON (trailing comma)
    json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"\nJSON Error: {e}")
```
````