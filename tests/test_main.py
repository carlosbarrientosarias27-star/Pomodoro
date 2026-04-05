import pytest
import threading
import time
from src.main import start_app
from src.logic import PomodoroApp

# --- Casos Normales (N) ---

def test_start_app_initialization_flow(monkeypatch):
    # Simular entradas rápidas
    inputs = iter(["", "", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    # Forzar que sleep no espere NADA
    monkeypatch.setattr("time.sleep", lambda x: None)
    monkeypatch.setattr("src.main.clear_screen", lambda: None)
    
    # Mockear el hilo para que no se ejecute en paralelo realmente
    monkeypatch.setattr("threading.Thread", lambda target, daemon: type('Thread', (), {'start': lambda self: None})())

    def mock_countdown(self, minutes, label):
        self.running = False # Detener el loop de ciclos inmediatamente
    
    monkeypatch.setattr(PomodoroApp, "countdown", mock_countdown)

    # Act
    start_app() 
    # Si llega aquí sin esperar segundos reales, el test es exitoso


def test_start_app_custom_values_assignment(monkeypatch):
    inputs = iter(["10", "2", "1"]) 
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("src.utils.interface.clear_screen", lambda: None)
    
    captured_config = {}
    def mock_countdown(self, minutes, label):
        captured_config['work'] = self.config.work_min
        self.running = False

    monkeypatch.setattr(PomodoroApp, "countdown", mock_countdown)
    monkeypatch.setattr(threading.Thread, "start", lambda x: None)

    start_app()
    assert captured_config['work'] == 10


# --- Casos Límite (L) ---

def test_start_app_completes_all_cycles(monkeypatch):
    inputs = iter(["1", "1", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr("src.utils.interface.clear_screen", lambda: None)
    
    # Usamos una lista para poder modificarla dentro del mock (mutable)
    stats = {"cycles": 0}
    
    def mock_countdown(self, minutes, label):
        stats["cycles"] += 1

    monkeypatch.setattr(PomodoroApp, "countdown", mock_countdown)
    monkeypatch.setattr(threading.Thread, "start", lambda x: None)

    start_app()

    # Debería ejecutarse 1 vez (Fase de trabajo).
    assert stats["cycles"] == 1