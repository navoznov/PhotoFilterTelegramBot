from options import Options
from optionsParser import OptionsParser
from telegramBot import TelegramBot

options = OptionsParser.parse()
bot = TelegramBot(options.telegram_bot_token)
bot.go()
