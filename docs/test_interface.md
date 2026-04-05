# 🧪 Tests — `test_interface.py`

Suite de pruebas para las funciones `clear_screen` y `progress_bar` definidas en `src/utils/interface.py`, utilizando **pytest** y `monkeypatch`.

# Requisitos

```bash
pip install pytest
```

# Ejecución

```bash
# Ejecutar todos los tests
pytest test_interface.py

# Con salida detallada
pytest test_interface.py -v
```

---

# Estrategia de mocking

Los tests de `clear_screen` parchean `platform.system` y `subprocess.run` para simular distintos sistemas operativos sin ejecutar comandos reales en la consola:

| Elemento mockeado   | Sustituto                         | Motivo                                          |
|---------------------|-----------------------------------|-------------------------------------------------|
| `platform.system`   | `lambda: "Windows"` / `"Linux"`  | Simular el SO sin depender del entorno real     |
| `subprocess.run`    | Función que captura argumentos    | Verificar el comando ejecutado sin efectos reales |

---

# Casos de prueba

### ✅ Casos Normales (N)

## `test_clear_screen_windows_calls_cls`
Verifica que en Windows, `clear_screen()` invoca `subprocess.run` con el comando `["cls"]`.

- **Mock de SO:** `"Windows"`
- **Aserción:**
  ```python
  assert captured_args[0] == ["cls"]
  ```

---

## `test_progress_bar_at_half_capacity`
Verifica que al 50% de progreso la barra muestre exactamente la mitad de bloques y el texto `50%`.

- **Entradas:** `current=50`, `total=100`, `length=20`
- **Aserción:**
  ```python
  assert result == f"[{'█' * 10}{' ' * 10}] 50%"
  ```

---

### ⚠️ Casos Límite (L)

## `test_progress_bar_at_zero_percent`
Verifica que con `current=0` la barra se muestre completamente vacía con `0%`.

- **Entradas:** `current=0`, `total=100`, `length=10`
- **Aserción:**
  ```python
  assert result == f"[{' ' * 10}] 0%"
  ```

---

## `test_progress_bar_at_one_hundred_percent`
Verifica que con `current=total` la barra se muestre completamente llena con `100%`.

- **Entradas:** `current=100`, `total=100`, `length=10`
- **Aserción:**
  ```python
  assert result == f"[{'█' * 10}] 100%"
  ```

---

## `test_clear_screen_linux_calls_clear`
Verifica que en Linux, `clear_screen()` invoca `subprocess.run` con el comando `["clear"]`.

- **Mock de SO:** `"Linux"`
- **Aserción:**
  ```python
  assert captured_args[0] == ["clear"]
  ```

---

### 🔴 Casos de Error y Edge Cases (E)

## `test_progress_bar_division_by_zero`
Verifica que cuando `total=0` la función no lanza excepción y devuelve una barra con `0%`.

- **Entradas:** `current=10`, `total=0`
- **Aserción:**
  ```python
  assert "0%" in result
  ```

---

## `test_progress_bar_with_string_input`
Verifica que pasar un `str` no numérico como `current` lanza `ValueError`.

- **Entradas:** `current="texto_no_valido"`, `total=10`
- **Aserción:**
  ```python
  with pytest.raises(ValueError):
      progress_bar(current, total)
  ```

---

## `test_progress_bar_current_greater_than_total`
Verifica que cuando `current` supera a `total`, el porcentaje se limita a `100%` sin desbordar la barra.

- **Entradas:** `current=120`, `total=100`, `length=10`
- **Aserción:**
  ```python
  assert "100%" in result
  ```

---

# Resumen de cobertura

| Test                                        | Función        | Categoría | Qué valida                                          |
|---------------------------------------------|----------------|-----------|-----------------------------------------------------|
| `test_clear_screen_windows_calls_cls`       | `clear_screen` | Normal    | Comando `cls` en Windows                            |
| `test_progress_bar_at_half_capacity`        | `progress_bar` | Normal    | Barra al 50% con bloques y texto correctos          |
| `test_progress_bar_at_zero_percent`         | `progress_bar` | Límite    | Barra vacía al 0%                                   |
| `test_progress_bar_at_one_hundred_percent`  | `progress_bar` | Límite    | Barra llena al 100%                                 |
| `test_clear_screen_linux_calls_clear`       | `clear_screen` | Límite    | Comando `clear` en Linux                            |
| `test_progress_bar_division_by_zero`        | `progress_bar` | Error     | `total=0` devuelve `0%` sin excepción               |
| `test_progress_bar_with_string_input`       | `progress_bar` | Error     | `str` no numérico lanza `ValueError`                |
| `test_progress_bar_current_greater_than_total` | `progress_bar` | Error  | `current > total` se limita a `100%`                |