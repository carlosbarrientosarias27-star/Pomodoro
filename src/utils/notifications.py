import platform
import sys


def play_beep():
    """Emite un sonido de notificación según el SO (Commit 6)."""
    system = platform.system()
    try:
        if system == "Windows":
            import winsound
            winsound.Beep(1000, 500)
        else:
            # Para Linux/Mac requiere usualmente 'beep' o usar el carácter de campana
            sys.stdout.write('\a')
            sys.stdout.flush()
    except Exception:
        print("\n[Nota: No se pudo reproducir el sonido]")
