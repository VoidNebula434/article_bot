# Бот-визитка для демонстрации работы с интернационализацией и локализацией

## Зависимости

При написании бота использовался `python 3.13.10`.

Основные библиотеки:

- `aiogram` — библиотека для разработки Telegram-ботов.
- `environs` — библиотека, позволяющая более удобно работать с переменными окружения.
- `aiosqlite` — асинхронная библиотека для работы с SQLite.
- `fluentogram` — библиотека для интеграции Fluent с aiogram. Позволяет хранить переводы в отдельных файлах и удобно подставлять тексты в зависимости от локали пользователя.

## Структура проекта

```text
bot/
├─ .env
├─ config.py
├─ main.py
├─ keyboards.py
├─ requirements.txt
├─ db/
│  ├─ __init__.py
│  ├─ connection.py
│  ├─ users.py
├─ handlers/
│  ├─ __init__.py
│  ├─ common.py
├─ middlewares/
│  ├─ __init__.py
│  ├─ db.py
│  └─ i18n.py
└─ i18n/
   ├─ __init__.py
   ├─ translator_hub.py
   └─ locales/
      ├─ en/LC_MESSAGES/txt.ftl
      └─ ru/LC_MESSAGES/txt.ftl
```

## Установка и запуск

1. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   ```
2. Активируйте окружение:
   ```bash
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите бота:
   ```bash
   python main.py
   ```
