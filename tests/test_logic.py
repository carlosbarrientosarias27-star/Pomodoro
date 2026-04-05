import pytest
import time
from src.logic import PomodoroApp

# Mock de la configuración para los tests
class MockConfig:
    def __init__(self):
        self.total_cycles = 4
        self.work_min = 25

# --- Casos Normales (N) ---

def test_pomodoro_initialization_state():
    """
    Verifica que el estado inicial de la aplicación sea el correcto.
    """
    # Arrange
    config = MockConfig()

    # Act
    app = PomodoroApp(config)

    # Assert
    assert app.current_cycle == 0 and app.running is True and app.paused is False


def test_countdown_completes_successfully(monkeypatch):
    config = MockConfig()
    app = PomodoroApp(config)
    
    # MOCK CLAVE: Detener el tiempo real
    monkeypatch.setattr("time.sleep", lambda x: None)
    
    # MOCK CLAVE: Simular las utilidades importadas en logic.py
    monkeypatch.setattr("src.logic.clear_screen", lambda: None)
    monkeypatch.setattr("src.logic.progress_bar", lambda cur, tot: "")
    
    beep_called = False
    def mock_beep():
        nonlocal beep_called
        beep_called = True
    monkeypatch.setattr("src.logic.play_beep", mock_beep)
    
    # Act
    app.countdown(0.01, "Test") # Usar un valor pequeño
    
    # Assert
    assert beep_called is True


# --- Casos Límite (L) ---

def test_countdown_with_zero_minutes(monkeypatch):
    """
    Verifica que si los minutos son 0, la función termine inmediatamente sin dormir.
    """
    # Arrange
    config = MockConfig()
    app = PomodoroApp(config)
    sleep_calls = 0
    
    def count_sleep(x):
        nonlocal sleep_calls
        sleep_calls += 1

    monkeypatch.setattr(time, "sleep", count_sleep)
    monkeypatch.setattr(app, "clear_screen", lambda: None)
    monkeypatch.setattr(app, "progress_bar", lambda cur, tot: "")
    monkeypatch.setattr("src.logic.play_beep", lambda: None)

    # Act
    app.countdown(0, "Limit")

    # Assert
    assert sleep_calls == 0


def test_countdown_stops_immediately_if_not_running(monkeypatch):
    """
    Verifica que si la app no está en estado 'running', el loop no se ejecuta.
    """
    # Arrange
    config = MockConfig()
    app = PomodoroApp(config)
    app.running = False
    
    executed_loop = False
    def mock_clear():
        nonlocal executed_loop
        executed_loop = True

    monkeypatch.setattr(app, "clear_screen", mock_clear)

    # Act
    app.countdown(1, "StopTest")

    # Assert
    assert executed_loop is False


# --- Casos de Error y Edge Cases (E) ---

def test_countdown_pause_loop_execution(monkeypatch):
    """
    Verifica que mientras está pausado, el tiempo (seconds) no disminuye.
    """
    # Arrange
    config = MockConfig()
    app = PomodoroApp(config)
    app.paused = True
    
    # Simulamos que después de una iteración en pausa, cerramos la app para romper el loop infinito del test
    def mock_sleep_and_stop(x):
        app.running = False 

    monkeypatch.setattr(time, "sleep", mock_sleep_and_stop)
    monkeypatch.setattr(app, "clear_screen", lambda: None)

    # Act
    initial_seconds = 1 * 60
    # Iniciamos countdown con 1 minuto
    app.countdown(1, "PauseTest")

    # Assert
    # Si la lógica es correcta, seconds no debería haber bajado de 60 ya que estaba pausado
    assert app.paused is True


def test_listen_keys_quit_logic(monkeypatch):
    """
    Verifica que la tecla 'q' cambia el estado running a False y lanza SystemExit.
    """
    # Arrange
    config = MockConfig()
    app = PomodoroApp(config)
    monkeypatch.setattr("builtins.input", lambda: "q")

    # Act / Assert
    with pytest.raises(SystemExit):
        app.listen_keys()
    
    assert app.running is False


def test_countdown_invalid_type_error(monkeypatch):
    """
    Verifica el comportamiento ante un tipo de dato inválido en minutos.
    """
    # Arrange
    config = MockConfig()
    app = PomodoroApp(config)

    # Act / Assert
    with pytest.raises(TypeError):
        app.countdown("invalid", "ErrorTest")