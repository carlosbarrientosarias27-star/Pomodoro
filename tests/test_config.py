import pytest
from src.config import Config

# --- Casos Normales (N) ---

def test_config_initialization_defaults():
    """
    Verifica que los valores por defecto se carguen correctamente al instanciar.
    """
    # Arrange
    config = Config()

    # Act
    work_time = config.work_min
    short_break = config.short_break_min
    long_break = config.long_break_min
    cycles = config.total_cycles

    # Assert
    assert (work_time, short_break, long_break, cycles) == (25, 5, 15, 4)

def test_validate_positive_with_standard_integer():
    """
    Verifica que un entero positivo estándar devuelva True.
    """
    # Arrange
    config = Config()
    val = 10

    # Act
    result = config.validate_positive(val)

    # Assert
    assert result is True

# --- Casos Límite (L) ---

def test_validate_positive_boundary_one():
    """
    Verifica que el valor mínimo entero positivo (1) devuelva True.
    """
    # Arrange
    config = Config()
    val = 1

    # Act
    result = config.validate_positive(val)

    # Assert
    assert result is True

def test_validate_positive_boundary_zero():
    """
    Verifica que el valor cero devuelva False (limite no incluido).
    """
    # Arrange
    config = Config()
    val = 0

    # Act
    result = config.validate_positive(val)

    # Assert
    assert result is False

def test_validate_positive_with_small_float():
    """
    Verifica que un valor flotante muy pequeño pero mayor a cero sea válido.
    """
    # Arrange
    config = Config()
    val = 0.00001

    # Act
    result = config.validate_positive(val)

    # Assert
    assert result is True

# --- Casos de Error y Edge Cases (E) ---

def test_validate_positive_negative_integer():
    """
    Verifica que un número negativo devuelva False.
    """
    # Arrange
    config = Config()
    val = -5

    # Act
    result = config.validate_positive(val)

    # Assert
    assert result is False

def test_validate_positive_with_string_raises_error():
    """
    Verifica que el paso de un tipo no numérico (string) lance una excepción.
    """
    # Arrange
    config = Config()
    val = "25"

    # Act / Assert
    with pytest.raises(TypeError):
        config.validate_positive(val)

def test_validate_positive_with_none_raises_error():
    """
    Verifica que el paso de None lance una excepción de tipo.
    """
    # Arrange
    config = Config()
    val = None

    # Act / Assert
    with pytest.raises(TypeError):
        config.validate_positive(val)