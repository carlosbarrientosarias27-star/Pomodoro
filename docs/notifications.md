# 🔔 `notifications.py` — Notificaciones de sonido

Módulo encargado de emitir una señal sonora al finalizar cada fase del temporizador, con comportamiento adaptado al sistema operativo.

---

# Funciones

## `play_beep()`

Emite un pitido de notificación compatible con Windows, macOS y Linux.

```python
from src.utils.notifications import play_beep

play_beep()
```

**Comportamiento por sistema operativo:**

| Sistema operativo | Mecanismo                              | Detalle                        |
|-------------------|----------------------------------------|--------------------------------|
| Windows           | `winsound.Beep(1000, 500)`             | Tono de 1000 Hz durante 500 ms |
| macOS / Linux     | `sys.stdout.write('\a')`               | Carácter de campana (BEL)      |
| Cualquiera (fallo)| `print("[Nota: No se pudo reproducir el sonido]")` | Fallback silencioso |

> En Linux puede requerirse el paquete del sistema `beep` o que el terminal tenga habilitados los sonidos para que `'\a'` sea audible.

**Manejo de errores:** cualquier excepción durante la reproducción es capturada y sustituida por un mensaje en consola, sin interrumpir la ejecución de la aplicación.

---

# Dependencias

| Módulo     | Uso                                                  |
|------------|------------------------------------------------------|
| `platform` | Detectar el sistema operativo                        |
| `sys`      | Escribir el carácter de campana en stdout            |
| `winsound` | Reproducir el pitido en Windows (solo disponible en Windows) |