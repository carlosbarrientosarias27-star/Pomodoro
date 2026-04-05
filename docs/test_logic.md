# 🧪 Tests — `test_logic.py`

Suite de pruebas para la clase `PomodoroApp` definida en `src/logic.py`, utilizando **pytest** y su sistema de mocks (`monkeypatch`).

# Requisitos

```bash
pip install pytest
```

# Ejecución

```bash
# Ejecutar todos los tests
pytest test_logic.py

# Con salida detallada
pytest test_logic.py -v
```

---

# Fixture auxiliar — `MockConfig`

Clase de configuración mínima usada en todos los tests para evitar dependencias externas:

```python
class MockConfig:
    total_cycles = 4
    work_min = 25
```

---

# Estrategia de mocking

Todos los tests que ejercitan `countdown` parchean las dependencias del módulo `src.logic` directamente, no la instancia:

| Elemento mockeado         | Sustituto                  | Motivo                                         |
|---------------------------|----------------------------|------------------------------------------------|
| `time.sleep`              | `lambda x: None`           | Evitar esperas reales                          |
| `src.logic.clear_screen`  | `lambda: None`             | Evitar efectos en consola                      |
| `src.logic.progress_bar`  | `lambda cur, tot: ""`      | Evitar dependencia de utilidades de interfaz   |
| `src.logic.play_beep`     | `lambda: None` o spy       | Controlar o verificar la señal sonora          |
| `builtins.input`          | `lambda: "q"`              | Simular entrada de teclado                     |

---

# Casos de prueba

### ✅ Casos Normales (N)

## `test_pomodoro_initialization_state`
Verifica que el estado inicial de `PomodoroApp` sea el correcto tras su construcción.

- **Aserción:**
  ```python
  assert app.current_cycle == 0
  assert app.running is True
  assert app.paused is False
  ```

---

## `test_countdown_completes_successfully`
Verifica que un temporizador con duración muy pequeña (`0.01 min`) finaliza correctamente y llama a `play_beep()`.

- **Entradas:** `minutes=0.01`, `label="Test"`
- **Aserción:**
  ```python
  assert beep_called is True
  ```

---

### ⚠️ Casos Límite (L)

## `test_countdown_with_zero_minutes`
Verifica que si `minutes=0`, el bucle no llega a ejecutarse y `sleep` no es invocado en ningún momento.

- **Entradas:** `minutes=0`, `label="Limit"`
- **Aserción:**
  ```python
  assert sleep_calls == 0
  ```

---

## `test_countdown_stops_immediately_if_not_running`
Verifica que si `app.running = False` antes de llamar a `countdown`, el cuerpo del bucle no se ejecuta en absoluto (sin llamadas a `clear_screen`).

- **Entradas:** `minutes=1`, `label="StopTest"`, `app.running = False`
- **Aserción:**
  ```python
  assert executed_loop is False
  ```

---

### 🔴 Casos de Error y Edge Cases (E)

## `test_countdown_pause_loop_execution`
Verifica que mientras la app está pausada (`paused=True`), el temporizador no decrementa el tiempo. El mock de `sleep` detiene el bucle tras la primera iteración.

- **Entradas:** `minutes=1`, `label="PauseTest"`, `app.paused = True`
- **Aserción:**
  ```python
  assert app.paused is True
  ```

---

## `test_listen_keys_quit_logic`
Verifica que al recibir el comando `'q'`, `listen_keys` establece `running = False` y lanza `SystemExit`.

- **Entrada simulada:** `input` devuelve `"q"`
- **Aserción:**
  ```python
  with pytest.raises(SystemExit):
      app.listen_keys()
  assert app.running is False
  ```

---

## `test_countdown_invalid_type_error`
Verifica que pasar un tipo inválido a `minutes` lanza `TypeError`.

- **Entrada:** `minutes="invalid"`, `label="ErrorTest"`
- **Aserción:**
  ```python
  with pytest.raises(TypeError):
      app.countdown("invalid", "ErrorTest")
  ```

---

# Resumen de cobertura

| Test                                        | Categoría | Qué valida                                              |
|---------------------------------------------|-----------|---------------------------------------------------------|
| `test_pomodoro_initialization_state`        | Normal    | Estado inicial correcto de `PomodoroApp`                |
| `test_countdown_completes_successfully`     | Normal    | `countdown` finaliza y ejecuta `play_beep()`            |
| `test_countdown_with_zero_minutes`          | Límite    | `minutes=0` no ejecuta el bucle ni llama a `sleep`      |
| `test_countdown_stops_immediately_if_not_running` | Límite | `running=False` aborta el bucle antes de empezar  |
| `test_countdown_pause_loop_execution`       | Edge case | El estado pausado no decrementa el temporizador         |
| `test_listen_keys_quit_logic`               | Error     | `'q'` detiene la app y lanza `SystemExit`               |
| `test_countdown_invalid_type_error`         | Error     | Tipo inválido en `minutes` lanza `TypeError`            |