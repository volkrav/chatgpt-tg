from aiogram import types
from aiogram.dispatcher import FSMContext

from app.config import VOICE_RELATIVE_DIR
from app.misc.open_ai import get_response_chatgpt, mp3_to_text
from app.misc.utils import (get_directory_path, make_filename_with_path,
                            ogg_to_mp3)


async def make_question_from_voice(message: types.Message) -> str:

    voice: types.File = await message.voice.get_file()
    voice_file_path = voice.file_path
    filename = str(message.from_user.id)

    voice_dir_path = await get_directory_path(VOICE_RELATIVE_DIR)
    ogg_file_path = await make_filename_with_path(voice_dir_path,
                                                  filename,
                                                  'ogg')

    await message.bot.download_file(file_path=voice_file_path,
                                    destination=ogg_file_path)

    mp3_file_path = await make_filename_with_path(voice_dir_path,
                                                  filename,
                                                  'mp3')
    try:
        await ogg_to_mp3(ogg_file_path, mp3_file_path)
    except ValueError as err:
        return await message.answer(f'I am got error {err}')

    return await mp3_to_text(mp3_file_path)


async def get_messages_from_storage(state: FSMContext) -> list:
    async with state.proxy() as data:
        return data.get('messages', [])


async def add_row_to_storage(key: str,
                             role: str,
                             content: str,
                             state: FSMContext) -> None:
    async with state.proxy() as data:
        data.setdefault(key, [])
        data[key].append(
            {'role': role,
             'content': content}
        )


async def send_answer_to_question(message: types.Message,
                                  state: FSMContext,
                                  question: str,
                                  markup) -> None:
    '''
    Sends the user a response from the bot to his question.
    Saves the history of correspondence in storage
    '''
    await add_row_to_storage('messages', 'user', question, state)
    messages = await get_messages_from_storage(state)
    response_chatgpt = await get_response_chatgpt(messages)
    await add_row_to_storage('messages', 'assistant', response_chatgpt, state)
    await message.answer(f'✅ <b>Моя відповідь:</b>\n\n{response_chatgpt}',
                         reply_markup=markup)
