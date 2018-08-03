from biblioteca_comunitaria import BibliotecaComunitaria
import telegram_client

class App:
    _biblioteca = BibliotecaComunitaria()

    @staticmethod
    def biblioteca():
        return App._biblioteca

if __name__ == "__main__":
    print 'App Launched'
    telegram_client.TelegramClient('413352364:AAEeRyLwuX8A7oeK1HVb1AGc4L6rYofwBQQ').start()
