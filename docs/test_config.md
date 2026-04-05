# 🧪 Tests — `test_config.py`

Suite de pruebas para la clase `Config` definida en `src/config.py`, utilizando **pytest**. Cubre la inicialización de valores por defecto y el método de validación `validate_positive`.

# Requisitos

```bash
pip install pytest
```

# Ejecución

```bash
# Ejecutar todos los tests
pytest test_config.py

# Con salida detallada
pytest test_config.py -v
```

---

# Casos de prueba

### ✅ Casos Normales (N)

## `test_config_initialization_defaults`
Verifica que al instanciar `Config()` sin argumentos, todos los atributos tomen sus valores por defecto.

- **Aserción:**
  ```python
  assert (work_min, short_break_min, long_break_min, total_cycles) == (25, 5, 15, 4)
  ```

---

## `test_validate_positive_with_standard_integer`
Verifica que un entero positivo estándar sea considerado válido.

- **Entrada:** `val = 10`
- **Aserción:**
  ```python
  assert result is True
  ```

---

### ⚠️ Casos Límite (L)

## `test_validate_positive_boundary_one`
Verifica que el valor mínimo entero positivo (`1`) sea aceptado.

- **Entrada:** `val = 1`
- **Aserción:**
  ```python
  assert result is True
  ```

---

## `test_validate_positive_boundary_zero`
Verifica que el valor `0` sea rechazado, ya que el límite es estrictamente mayor que cero.

- **Entrada:** `val = 0`
- **Aserción:**
  ```python
  assert result is False
  ```

---

## `test_validate_positive_with_small_float`
Verifica que un valor flotante muy pequeño pero mayor a cero (`0.00001`) sea considerado válido.

- **Entrada:** `val = 0.00001`
- **Aserción:**
  ```python
  assert result is True
  ```

---

### 🔴 Casos de Error y Edge Cases (E)

## `test_validate_positive_negative_integer`
Verifica que un número negativo sea rechazado.

- **Entrada:** `val = -5`
- **Aserción:**
  ```python
  assert result is False
  ```

---

## `test_validate_positive_with_string_raises_error`
Verifica que pasar un `str` en lugar de un número lance `TypeError`.

- **Entrada:** `val = "25"`
- **Aserción:**
  ```python
  with pytest.raises(TypeError):
      config.validate_positive(val)
  ```

---

## `test_validate_positive_with_none_raises_error`
Verifica que pasar `None` lance `TypeError`.

- **Entrada:** `val = None`
- **Aserción:**
  ```python
  with pytest.raises(TypeError):
      config.validate_positive(val)
  ```

---

# Resumen de cobertura

| Test                                          | Categoría | Qué valida                                            |
|-----------------------------------------------|-----------|-------------------------------------------------------|
| `test_config_initialization_defaults`         | Normal    | Valores por defecto correctos al instanciar `Config`  |
| `test_validate_positive_with_standard_integer`| Normal    | Entero positivo devuelve `True`                       |
| `test_validate_positive_boundary_one`         | Límite    | Valor mínimo positivo (`1`) devuelve `True`           |
| `test_validate_positive_boundary_zero`        | Límite    | Valor `0` devuelve `False`                            |
| `test_validate_positive_with_small_float`     | Límite    | Float muy pequeño positivo devuelve `True`            |
| `test_validate_positive_negative_integer`     | Error     | Número negativo devuelve `False`                      |
| `test_validate_positive_with_string_raises_error` | Error | `str` lanza `TypeError`                              |
| `test_validate_positive_with_none_raises_error`   | Error | `None` lanza `TypeError`                             |