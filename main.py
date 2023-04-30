import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from app.config import BOT_TOKEN
from app.handlers.echo import register_echo_handlers

async def _on_startup(dp: Dispatcher) -> None:
    register_echo_handlers(dp)

def main():

    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # Initialize bot and dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())


    executor.start_polling(dp, skip_updates=True, on_startup=_on_startup)

if __name__ == '__main__':
    main()
