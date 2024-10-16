from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = '7691317600:AAF5_Q-M0imjIeVbw71HNUWl0k5I7mrBDKw'
URL = f'https://api.telegram.org/bot{TOKEN}/'

@app.route('/webhook', methods=['POST'])
def webhook():
    update = request.get_json()
    print(update)  # Выводим обновление в консоль для отладки

    # Здесь вы можете обрабатывать обновления и отвечать на них
    return '', 200

if __name__ == '__main__':
    # Установите вебхук
    requests.get(f'{URL}setWebhook?url=https://ratatapapaz.github.io/nvigames.github.io//webhook')
    app.run(port=5000)
