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