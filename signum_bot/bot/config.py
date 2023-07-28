import os
from dotenv import load_dotenv

_dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(_dotenv_path):
    load_dotenv(_dotenv_path)
else:
    raise FileNotFoundError(f'Not found .env file in {os.path.dirname(__file__)}')

TOKEN = os.getenv('TOKEN')
LOGGER_LEVEL = 'DEBUG'
