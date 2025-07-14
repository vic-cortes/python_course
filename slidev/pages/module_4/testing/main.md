---
layout: two-cols
---

# Pruebas con pytest

- Introducción a pytest
- Estructura de pruebas
- Fixtures
- Aserciones y marcadores
- Buenas prácticas

::right::

```python {all|1-2|4-7|9-12|all}
# test_calculator.py
from calculator import add

def test_add_positive_numbers():
    result = add(1, 2)
    assert result == 3

def test_add_negative_numbers():
    result = add(-1, -2)
    assert result == -3
```

---

# Estructura de Pruebas

```
proyecto/
├── src/
│   └── calculator.py
└── tests/
    ├── __init__.py
    ├── test_calculator.py
    └── conftest.py
```

```python {all|1-4|6-9|11-14|all}
# calculator.py
def add(a: int, b: int) -> int:
    """Suma dos números enteros."""
    return a + b

# test_calculator.py
def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0

# conftest.py
import pytest
def pytest_configure(config):
    """Configuración global de pytest."""
```

---

# Fixtures en pytest

```python {all|1-5|7-11|13-18|all}
@pytest.fixture
def numbers():
    """Fixture que provee números de prueba."""
    return [1, 2, 3, 4, 5]

@pytest.fixture
def calculator():
    """Fixture que provee una instancia de Calculator."""
    return Calculator()

def test_sum_list(calculator, numbers):
    """Prueba que usa múltiples fixtures."""
    total = calculator.sum_list(numbers)
    assert total == 15
    assert isinstance(total, int)
```

---

# Marcadores y Parametrización

```python {all|1-4|6-11|13-19|all}
@pytest.mark.slow
def test_complex_calculation():
    """Prueba marcada como lenta."""
    assert complex_calc() == 42

@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25)
])
def test_square(input, expected):
    assert square(input) == expected

@pytest.mark.skip(reason="No implementado aún")
def test_future_feature():
    pass

@pytest.mark.xfail
def test_known_bug():
    assert buggy_function() == True
```

---

# Cobertura y Reportes

```bash {all|1-2|4-5|7-8|all}
# Ejecutar pruebas con cobertura
pytest --cov=src tests/

# Generar reporte HTML
pytest --cov=src --cov-report=html

# Ejecutar pruebas con JUnit XML
pytest --junitxml=report.xml
```

<div class="mt-4">

### Comandos Útiles

- `pytest -v`: Modo verboso
- `pytest -k "test_name"`: Filtrar pruebas
- `pytest -m "slow"`: Ejecutar pruebas marcadas
- `pytest --pdb`: Debugger en fallos
</div>

---

# Buenas Prácticas

<div class="grid grid-cols-2 gap-4">

<div>

### Organización ✅

- Un archivo por módulo
- Nombres descriptivos
- Pruebas independientes
- Uso de fixtures
- Documentación clara
</div>

<div>

### Diseño de Pruebas ✅

- Pruebas unitarias pequeñas
- Casos borde
- Parametrización
- Mocks cuando necesario
- Cobertura > 80%
</div>

</div>