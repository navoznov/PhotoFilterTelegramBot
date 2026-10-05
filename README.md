# PhotoFilterTelegramBot

A Telegram bot that turns photos black and white. Send it a photo, and it replies with the same picture in grayscale (PNG).

## Usage

1. Send the bot `/start`.
2. Send photos one at a time. The bot replies to each with a processed copy.
3. `/cancel` ends the conversation.

## Running

You need Python 3, [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) 13.x and [Pillow](https://python-pillow.org/). The bot uses the old API with `Updater` and `Filters`, so it won't run on version 20 or newer.

```sh
pip3 install "python-telegram-bot<14" Pillow
```

1. Create a bot with [@BotFather](https://t.me/BotFather) and get its token.
2. Next to the scripts, create the folders `Photos` (downloaded originals go here) and `Results` (processed pictures go here). The bot doesn't create them itself.
3. Run:

   ```sh
   python3 main.py --bot-token=<token>
   ```

## Project layout

- `main.py`: the entry point. Reads the options and starts the bot.
- `optionsParser.py`, `options.py`: parse the `--bot-token` option.
- `telegramBot.py`: the conversation with the user: greeting, receiving photos, sending results.
- `blackAndWhiteFilter.py`: the filter itself, which converts a picture to grayscale with Pillow.

## License

[GPL-3.0](LICENSE)
