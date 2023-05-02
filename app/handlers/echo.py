from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text

from app.config import BUTTON_NEW_TEXT, HELP_TEXT, NEW_TEXT, START_TEXT
from app.handlers.tools import (make_question_from_voice,
                                send_answer_to_question)
from app.keyboards.reply import kb_new


async def voice_message_handler(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends voice message
    """
    await message.answer("Повідомлення прийнято. Чекаю відповіді від сервера...")
    question = await make_question_from_voice(message)
    await message.answer(f"❓<b>Ваш запит:</b>\n\n{question}")
    await send_answer_to_question(message, state, question, kb_new)


async def send_welcome(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/start` command
    """
    await state.finish()
    await message.answer(text=START_TEXT,
                         reply_markup=kb_new)


async def send_help(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/help` command
    """
    await message.answer(text=HELP_TEXT,
                         reply_markup=kb_new)


async def start_new_conversation_handler(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends `/new` command
    or or presses a button "Start a new conversation"
    """
    await state.finish()
    await message.answer(text=NEW_TEXT,
                         reply_markup=kb_new
                         )


async def text_message_handler(message: types.Message, state: FSMContext):
    """
    This handler will be called when user sends text message
    """
    await send_answer_to_question(message, state, message.text, kb_new)


def register_all_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(voice_message_handler,
                                content_types=[types.ContentType.VOICE])
    dp.register_message_handler(send_welcome,
                                CommandStart())
    dp.register_message_handler(send_help,
                                CommandHelp())
    dp.register_message_handler(start_new_conversation_handler,
                                commands=['new'])
    dp.register_message_handler(start_new_conversation_handler,
                                Text(equals=BUTTON_NEW_TEXT,
                                     ignore_case=True))
    dp.register_message_handler(text_message_handler)
