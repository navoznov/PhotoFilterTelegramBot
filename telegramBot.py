#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageEnhance
import logging
from uuid import uuid4
from telegram import InlineQueryResult, InlineQueryResultArticle, ParseMode, InputTextMessageContent, ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    InlineQueryHandler
)
import re


class TelegramBot:

    def __init__(self, token: str):
        self.__token = token

    def go(self) -> None:
        # TODO: длинный метод
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)


        updater = Updater(self.__token)
        dispatcher = updater.dispatcher
        # dispatcher.add_handler(conv_handler)
        updater.start_polling()
        updater.idle()
