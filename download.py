from aiogram import types, Dispatcher
from utils.youtube import download_audio

async def download_command(message: types.Message):
    query = message.get_args()
    if not query:
        await message.reply("Қидирув учун мусиқа номини ёзинг. Масалан: `/download Billie Jean`", parse_mode="Markdown")
        return

    await message.reply("Юкланмоқда, илтимос кутиб туринг...")
    audio_file = await download_audio(query)

    if audio_file:
        await message.reply_audio(open(audio_file, 'rb'))
    else:
        await message.reply("Қидирувда хатолик юз берди ёки топилмади.")

def register(dp: Dispatcher):
    dp.register_message_handler(download_command, commands=['download'])
