# ⚙️ `config.py` — Configuración del Pomodoro Timer

Módulo que define la clase `Config`, responsable de almacenar y validar los parámetros configurables de la sesión Pomodoro.

---

# Clase `Config`

## Inicialización

```python
from src.config import Config

config = Config()
```

# Atributos

| Atributo          | Tipo    | Valor por defecto | Descripción                          |
|-------------------|---------|:-----------------:|--------------------------------------|
| `work_min`        | `int`   | `25`              | Duración de la fase de trabajo (min) |
| `short_break_min` | `int`   | `5`               | Duración del descanso corto (min)    |
| `long_break_min`  | `int`   | `15`              | Duración del descanso largo (min)    |
| `total_cycles`    | `int`   | `4`               | Número total de ciclos de la sesión  |

---

# Métodos

## `validate_positive(val)`

Valida que un valor de configuración sea positivo.

```python
config.validate_positive(25)  # True
config.validate_positive(0)   # False
config.validate_positive(-5)  # False
```

**Parámetros:**

| Parámetro | Tipo         | Descripción             |
|-----------|--------------|-------------------------|
| `val`     | `int/float`  | Valor a validar         |

**Retorna:** `True` si `val > 0`, `False` en caso contrario.

---

# Ejemplo de uso

```python
config = Config()

# Modificar valores por defecto
config.work_min = 50
config.short_break_min = 10
config.total_cycles = 2

# Validar antes de asignar
value = int(input("Minutos de trabajo: "))
if config.validate_positive(value):
    config.work_min = value
else:
    print("El valor debe ser mayor que 0.")
```