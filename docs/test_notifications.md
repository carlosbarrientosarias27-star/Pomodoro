# 🧪 Tests — `test_notifications.py`

Suite de pruebas para la función `play_beep` definida en `src/utils/notifications.py`, utilizando **pytest** y `monkeypatch`. Cubre el comportamiento en distintos sistemas operativos y el manejo de errores.

# Requisitos

```bash
pip install pytest
```

# Ejecución

```bash
# Ejecutar todos los tests
pytest test_notifications.py

# Con salida detallada
pytest test_notifications.py -v
```

---

# Estrategia de mocking

| Elemento mockeado      | Sustituto                          | Motivo                                                  |
|------------------------|------------------------------------|---------------------------------------------------------|
| `platform.system`      | `lambda: "Windows"` / `"Linux"`…  | Simular el SO sin depender del entorno real             |
| `sys.modules["winsound"]` | `MockWinsound` o `None`         | Simular presencia o ausencia del módulo Windows         |
| `capsys` (fixture)     | Captura de stdout                  | Verificar que se escribe `'\a'` o el mensaje de error   |

---

# Casos de prueba

### ✅ Casos Normales (N)

## `test_play_beep_windows_calls_winsound`
Verifica que en Windows se invoca `winsound.Beep` con los parámetros correctos (1000 Hz, 500 ms).

- **Mock de SO:** `"Windows"`
- **Mock de módulo:** clase `MockWinsound` inyectada en `sys.modules`
- **Aserción:**
  ```python
  assert sys.modules["winsound"].called is True
  ```

---

## `test_play_beep_linux_writes_bell_character`
Verifica que en Linux se escribe el carácter de campana `'\a'` en stdout.

- **Mock de SO:** `"Linux"`
- **Aserción:**
  ```python
  assert "\a" in captured.out
  ```

---

### ⚠️ Casos Límite (L)

## `test_play_beep_macos_behavior`
Verifica que macOS (`"Darwin"`) sigue la misma rama que Linux, emitiendo `'\a'` en stdout.

- **Mock de SO:** `"Darwin"`
- **Aserción:**
  ```python
  assert "\a" in captured.out
  ```

---

### 🔴 Casos de Error y Edge Cases (E)

## `test_play_beep_handles_exception_gracefully`
Verifica que si `winsound` no está disponible (`None` en `sys.modules`), la función captura la excepción y muestra el mensaje de fallback en consola sin interrumpir la ejecución.

- **Mock de SO:** `"Windows"`
- **Mock de módulo:** `sys.modules["winsound"] = None`
- **Aserción:**
  ```python
  assert "[Nota: No se pudo reproducir el sonido]" in captured.out
  ```

---

## `test_play_beep_with_unknown_os_defaults_to_bell`
Verifica que ante un SO desconocido, la función cae en la rama por defecto y emite `'\a'`.

- **Mock de SO:** `"UnknownOS"`
- **Aserción:**
  ```python
  assert "\a" in captured.out
  ```

---

# Resumen de cobertura

| Test                                          | Categoría | Qué valida                                              |
|-----------------------------------------------|-----------|---------------------------------------------------------|
| `test_play_beep_windows_calls_winsound`       | Normal    | `winsound.Beep` se invoca en Windows                    |
| `test_play_beep_linux_writes_bell_character`  | Normal    | `'\a'` se escribe en stdout en Linux                    |
| `test_play_beep_macos_behavior`               | Límite    | macOS sigue la misma rama que Linux                     |
| `test_play_beep_handles_exception_gracefully` | Error     | `winsound` no disponible muestra mensaje de fallback    |
| `test_play_beep_with_unknown_os_defaults_to_bell` | Error | SO desconocido emite `'\a'` por defecto                |