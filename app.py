from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from config import BOT_TOKEN

from handlers import start, search, download

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

start.register(dp)
search.register(dp)
download.register(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
