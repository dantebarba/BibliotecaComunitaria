# -*- coding: utf-8 -*-
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
import logging
from app import App

class TelegramClient:

    def __init__(self, token_param=''):
        self.updater = Updater(token=token_param)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
        self.registerHandlers()

    def registerHandlers(self):
        self.dispatcher().add_handler(CommandHandler('start', CommandFactory.start))
        self.dispatcher().add_handler(CommandHandler('isbn', CommandFactory.isbn, pass_args=True))
        self.dispatcher().add_handler(CommandHandler('books', CommandFactory.books))
        self.dispatcher().add_handler(CommandHandler('help', CommandFactory.help))
        self.dispatcher().add_handler(MessageHandler(Filters.command, CommandFactory.unknown))

    def dispatcher(self):
        return self.updater.dispatcher

    def start(self):
        self.updater.start_polling()

    def stop(self):
        self.updater.stop()



class CommandFactory:

    @staticmethod
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
        text="Bienvenido a la biblioteca comunitaria. Ingrese /help para ayuda.")

    @staticmethod
    def unknown(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Comando incorrecto. Ingrese /help para visualizar todos los comandos")

    @staticmethod
    def isbn(bot, update, args):
        if not args:
            bot.send_message(chat_id=update.message.chat_id, text="Por favor ingrese un ISBN")
        else:
            try:
                bot.send_message(chat_id=update.message.chat_id, text=App.biblioteca().isbn(args[0]))
            except Exception as e:
                bot.send_message(chat_id=update.message.chat_id,
                text="Ha ocurrido un error al obtener el Libro con ISBN " + str(args[0]))
                raise

    @staticmethod
    def help(bot, update):
        help = '''
- /start → Comando de entrada al bot.
- /isbn {isbn} → Muestra el libro con ISBN {isbn} si existe
- /books → Lista todos los libros disponibles en la biblioteca
- /help → Muestra la lista de comandos
        '''
        bot.send_message(chat_id=update.message.chat_id, text=help)


    @staticmethod
    def books(bot, update):
        try:
            bot.send_message(chat_id=update.message.chat_id, text=App.biblioteca().books())
        except Exception as e:
            bot.send_message(chat_id=update.message.chat_id,
            text="Ha ocurrido un error al listar los libros")
            raise
