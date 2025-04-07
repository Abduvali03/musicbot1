from aiogram import types, Dispatcher

async def search_command(message: types.Message):
    await message.answer("Қидирмоқчи бўлган мусиқа номини ёзинг:")

def register(dp: Dispatcher):
    dp.register_message_handler(search_command, commands=['search'])
