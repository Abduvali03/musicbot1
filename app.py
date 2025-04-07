from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.reply("Salom! MusicBot muvaffaqiyatli ishga tushdi!")

if __name__ == "__main__":
    executor.start_polling(dp)