# 🍅 Pomodoro

> Aplicación de gestión del tiempo basada en la técnica Pomodoro, con asistencia de inteligencia artificial y sistema de notificaciones integrado.

---

# 📋 Descripción

**Pomodoro** es una herramienta de productividad que implementa la famosa [técnica Pomodoro](https://es.wikipedia.org/wiki/T%C3%A9cnica_Pomodoro) para ayudarte a gestionar el tiempo de trabajo de forma eficiente. Combina un temporizador configurable con notificaciones inteligentes y un módulo de asistencia por IA que potencia tu flujo de trabajo.

---

# 🗂️ Estructura del Proyecto

```
POMODORO/
├── .github/
│   └── workflows/
│       └── pipeline.yml          # CI/CD con GitHub Actions
├── docs/
│   └── asistencia_ia.md          # Documentación del módulo de IA
├── src/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── interface.py          # Interfaz de usuario
│   │   └── notifications.py     # Sistema de notificaciones
│   ├── __init__.py
│   ├── config.py                 # Configuración de la aplicación
│   ├── logic.py                  # Lógica principal del temporizador
│   └── main.py                   # Punto de entrada de la aplicación
├── tests/
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── test_interface.py
│   │   └── test_notifications.py
│   ├── __init__.py
│   ├── test_config.py
│   ├── test_logic.py
│   ├── test_main.py
│   └── conftest.py               # Fixtures de pytest
├── LICENSE
├── pytest.ini                    # Configuración de tests
├── README.md
├── requirements.txt              # Dependencias del proyecto
└── run.py                        # Script de arranque
```

---

# ✨ Características

- ⏱️ **Temporizador Pomodoro** — Ciclos de trabajo y descanso configurables
- 🔔 **Notificaciones** — Alertas al finalizar cada sesión o descanso
- 🤖 **Asistencia con IA** — Módulo inteligente para optimizar tu productividad
- ⚙️ **Configurable** — Ajusta tiempos y preferencias desde `config.py`
- ✅ **Testeado** — Suite completa de tests unitarios con pytest
- 🚀 **CI/CD** — Pipeline automatizado con GitHub Actions

---

# 🚀 Instalación

## Requisitos previos

- Python 3.8 o superior
- pip

## Pasos

```bash
# 1. Clona el repositorio
git clone https://github.com/tu-usuario/pomodoro.git
cd pomodoro

# 2. Crea y activa un entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Instala las dependencias
pip install -r requirements.txt
```

---

# ▶️ Uso

```bash
# Ejecutar la aplicación
python run.py

# O directamente desde el módulo principal
python src/main.py
```

---

# 🧪 Tests

```bash
# Ejecutar todos los tests
pytest

# Con reporte de cobertura
pytest --cov=src tests/

# Tests de un módulo específico
pytest tests/test_logic.py -v
```

---

# ⚙️ Configuración

Edita `src/config.py` para personalizar la aplicación:

| Parámetro | Descripción | Valor por defecto |
|---|---|---|
| `WORK_DURATION` | Duración del ciclo de trabajo (min) | `25` |
| `SHORT_BREAK` | Duración del descanso corto (min) | `5` |
| `LONG_BREAK` | Duración del descanso largo (min) | `15` |
| `CYCLES_BEFORE_LONG_BREAK` | Ciclos antes del descanso largo | `4` |

---

# 🤖 Asistencia IA

El proyecto incluye un módulo de inteligencia artificial documentado en [`docs/asistencia_ia.md`](docs/asistencia_ia.md). Este módulo analiza tus patrones de trabajo y puede sugerir ajustes en los ciclos para maximizar tu rendimiento.

---

# 🔄 CI/CD

El proyecto utiliza **GitHub Actions** para automatizar:

- Ejecución de tests en cada *push* y *pull request*
- Validación de estilo de código
- Generación de reportes de cobertura

Consulta [`.github/workflows/pipeline.yml`](.github/workflows/pipeline.yml) para más detalles.

---

# 📄 Licencia

Este proyecto está bajo la licencia descrita en el archivo [LICENSE](LICENSE MIT).

---

# 🙌 Contribuciones

¡Las contribuciones son bienvenidas! Por favor, abre un *issue* o envía un *pull request*.

1. Haz un fork del proyecto
2. Crea tu rama de feature (`git checkout -b feature/nueva-funcionalidad`)
3. Haz commit de tus cambios (`git commit -m 'Add: nueva funcionalidad'`)
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---