

```bash
uv

# Crear entorno virtual 
uv venv

# Activarlo manualmente
source .venv/bin/activate

# Agregar librerias
uv add flask pandas

# Agregar librerias a un grupo definido
uv add --group dev pytest

# Actualizar todas las dependencias
uv sync --upgrade

# Actualizar dependencias de un grupo específico
uv sync --group dev --upgrade
```