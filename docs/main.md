# 🍅 Pomodoro Timer

Aplicación de línea de comandos para gestionar sesiones de trabajo y descanso mediante la técnica Pomodoro.

# ¿Qué es la técnica Pomodoro?

La técnica Pomodoro consiste en dividir el trabajo en intervalos de tiempo (normalmente 25 minutos), separados por breves descansos. Tras completar varios ciclos, se toma un descanso más largo.

# Estructura del proyecto

```
.
├── main.py              # Punto de entrada de la aplicación
└── src/
    ├── config.py        # Configuración y valores por defecto
    ├── logic.py         # Lógica principal (PomodoroApp)
    └── utils/
        └── interface.py # Utilidades de interfaz (clear_screen, etc.)
```

# Requisitos

- Python 3.7 o superior
- No requiere dependencias externas

# Uso

```bash
python main.py
```

Al iniciar, la aplicación solicitará los parámetros de la sesión:

```
--- BIENVENIDO AL POMODORO TIMER ---
Minutos de trabajo (default 25):
Minutos de descanso corto (default 5):
Total de ciclos (default 4):
```

Puedes pulsar **Enter** en cada campo para aceptar el valor por defecto.

# Configuración

| Parámetro              | Valor por defecto | Descripción                              |
|------------------------|:-----------------:|------------------------------------------|
| `work_min`             | 25 min            | Duración de cada sesión de trabajo       |
| `short_break_min`      | 5 min             | Duración del descanso corto              |
| `long_break_min`       | 15 min            | Duración del descanso largo              |
| `total_cycles`         | 4                 | Número total de ciclos a completar       |

> El descanso largo se activa automáticamente cada 4 ciclos completados.

# Flujo de una sesión

```
Ciclo 1 → TRABAJO (25 min) → DESCANSO CORTO (5 min)
Ciclo 2 → TRABAJO (25 min) → DESCANSO CORTO (5 min)
Ciclo 3 → TRABAJO (25 min) → DESCANSO CORTO (5 min)
Ciclo 4 → TRABAJO (25 min) → DESCANSO LARGO (15 min)
          ↓
    ¡Sesión completada!
```

# Controles

| Tecla              | Acción                        |
|--------------------|-------------------------------|
| `Ctrl + C`         | Detener el programa           |
| Teclas de teclado  | Gestionadas por `listen_keys` |

# Módulos principales

## `main.py`
Punto de entrada. Se encarga de:
- Inicializar la configuración (`Config`) y la aplicación (`PomodoroApp`)
- Solicitar los parámetros al usuario
- Lanzar el hilo de escucha de teclado en segundo plano
- Ejecutar el bucle principal de ciclos de trabajo/descanso

## `src/config.py`
Define la clase `Config` con todos los parámetros configurables de la sesión.

## `src/logic.py`
Contiene la clase `PomodoroApp` con la lógica del temporizador (`countdown`) y la escucha de eventos de teclado (`listen_keys`).

## `src/utils/interface.py`
Utilidades de interfaz de usuario, incluyendo `clear_screen()` para limpiar la consola.

# Licencia

MIT