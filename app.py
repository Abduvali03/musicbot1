from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

BOT_TOKEN = "8072492883:AAEMeZ9ScYhKtWDpUZGCv1c_GsQWKfeoUfU"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.reply("Salom! MusicBot muvaffaqiyatli ishga tushdi!")

if __name__ == "__main__":
    executor.start_polling(dp)