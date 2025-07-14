---
layout: two-cols
---

# Entornos Virtuales en Python

- ¿Qué son los entornos virtuales?
- Beneficios de usar entornos virtuales
- `venv` (módulo incorporado)
- `poetry` (herramienta moderna)
- `uv` (herramienta moderna desarrollada en Rust)

::right::

```python {all|1-2|4-5|7-8|all}
# Crear entorno virtual con venv
python -m venv myenv

# Activar el entorno
source myenv/bin/activate  # Unix
myenv\Scripts\activate     # Windows

# Desactivar
deactivate
```

---
layout: default
---

# Poetry: Gestión Moderna de Entornos

```bash {all|1-2|4-5|7-8|10-11|all}
# Instalar Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Crear nuevo proyecto
poetry new mi-proyecto

# Inicializar en proyecto existente
poetry init

# Activar entorno virtual
poetry shell
```

---

# Estructura del Proyecto con Poetry

```yaml {all|1-4|6-9|11-14|all}
[tool.poetry]
name = "mi-proyecto"
version = "0.1.0"
description = "Descripción del proyecto"

[tool.poetry.dependencies]
python = "^3.8"
requests = "^2.28.0"
pandas = "^1.4.0"

[tool.poetry.dev-dependencies]
pytest = "^7.1.0"
black = "^22.3.0"
flake8 = "^4.0.1"
```

---

# UV: Gestor de Paquetes Ultra Rápido

```bash {all|1-2|4-5|7-8|10-11|all}
# Instalar UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Crear entorno virtual
uv venv

# Instalar dependencias
uv pip install requests pandas

# Instalar desde requirements.txt
uv pip install -r requirements.txt
```

---

# Comparación: venv vs Poetry vs UV

<div class="grid grid-cols-3 gap-4">

<div>
<h3>venv</h3>

- Módulo incorporado en Python
- Simple y directo
- Manejo básico de dependencias
- Ideal para proyectos pequeños
</div>

<div>
<h3>Poetry</h3>

- Gestión moderna de dependencias
- Resolución de dependencias avanzada
- Publicación de paquetes
- Ideal para proyectos medianos/grandes
</div>

<div>
<h3>UV</h3>

- Desarrollado en Rust (ultra rápido)
- Compatible con pip
- Caché binario optimizado
- Ideal para proyectos de cualquier tamaño
</div>

</div>