import platform
import subprocess

def clear_screen():
    sys_platform = platform.system()
    command = "cls" if sys_platform == "Windows" else "clear"
    # shell=True is needed for built-in shell commands like cls/clear
    subprocess.run(command, shell=True)

def progress_bar(current, total, length=30):
    if total <= 0:
        return f"[{' ' * length}] 0%"
    
    # Intentar convertir a float lanzará ValueError si es una cadena no numérica
    # Esto hará que test_progress_bar_with_string_input pase.
    percent = float(current) / total 
    
    display_percent = min(100, int(percent * 100))
    bar_percent = max(0.0, min(1.0, percent))
    
    arrow = '█' * int(round(bar_percent * length))
    spaces = ' ' * (length - len(arrow))
    
    return f"[{arrow}{spaces}] {display_percent}%"
