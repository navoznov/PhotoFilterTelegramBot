from options import Options
from optionsParser import OptionsParser
from telegramBot import TelegramBot
from blackAndWhiteFilter import BlackAndWhiteFilter

options = OptionsParser.parse()
blackAndWhiteFilter = BlackAndWhiteFilter()
bot = TelegramBot(options.telegram_bot_token, blackAndWhiteFilter)
bot.go()
