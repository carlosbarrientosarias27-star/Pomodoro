import pytest
import sys
import platform
from src.utils.notifications import play_beep

# --- Casos Normales (N) ---

def test_play_beep_windows_calls_winsound(monkeypatch):
    """
    Verifica que en Windows se intente importar y ejecutar winsound.Beep.
    """
    # Arrange
    class MockWinsound:
        def Beep(self, freq, dur):
            self.called = True
            self.params = (freq, dur)

    mock_ws = MockWinsound()
    monkeypatch.setattr(platform, "system", lambda: "Windows")
    # Simulamos la existencia del módulo winsound en el sys.modules
    monkeypatch.setitem(sys.modules, "winsound", mock_ws)

    # Act
    play_beep()

    # Assert
    assert sys.modules["winsound"].called is True


def test_play_beep_linux_writes_bell_character(monkeypatch, capsys):
    """
    Verifica que en sistemas no-Windows (Linux/Mac) se envíe el carácter \a a stdout.
    """
    # Arrange
    monkeypatch.setattr(platform, "system", lambda: "Linux")

    # Act
    play_beep()
    captured = capsys.readouterr()

    # Assert
    assert "\a" in captured.out


# --- Casos Límite (L) ---

def test_play_beep_macos_behavior(monkeypatch, capsys):
    """
    Verifica que Darwin (macOS) se trate bajo la misma lógica de carácter de campana que Linux.
    """
    # Arrange
    monkeypatch.setattr(platform, "system", lambda: "Darwin")

    # Act
    play_beep()
    captured = capsys.readouterr()

    # Assert
    assert "\a" in captured.out


# --- Casos de Error y Edge Cases (E) ---

def test_play_beep_handles_exception_gracefully(monkeypatch, capsys):
    # Arrange
    monkeypatch.setattr(platform, "system", lambda: "Windows")
    # Simulate winsound not being available in the system
    monkeypatch.setitem(sys.modules, "winsound", None) 

    # Act
    play_beep()
    captured = capsys.readouterr()

    # Assert
    assert "[Nota: No se pudo reproducir el sonido]" in captured.out


def test_play_beep_with_unknown_os_defaults_to_bell(monkeypatch, capsys):
    """
    Verifica que ante un SO desconocido, el sistema intente usar el carácter de campana por defecto.
    """
    # Arrange
    monkeypatch.setattr(platform, "system", lambda: "UnknownOS")

    # Act
    play_beep()
    captured = capsys.readouterr()

    # Assert
    assert "\a" in captured.out