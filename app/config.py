from os import environ

from dotenv import find_dotenv, load_dotenv

from app.misc.utils import get_base_directory

load_dotenv(find_dotenv())

BOT_TOKEN = environ.get('BOT_TOKEN', 'define bot token!')

BASE_DIR = get_base_directory()
