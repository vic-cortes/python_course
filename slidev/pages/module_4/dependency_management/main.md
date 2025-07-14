---
layout: two-cols
---

# Gestión de Dependencias

- Instalación de paquetes con pip
- requirements.txt
- Versiones de paquetes
- Buenas prácticas

::right::

```bash {all|1-2|4-5|7-8|all}
# Instalar un paquete
pip install requests

# Instalar versión específica
pip install requests==2.28.0

# Instalar con restricciones de versión
pip install "requests>=2.28.0,<3.0.0"
```

---

# Trabajando con requirements.txt

```bash {all|1-2|4-5|7-8|all}
# Generar requirements.txt
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt

# Actualizar dependencias
pip install -U -r requirements.txt
```

---

# Estructura de requirements.txt

```txt {all|1-3|5-7|9-11|all}
# Dependencias principales
requests==2.28.0
pandas==1.4.0

# Dependencias de desarrollo
pytest>=7.1.0
black==22.3.0

# Dependencias opcionales
python-dotenv>=0.19.0
pillow~=9.0.0
```

---

# Buenas Prácticas

<div class="grid grid-cols-2 gap-4">

<div>

### Recomendado ✅

```txt
requests==2.28.0
pandas==1.4.0
```

- Versiones específicas
- Separar dev y prod
- Documentar dependencias
- Actualizar regularmente
</div>

<div>

### Evitar ❌

```txt
requests
pandas>=1.0.0
```

- Versiones sin especificar
- Mezclar entornos
- Dependencias innecesarias
- Versiones obsoletas
</div>

</div>

---

# Herramientas Adicionales

<div class="grid grid-cols-2 gap-4">

<div>

### pip-tools

- Bloqueo de versiones
- Resolución de dependencias
- Archivo requirements.in

```bash
# Generar requirements.txt
pip-compile requirements.in
```
</div>

<div>

### pipdeptree

- Visualizar dependencias
- Detectar conflictos
- Análisis de paquetes

```bash
# Ver árbol de dependencias
pipdeptree
```
</div>

</div>