# 🚀 `run.py` — Punto de entrada de la aplicación

Archivo de arranque del Pomodoro Timer. Su única responsabilidad es invocar `start_app()` cuando el script se ejecuta directamente.

# Uso

```bash
python run.py
```

# Funcionamiento

```python
from src.main import start_app

if __name__ == "__main__":
    start_app()
```

El bloque `if __name__ == "__main__"` garantiza que `start_app()` solo se ejecute cuando `run.py` se lanza directamente, y no si el módulo fuera importado desde otro fichero.

# Relación con el resto del proyecto

```
run.py
  └── src/main.py       → start_app() — configura e inicia el ciclo de sesión
        ├── src/config.py   → Config — parámetros de la sesión
        └── src/logic.py    → PomodoroApp — temporizador y control de estado
```