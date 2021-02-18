#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
import os
from blackAndWhiteFilter import BlackAndWhiteFilter

class TelegramBot:

    def __init__(self, token: str, blackAndWhiteFilter: BlackAndWhiteFilter):
        self.__token = token
        self.__blackAndWhiteFilter = blackAndWhiteFilter

    def go(self) -> None:
        # TODO: длинный метод
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        logger = logging.getLogger(__name__)


        MAIN_MENU_STATE, UPLOAD_PHOTO_STATE = range(2)

        def main_menu_state_handler(update: Update, context: CallbackContext) -> int:
            logger.info("Main menu")
            text = 'Привет. Присылайте мне фотки (по одной за раз), и я сделаю их черно-белыми.'
            update.message.reply_text(text)
            return UPLOAD_PHOTO_STATE

        def upload_photo_handler(update: Update, context: CallbackContext) -> int:
            user = update.message.from_user
            photo = update.message.photo[-1]
            file_id = photo.file_id
            original_file_path = f'Photos/{file_id}'
            if not os.path.isfile(original_file_path):
                photo_file = photo.get_file()
                photo_file.download(original_file_path)

            logger.info("UserPhoto of %s: %s", user.first_name, original_file_path)

            file_bytes = photo = open(original_file_path, 'rb').read()
            converted_file_path = f'Results/{file_id}.png'
            self.__blackAndWhiteFilter.apply(original_file_path, converted_file_path)

            converted_photo = open(converted_file_path, 'rb')
            update.message.reply_photo(converted_photo, reply_to_message_id=update.message.message_id)
            return MAIN_MENU_STATE

        def send_photo(update: Update, context: CallbackContext) -> int:
            photo = open('Photos/Test-JPEG-1.jpg', 'rb')
            update.message.reply_photo(photo)
            return MAIN_MENU_STATE

        def cancel(update: Update, context: CallbackContext) -> int:
            logger.info("Отмена")
            text = 'Bye! I hope we can talk again some day.'
            update.message.reply_text(text, reply_markup=ReplyKeyboardRemove(), reply_to_message_id=update.message.message_id)
            return ConversationHandler.END

        conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', main_menu_state_handler)],
            states={
                MAIN_MENU_STATE: [
                    MessageHandler(Filters.text, send_photo),
                    MessageHandler(Filters.photo, upload_photo_handler),
                ],
                UPLOAD_PHOTO_STATE: [
                    MessageHandler(Filters.photo, upload_photo_handler),
                    MessageHandler(Filters.text, send_photo),
                ],
            },
            fallbacks=[CommandHandler('cancel', cancel)],
        )

        updater = Updater(self.__token)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(conv_handler)
        updater.start_polling()
        updater.idle()
