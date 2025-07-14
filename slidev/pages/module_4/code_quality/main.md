---
layout: two-cols
---

# Herramientas de Calidad de Código

- Linters y formatters
- Tipos de herramientas
- Configuración
- Integración con editores

::right::

```python {all|1-3|5-7|9-11|all}
# Código original
def calculate(x,y):
    return x+y

# Después de black
def calculate(x, y):
    return x + y

# Con type hints (mypy)
def calculate(x: int, y: int) -> int:
    return x + y
```

---

# Black - El Formateador de Python

```python {all|1-5|7-11|13-17|all}
# Antes de black
def long_function(arg1,arg2,
    arg3,arg4):
    x=[1,2,3]
    return x

# Después de black
def long_function(
    arg1, arg2, arg3, arg4
):
    x = [1, 2, 3]
    return x

# Black es inflexible por diseño
# No hay opciones de configuración
# "Any color you like, as long as it's black"
```

---

# Flake8 - Linter

```python {all|1-6|8-13|15-19|all}
# Problemas que detecta flake8
x = 42 # E261 at least two spaces before inline comment

def func(): # E301 expected 1 blank line
    y = [1,2] # E231 missing whitespace after ','
    return y

# Configuración en setup.cfg
[flake8]
max-line-length = 88
extend-ignore = E203
exclude = .git,__pycache__,build,dist
max-complexity = 10

# Ignorar en línea específica
x = 1 # noqa: E261

y = [
    1, 2, 3  # noqa: E231
]
```

---

# Mypy - Verificación de Tipos

```python {all|1-5|7-11|13-17|all}
from typing import List, Optional

def find_user(id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(id)

# Error de tipo
def process_items(items: List[int]) -> int:
    return sum(items)

process_items(["1", "2"])  # Error!

# Union de tipos
from typing import Union

def process_data(x: Union[int, str]) -> str:
    return str(x)
```

---

# Configuración e Integración

<div class="grid grid-cols-2 gap-4">

<div>

### Configuración

```toml
# pyproject.toml
[tool.black]
line-length = 88
target-version = ['py37']

[tool.mypy]
disallow_untyped_defs = true
check_untyped_defs = true
```
</div>

<div>

### Pre-commit

```yaml
# .pre-commit-config.yaml
repos:
- repo: https://github.com/psf/black
  rev: 22.3.0
  hooks:
    - id: black
- repo: https://github.com/pycqa/flake8
  rev: 4.0.1
  hooks:
    - id: flake8
```
</div>

</div>

---

# Mejores Prácticas

<div class="grid grid-cols-2 gap-4">

<div>

### Recomendaciones ✅

- Usar Black sin configuración
- Flake8 compatible con Black
- Mypy gradualmente
- Pre-commit hooks
- CI/CD integración
</div>

<div>

### VSCode Setup

```json
{
  "python.formatting.provider": "black",
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "editor.formatOnSave": true
}
```
</div>

</div>