# 🧠 `logic.py` — Lógica principal del Pomodoro Timer

Módulo que contiene la clase `PomodoroApp`, responsable del temporizador, el control de estado de la sesión y la escucha de comandos de teclado en tiempo real.

---

# Clase `PomodoroApp`

## Inicialización

```python
app = PomodoroApp(config)
```

| Atributo        | Tipo      | Valor inicial | Descripción                                      |
|-----------------|-----------|:-------------:|--------------------------------------------------|
| `config`        | `Config`  | —             | Objeto de configuración de la sesión             |
| `current_cycle` | `int`     | `0`           | Ciclo actual en curso                            |
| `paused`        | `bool`    | `False`       | Indica si el temporizador está pausado           |
| `running`       | `bool`    | `True`        | Controla si la aplicación debe seguir ejecutándose |

---

# Métodos

## `countdown(minutes, label)`

Ejecuta un temporizador regresivo para una fase de trabajo o descanso.

```python
app.countdown(25, "TRABAJO")
app.countdown(5, "DESCANSO CORTO")
```

**Parámetros:**

| Parámetro | Tipo             | Descripción                              |
|-----------|------------------|------------------------------------------|
| `minutes` | `int` o `float`  | Duración del temporizador en minutos     |
| `label`   | `str`            | Etiqueta de la fase (`"TRABAJO"`, `"DESCANSO CORTO"`, `"DESCANSO LARGO"`) |

**Comportamiento:**
- Muestra en pantalla el modo actual, el ciclo en curso, el tiempo restante y una barra de progreso.
- Se actualiza cada segundo mientras `running` sea `True` y `paused` sea `False`.
- Si está pausado, muestra el estado `(PAUSADO)` y espera 0.5 segundos antes de volver a comprobar.
- Al finalizar el tiempo (`seconds <= 0`), emite una señal sonora mediante `play_beep()`.

**Excepciones:**

| Excepción     | Condición                                         |
|---------------|---------------------------------------------------|
| `TypeError`   | Si `minutes` no es un valor numérico (`int`/`float`) |

---

## `listen_keys()`

Escucha comandos de teclado en segundo plano durante la sesión.

```python
threading.Thread(target=app.listen_keys, daemon=True).start()
```

**Comandos disponibles:**

| Tecla | Acción                                                        |
|-------|---------------------------------------------------------------|
| `p`   | Alterna entre pausar y reanudar el temporizador               |
| `q`   | Detiene la aplicación y termina el proceso (`sys.exit(0)`)    |

> El método se ejecuta en un hilo separado (`daemon=True`) para no bloquear el bucle principal. Termina automáticamente cuando `running` pasa a `False` o se produce un `EOFError`.

---

# Dependencias internas

| Módulo                        | Uso                                              |
|-------------------------------|--------------------------------------------------|
| `src.utils.notifications`     | `play_beep()` — señal sonora al fin del ciclo    |
| `src.utils.interface`         | `clear_screen()` — limpia la consola             |
|                               | `progress_bar()` — barra de progreso visual      |

---

# Flujo interno de `countdown`

```
Inicio
  │
  ├─ ¿minutes es numérico? ──No──► TypeError
  │
  └─ Bucle (seconds > 0 y running)
       │
       ├─ ¿paused == False?
       │     └─ Mostrar tiempo + barra → sleep(1) → seconds -= 1
       │
       └─ ¿paused == True?
             └─ Mostrar estado PAUSADO → sleep(0.5)
  │
  └─ ¿running y seconds == 0? ──► play_beep()
```