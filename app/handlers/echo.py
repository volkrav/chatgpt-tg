from aiogram import Dispatcher, types

from app.config import BASE_DIR


async def voice_message_handler(message: types.Message):
    voice = await message.voice.get_url()

    await message.answer(voice)


async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)
    await message.answer(BASE_DIR)



def register_echo_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(voice_message_handler,
                                content_types=[types.ContentType.VOICE])
    dp.register_message_handler(send_welcome,
                                commands=['start', 'help'])
    dp.register_message_handler(echo)
