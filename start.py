from aiogram import types, Dispatcher

async def start_command(message: types.Message):
    await message.answer("Салом, мен профессионал мусиқа ботиман!")

def register(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
