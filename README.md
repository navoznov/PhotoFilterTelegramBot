# PhotoFilterTelegramBot

Telegram-бот, который делает фотографии чёрно-белыми. Присылаете фото, бот отвечает на него той же картинкой в оттенках серого (PNG).

## Как пользоваться

1. Отправьте боту `/start`.
2. Присылайте фото по одному. На каждое бот ответит обработанной копией.
3. `/cancel` завершает диалог.

## Запуск

Нужны Python 3, [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) 13.x (бот написан под старый API с `Updater` и `Filters`, на версиях 20+ не запустится) и [Pillow](https://python-pillow.org/):

```sh
pip3 install "python-telegram-bot<14" Pillow
```

1. Создайте бота у [@BotFather](https://t.me/BotFather) и получите токен.
2. Создайте рядом со скриптами папки `Photos` (сюда скачиваются оригиналы) и `Results` (сюда сохраняются обработанные картинки). Сам бот их не создаёт.
3. Запустите:

   ```sh
   python3 main.py --bot-token=<токен>
   ```

## Устройство

- `main.py` — точка входа: читает параметры и запускает бота.
- `optionsParser.py`, `options.py` — разбор параметра `--bot-token`.
- `telegramBot.py` — диалог с пользователем: приветствие, приём фото, отправка результата.
- `blackAndWhiteFilter.py` — сам фильтр: перевод картинки в оттенки серого через Pillow.

## Лицензия

[GPL-3.0](LICENSE)
