from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Вставьте ваш токен
TOKEN = '7691317600:AAF5_Q-M0imjIeVbw71HNUWl0k5I7mrBDKw'

def start(update: Update, context: CallbackContext) -> None:
    """Отправляет сообщение, когда бот получает команду /start."""
    update.message.reply_text('Привет! Я бот для игры в Крестики-Нолики. Напишите /play, чтобы начать игру!')

def play(update: Update, context: CallbackContext) -> None:
    """Запускает игру."""
    # Здесь вы можете добавить логику для начала игры
    update.message.reply_text('Игра начинается!')

def main() -> None:
    """Запускает бота."""
    # Создаем объект Updater и передаем ему токен вашего бота
    updater = Updater(TOKEN)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Добавляем обработчики команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

    # Начинаем получать обновления от Telegram
    updater.start_polling()

    # Бот будет работать до тех пор, пока не будет остановлен
    updater.idle()

if __name__ == '__main__':
    main()
