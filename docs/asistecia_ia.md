# 🍅 Pomodoro — Prompts de IA utilizados

Este documento recoge los **prompts principales** empleados durante el desarrollo del proyecto Pomodoro con asistencia de IA (`docs/asistecia_ia.md`).

---

# 📁 Estructura del proyecto

```
POMODORO/
├── .github/workflows/pipeline.yml
├── docs/asistecia_ia.md
├── src/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── interface.py
│   │   └── notifications.py
│   ├── __init__.py
│   ├── config.py
│   ├── logic.py
│   └── main.py
├── tests/
│   ├── utils/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_logic.py
│   └── test_main.py
├── conftest.py
├── run.py
├── requirements.txt
├── pytest.ini
└── README.md
```

---

# 🤖 Prompts utilizados en el desarrollo

## 1. Configuración inicial del proyecto (`config.py`)

```
Crea un archivo de configuración en Python para una aplicación Pomodoro.
Debe incluir constantes para:
- Duración del pomodoro (25 minutos por defecto)
- Duración del descanso corto (5 minutos)
- Duración del descanso largo (15 minutos)
- Número de pomodoros antes del descanso largo (4)
Usa variables de entorno con valores por defecto si no están definidas.
```

---

## 2. Lógica del temporizador (`logic.py`)

```
Implementa la lógica principal de un temporizador Pomodoro en Python.
Debe incluir:
- Una clase PomodoroTimer con métodos start(), pause(), reset() y skip()
- Control del estado actual: pomodoro, descanso corto o descanso largo
- Contador de ciclos completados
- Callbacks para notificar cambios de estado
El código debe ser testeable de forma unitaria y no depender de la UI.
```

---

## 3. Interfaz de usuario (`src/utils/interface.py`)

```
Crea una interfaz de línea de comandos (CLI) para el temporizador Pomodoro.
Debe mostrar:
- El tiempo restante en formato MM:SS
- El estado actual (Pomodoro / Descanso corto / Descanso largo)
- El número de pomodoros completados
Incluye controles de teclado para iniciar, pausar y saltar al siguiente ciclo.
Usa la librería 'rich' o similar para mejorar la visualización en terminal.
```

---

## 4. Sistema de notificaciones (`src/utils/notifications.py`)

```
Implementa un sistema de notificaciones de escritorio para Python que sea
compatible con Windows, macOS y Linux.
Cuando termine un ciclo Pomodoro o un descanso, debe:
- Mostrar una notificación nativa del sistema operativo
- Incluir un sonido de alerta opcional
- Indicar en el mensaje qué tipo de sesión comienza a continuación
```

---

## 5. Punto de entrada principal (`main.py` y `run.py`)

```
Crea el punto de entrada principal de la aplicación Pomodoro.
El archivo main.py debe:
- Inicializar la configuración
- Instanciar el temporizador y la interfaz
- Conectar la lógica con las notificaciones
- Manejar señales del sistema (Ctrl+C) de forma elegante

Además, crea un run.py en la raíz del proyecto que sirva como
script de arranque rápido.
```

---

## 6. Tests unitarios (`tests/`)

```
Genera tests unitarios con pytest para los siguientes módulos del proyecto Pomodoro:

1. test_config.py: verifica que los valores de configuración son correctos
   y que se leen bien desde variables de entorno.

2. test_logic.py: prueba los métodos start(), pause(), reset() y skip()
   de la clase PomodoroTimer. Incluye casos para transiciones de estado
   y conteo de ciclos.

3. test_main.py: verifica la inicialización y el flujo principal
   de la aplicación usando mocks para la interfaz y las notificaciones.

Usa fixtures en conftest.py para la configuración compartida entre tests.
```

---

## 7. Pipeline de CI/CD (`.github/workflows/pipeline.yml`)

```
Crea un workflow de GitHub Actions para el proyecto Pomodoro que:
- Se ejecute en cada push y pull request a la rama main
- Configure Python 3.10
- Instale las dependencias desde requirements.txt
- Ejecute los tests con pytest y genere un reporte de cobertura
- Falle el pipeline si la cobertura cae por debajo del 80%
```

---

## 8. Documentación de asistencia IA (`docs/asistecia_ia.md`)

```
Genera un documento Markdown que registre el uso de IA durante el desarrollo
de este proyecto. Incluye:
- Qué partes del código fueron generadas o asistidas por IA
- Los prompts más relevantes utilizados
- Las decisiones de diseño tomadas con ayuda de IA
- Lecciones aprendidas sobre el uso de IA como herramienta de desarrollo
```

---

# 🛠️ Tecnologías y dependencias

| Paquete | Uso |
|---|---|
| `pytest` | Framework de testing |
| `pytest-cov` | Cobertura de tests |
| `rich` | Interfaz visual en terminal |
| `plyer` / `playsound` | Notificaciones del sistema |

---

# 🚀 Cómo ejecutar el proyecto

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
python run.py

# Ejecutar los tests
pytest --cov=src tests/
```

---

# 📝 Notas sobre el uso de IA

Los prompts listados en este documento fueron utilizados con modelos de lenguaje (LLM) para acelerar el desarrollo. Todo el código generado fue revisado, adaptado y testeado manualmente antes de integrarse al proyecto.

> Ver también: [`docs/asistecia_ia.md`](docs/asistecia_ia.md) para el registro completo de asistencia IA.