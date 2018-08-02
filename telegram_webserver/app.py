from flask import Flask
from biblioteca_comunitaria import BibliotecaComunitaria
from telegram_client import TelegramClient

biblioteca = BibliotecaComunitaria()
telegram_client = TelegramClient('413352364:AAEeRyLwuX8A7oeK1HVb1AGc4L6rYofwBQQ')

app = Flask(__name__)

@app.route("/")
def hello():
    return "App running"

def biblioteca():
    return biblioteca

if __name__ == "__main__":
    telegram_client.start()
    app.run(host="0.0.0.0", ssl_context='adhoc')
