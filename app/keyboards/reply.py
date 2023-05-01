from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from app.config import BUTTON_NEW_TEXT

kb_new = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=BUTTON_NEW_TEXT)
        ],
    ],
    resize_keyboard=True,
    is_persistent=True
)
