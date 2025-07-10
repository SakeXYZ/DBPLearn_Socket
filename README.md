
---

### English Version (README-en.md)
```markdown
# Simple Chat Application

## Features
- Multi-client chat server
- Real-time messaging
- Thread-based architecture
- Simple commands (`/quit` to exit)

## Quick Start
1. Run the server:
   ```bash
   python server.py
   ```
2. Connect clients:
   ```bash
   python client.py
   ```

## Configuration
Edit these variables in the code:
```python
HOST = '0.0.0.0'  # Server IP
PORT = 12345      # Server port
```

[View in Russian](/README-ru.md) | [Смотреть на русском](/README-ru.md)
```

---

### Russian Version (README-ru.md)
```markdown
# Простое чат-приложение

## Возможности
- Многопользовательский сервер
- Обмен сообщениями в реальном времени
- Потоковая архитектура
- Простые команды (`/quit` для выхода)

## Быстрый старт
1. Запустите сервер:
   ```bash
   python server.py
   ```
2. Подключите клиенты:
   ```bash
   python client.py
   ```

## Настройка
Измените переменные в коде:
```python
HOST = '0.0.0.0'  # IP сервера
PORT = 12345      # Порт сервера
```

[View in English](/README-en.md) | [Читать по-английски](/README-en.md)
```

---

### Implementation notes:
1. Place both files in your project root
2. The links will work if:
   - Files are hosted on GitHub/GitLab
   - Or served via web server with proper routing
3. For local use, you can create a simple HTML switcher:

```html
<!-- language-switcher.html -->
<div style="text-align: center; margin: 20px;">
  <a href="README-en.md">English</a> | 
  <a href="README-ru.md">Русский</a>
</div>
```

This approach keeps the documentation cleanly separated while providing clear navigation between language versions.
