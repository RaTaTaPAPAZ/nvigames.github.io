from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
import asyncio

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Вставьте ваш токен
TOKEN = '7691317600:AAF5_Q-M0imjIeVbw71HNUWl0k5I7mrBDKw'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отправляет сообщение, когда бот получает команду /start."""
    await update.message.reply_text('Привет! Я бот для игры в Крестики-Нолики. Напишите /play, чтобы начать игру!')

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Запускает игру."""
    await update.message.reply_text('Игра начинается!')

async def main() -> None:
    """Запускает бота."""
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("play", play))
    await application.run_polling()

if __name__ == '__main__':
    # Получаем текущий цикл событий и запускаем основной метод
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
