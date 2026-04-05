import pytest
import subprocess
import platform
from src.utils.interface import clear_screen, progress_bar

# --- Casos Normales (N) ---

def test_clear_screen_windows_calls_cls(monkeypatch):
    captured_args = []

    # 1. Mock the platform to return Windows
    monkeypatch.setattr(platform, "system", lambda: "Windows")

    # 2. Mock subprocess.run instead of os.system
    def mock_run(command, **kwargs):
        captured_args.append(command)
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr(subprocess, "run", mock_run)

    # 3. Call without arguments (matches your interface.py definition)
    clear_screen()

    # 4. Verify the command list contains "cls"
    assert captured_args[0] == ["cls"]


def test_progress_bar_at_half_capacity():
    """
    Verifica que al 50% la barra muestre la mitad de bloques y el texto '50%'.
    """
    # Arrange
    current = 50
    total = 100
    length = 20
    # 50% de 20 es 10 bloques

    # Act
    result = progress_bar(current, total, length)

    # Assert
    assert result == f"[{'█' * 10}{' ' * 10}] 50%"


# --- Casos Límite (L) ---

def test_progress_bar_at_zero_percent():
    """
    Verifica el estado inicial de la barra (0%).
    """
    # Arrange
    current = 0
    total = 100
    length = 10

    # Act
    result = progress_bar(current, total, length)

    # Assert
    assert result == f"[{' ' * 10}] 0%"


def test_progress_bar_at_one_hundred_percent():
    """
    Verifica el estado final de la barra (100%).
    """
    # Arrange
    current = 100
    total = 100
    length = 10

    # Act
    result = progress_bar(current, total, length)

    # Assert
    assert result == f"[{'█' * 10}] 100%"


def test_clear_screen_linux_calls_clear(monkeypatch):
    captured_args = []

    # 1. Mock the platform to return Linux
    monkeypatch.setattr(platform, "system", lambda: "Linux")

    # 2. Mock subprocess.run
    def mock_run(command, **kwargs):
        captured_args.append(command)
        return subprocess.CompletedProcess(command, 0)

    monkeypatch.setattr(subprocess, "run", mock_run)

    # 3. Call the function
    clear_screen()

    # 4. Verify the command list contains "clear"
    assert captured_args[0] == ["clear"]


# --- Casos de Error y Edge Cases (E) ---

def test_progress_bar_division_by_zero():
    # Instead of raises, check the "safe" output
    result = progress_bar(10, 0)
    assert "0%" in result


def test_progress_bar_with_string_input():
    current = "texto_no_valido"
    total = 10
    # float("texto_no_valido") lanza ValueError
    with pytest.raises(ValueError):
        progress_bar(current, total)


def test_progress_bar_current_greater_than_total():
    # If your code clamps, your test must expect 100%
    result = progress_bar(120, 100, 10)
    assert "100%" in result