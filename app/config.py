from os import environ, getenv

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = environ.get('BOT_TOKEN', 'define bot token!')

VOICE_RELATIVE_DIR = 'data/files/voices'

OPENAI_API_KEY = getenv('OPENAI_API_KEY')

BUTTON_NEW_TEXT = 'Почати нову розмову'
