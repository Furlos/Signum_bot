import os
from enum import Enum

from loguru import logger
from dotenv import load_dotenv

_dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(_dotenv_path):
    load_dotenv(_dotenv_path)
else:
    raise FileNotFoundError(f'Not found .env file in {os.path.dirname(__file__)}')


class LogLevel(Enum):
    CRITICAL = 'CRITICAL'
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    INFO = 'INFO'
    DEBUG = 'DEBUG'


TOKEN = os.getenv('TOKEN')

# logger.remove()
logger.add(os.path.dirname(__file__) + '/logs/logs_{time}.log',
           level=LogLevel.DEBUG.value,
           enqueue=True,
           format="{time:DD-MM-YYYY at HH:mm:ss} | "
                  "<level>{level:^8}</level> | "
                  "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")
