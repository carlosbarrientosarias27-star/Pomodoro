import time
import threading
from src.config import Config
from src.logic import PomodoroApp
from src.utils.interface import clear_screen


def start_app():
    """Configura e inicia el ciclo de vida de la aplicación."""
    config = Config()
    app = PomodoroApp(config)

    clear_screen()
    print("--- BIENVENIDO AL POMODORO TIMER ---")

    # 1. Configuración de usuario
    try:
        app.config.work_min = int(input("Minutos de trabajo (default 25): ") or 25)
        short_prompt = "Minutos de descanso corto (default 5): "
        app.config.short_break_min = int(input(short_prompt) or 5)
        app.config.total_cycles = int(input("Total de ciclos (default 4): ") or 4)
    except ValueError:
        print("\nEntrada no válida, usando valores por defecto...")
        time.sleep(1)

    # 2. Iniciar hilo de escucha de teclado en segundo plano
    threading.Thread(target=app.listen_keys, daemon=True).start()

    # 3. Bucle principal de la sesión
    try:
        while app.current_cycle < app.config.total_cycles and app.running:
            # Fase de Trabajo
            app.countdown(app.config.work_min, "TRABAJO")
            app.current_cycle += 1

            # Verificar si corresponde descanso
            if app.current_cycle < app.config.total_cycles and app.running:
                if app.current_cycle % 4 == 0:
                    app.countdown(app.config.long_break_min, "DESCANSO LARGO")
                else:
                    app.countdown(app.config.short_break_min, "DESCANSO CORTO")

        if app.running:
            clear_screen()
            print("\n¡Felicidades! Has completado todas tus sesiones.")

    except KeyboardInterrupt:
        print("\n\nPrograma interrumpido por el usuario. ¡Hasta luego!")
        app.running = False
