import time
import sys
from src.utils.notifications import play_beep
from src.utils.interface import clear_screen, progress_bar


class PomodoroApp:
    def __init__(self, config):
        self.config = config
        self.current_cycle = 0
        self.paused = False
        self.running = True

    def countdown(self, minutes, label):
        if not isinstance(minutes, (int, float)):
            raise TypeError("Los minutos deben ser un número")

        seconds = int(minutes * 60)
        total_seconds = seconds

        while seconds > 0 and self.running:
            if not self.paused:
                mins, secs = divmod(seconds, 60)
                clear_screen()
                print(f"=== MODO: {label} ===")
                print(f"Ciclo: {self.current_cycle + 1}/{self.config.total_cycles}")
                print(f"\nTiempo restante: {mins:02d}:{secs:02d}")
                print(progress_bar(total_seconds - seconds, total_seconds))

                time.sleep(1)
                seconds -= 1
            else:
                clear_screen()
                print(f"=== MODO: {label} (PAUSADO) ===")
                time.sleep(0.5)

        if self.running and seconds <= 0:
            play_beep()

    def listen_keys(self):
        while self.running:
            try:
                cmd = input().lower()
                if cmd == 'p':
                    self.paused = not self.paused
                elif cmd == 'q':
                    self.running = False
                    sys.exit(0)
            except EOFError:
                break
