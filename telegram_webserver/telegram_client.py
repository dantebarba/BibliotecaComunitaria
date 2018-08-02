from telegram.ext import Updater
import logging
import app

class TelegramClient:

    def __init__(self, token=''):
        self.updater = Updater(token='token')
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
        self.registerHandlers

    def registerHandlers(self):
        self.dispatcher.add_handler(CommandHandler('start', CommandFactory.start))
        dispatcher.add_handler(MessageHandler(Filters.command, CommandFactory.unknown))

    def dispatcher(self):
        return self.updater.dispatcher

    def start(self):
        self.updater.start_polling()

    def stop(self):
        self.updater.stop()



class CommandFactory:
    def start(bot, update):
        bot.send_message(chat_id=update.message.chat_id,
        text="Bienvenido a la biblioteca comunitaria. Por favor ingrese el isbn del libro que busca.")

    def unknown(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Comando incorrecto. Por favor ingrese un isbn.")

    def isbn(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text=app.biblioteca().isbn(args[0]))
