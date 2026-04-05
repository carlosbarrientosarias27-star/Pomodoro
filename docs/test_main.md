# 🧪 Tests — `test_main.py`

Suite de pruebas para el punto de entrada principal de la aplicación Pomodoro (`src/main.py`), utilizando **pytest** y su sistema de mocks (`monkeypatch`).

# Requisitos

```bash
pip install pytest
```

# Ejecución

```bash
# Ejecutar todos los tests
pytest test_main.py

# Con salida detallada
pytest test_main.py -v
```

# Estrategia de mocking

Dado que `start_app()` depende de entrada de usuario, temporizadores reales e hilos en segundo plano, todos los tests aplican los siguientes mocks para garantizar ejecución rápida y determinista:

| Elemento mockeado          | Sustituto                        | Motivo                                      |
|----------------------------|----------------------------------|---------------------------------------------|
| `builtins.input`           | Iterador con valores predefinidos | Evitar interacción manual                   |
| `PomodoroApp.countdown`    | Función personalizada            | Evitar esperas reales y controlar el flujo  |
| `threading.Thread.start`   | `lambda x: None`                 | Evitar hilos paralelos en los tests         |
| `clear_screen`             | `lambda: None`                   | Evitar efectos en la consola                |
| `time.sleep`               | `lambda x: None`                 | Evitar pausas reales                        |

---

# Casos de prueba

### ✅ Casos Normales (N)

## `test_start_app_initialization_flow`
Verifica que `start_app()` arranca y completa su flujo sin errores cuando se usan los **valores por defecto** (inputs vacíos).

- **Entradas simuladas:** `""`, `""`, `""`
- **Comportamiento esperado:** El mock de `countdown` detiene el bucle inmediatamente (`self.running = False`). La función finaliza sin bloqueos ni esperas reales.
- **Criterio de éxito:** Llegar al final de `start_app()` sin excepciones ni timeouts.

---

## `test_start_app_custom_values_assignment`
Verifica que los **valores introducidos por el usuario** se asignan correctamente a la configuración de la aplicación.

- **Entradas simuladas:** `"10"` (trabajo), `"2"` (descanso corto), `"1"` (ciclos)
- **Comportamiento esperado:** El mock de `countdown` captura `self.config.work_min` en el momento de ejecutarse.
- **Aserción:**
  ```python
  assert captured_config['work'] == 10
  ```

---

# ⚠️ Casos Límite (L)

## `test_start_app_completes_all_cycles`
Verifica que con **un único ciclo configurado**, `countdown` se invoca exactamente **una vez** (solo la fase de trabajo, sin descanso posterior).

- **Entradas simuladas:** `"1"`, `"1"`, `"1"`
- **Comportamiento esperado:** El bucle principal ejecuta un ciclo de trabajo y, al ser el último ciclo, no programa descanso.
- **Aserción:**
  ```python
  assert stats["cycles"] == 1
  ```

---

# Resumen de cobertura

| Test                                    | Categoría | Qué valida                                      |
|-----------------------------------------|-----------|-------------------------------------------------|
| `test_start_app_initialization_flow`    | Normal    | Flujo completo sin errores con valores por defecto |
| `test_start_app_custom_values_assignment` | Normal  | Asignación correcta de parámetros del usuario   |
| `test_start_app_completes_all_cycles`   | Límite    | Número exacto de llamadas a `countdown`         |