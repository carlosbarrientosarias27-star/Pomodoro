import os
import platform
import logging

# Configuramos un logger básico para evitar el 'pass' silencioso
logger = logging.getLogger(__name__)


def clear_screen(*args):
    sys_platform = platform.system()
    try:
        if sys_platform == "Windows":
            # Ruta absoluta típica de CMD en Windows
            os.system('C:\\Windows\\System32\\cls.exe')  # nosec B605 B607
        else:
            # Ruta absoluta típica en Linux/Mac
            os.system('/usr/bin/clear')  # nosec B605 B607
    except Exception as e:
        logger.debug(f"No se pudo limpiar la pantalla: {e}")


def progress_bar(current, total, length=30):
    """Genera una barra de progreso visual sin 'self'."""
    if total <= 0:
        return f"[{' ' * length}] 0%"

    # Aseguramos que current no sea None y sea un número
    current_val = current if current is not None else 0

    percent = float(current_val) / total
    # Limitamos el porcentaje entre 0 y 1 para evitar errores visuales
    percent = max(0.0, min(1.0, percent))

    arrow = '█' * int(round(percent * length))
    spaces = ' ' * (length - len(arrow))
    return f"[{arrow}{spaces}] {int(percent * 100)}%"
