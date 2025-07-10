# 🚀 Simple Python Chat | Простой чат на Python  

### 🌟 Features | Возможности  
- 🖥️ **Multi-client chat server** (`server.py`) | **Многопользовательский сервер**  
- ⚡ **Real-time messaging** with threading | **Обмен сообщениями** в реальном времени  
- 🚪 **/quit** command to disconnect | Команда **/quit** для выхода  
- 🔒 **Basic error handling** | Базовая обработка ошибок  

---

### 🏁 Quick Start | Быстрый старт  

#### Server | Сервер  
```bash
# Start server on default 0.0.0.0:12345 | Запуск сервера
python server.py
```
**Пример запуска:**  
`🖥️ Server started on port 12345... Waiting for connections...`  

#### Client | Клиент  
```bash
# Connect to server | Подключение к серверу
python client.py
```
**Пример работы:**  
```
👤 Enter your name: Alice  
🔗 Connected! Start chatting...
> Hello everyone!  
[Bob]: Hi Alice!  
> /quit  
❌ Disconnected from server  
```

---

### ⚙️ Configuration | Настройка  

| Parameter | Настройка | Description | Описание |
|-----------|-----------|-------------|----------|
| `HOST = '0.0.0.0'` | `HOST = '0.0.0.0'` | Listen on all interfaces | Принимать подключения с любых IP |
| `PORT = 12345` | `PORT = 12345` | Custom port number | Номер порта для подключения |

**🔧 Советы:**  
- Для локального теста используйте `127.0.0.1` вместо `0.0.0.0`  
- Откройте порт в брандмауэре для сетевого доступа  

---

### 🎨 Пример сеанса чата  
```
[Server] 🟢 John joined the chat  
[John]: Привет всем!  
[Alice]: Привет, John! Как дела?  
[Server] 🔴 Bob left the chat  
> /quit  
```

---

### 🌍 Язык/Language  
🇬🇧 [English Version](#) | 🇷🇺 [Русская версия](#)  

<details>
<summary>📦 Требования | Requirements</summary>

- Python 3.6+  
- Доступ к сети | Network access  
- Открытый порт | Open port  

</details>

💡 **Подсказка:** Для публичного сервера добавьте аутентификацию!  

---
- Версия 1.0 | Version 1.0  
