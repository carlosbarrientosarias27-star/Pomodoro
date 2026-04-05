# 🖥️ `interface.py` — Utilidades de interfaz de consola

Módulo de utilidades para la visualización en terminal. Proporciona dos funciones: limpieza de pantalla multiplataforma y renderizado de una barra de progreso.

---

# Funciones

## `clear_screen()`

Limpia la consola de forma compatible con Windows, macOS y Linux.

```python
from src.utils.interface import clear_screen

clear_screen()
```

**Comportamiento:**
- Detecta el sistema operativo con `platform.system()`.
- Ejecuta `cls` en Windows y `clear` en Unix/macOS mediante `subprocess.run()`.
- Si el comando falla o no se encuentra, lo ignora silenciosamente (sin lanzar excepción).

| Sistema operativo | Comando ejecutado |
|-------------------|:-----------------:|
| Windows           | `cls`             |
| macOS / Linux     | `clear`           |

---

## `progress_bar(current, total, length=30)`

Genera una barra de progreso en formato texto para mostrar en consola.

```python
from src.utils.interface import progress_bar

print(progress_bar(45, 60))
# [█████████████████████         ] 75%

print(progress_bar(0, 60))
# [                              ] 0%

print(progress_bar(60, 60))
# [██████████████████████████████] 100%
```

**Parámetros:**

| Parámetro | Tipo          | Valor por defecto | Descripción                              |
|-----------|---------------|:-----------------:|------------------------------------------|
| `current` | `int`/`float` | —                 | Valor actual del progreso                |
| `total`   | `int`/`float` | —                 | Valor máximo del progreso                |
| `length`  | `int`         | `30`              | Longitud de la barra en caracteres       |

**Retorna:** `str` con el formato `[████░░░░░] XX%`

**Casos especiales:**

| Situación                  | Comportamiento                              |
|----------------------------|---------------------------------------------|
| `total <= 0`               | Devuelve barra vacía con `0%`               |
| `current > total`          | El porcentaje se limita a `100%`            |
| `current < 0`              | La barra se muestra vacía (`0%`)            |
| `current` no numérico      | Lanza `ValueError`                          |

---

# Dependencias

| Módulo       | Uso                                              |
|--------------|--------------------------------------------------|
| `platform`   | Detectar el sistema operativo                    |
| `subprocess` | Ejecutar el comando de limpieza de pantalla      |