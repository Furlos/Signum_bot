import os
from enum import Enum

from loguru import logger
from dotenv import load_dotenv


class _LogLevel(Enum):
    CRITICAL = 'CRITICAL'
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    INFO = 'INFO'
    DEBUG = 'DEBUG'


# logger.remove()
logger.add(os.path.dirname(__file__) + '/logs/logs_{time}.log',
           level=_LogLevel.DEBUG.value,
           enqueue=True,
           format="{time:DD-MM-YYYY at HH:mm:ss} | "
                  "<level>{level:^8}</level> | "
                  "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")

_dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(_dotenv_path):
    load_dotenv(_dotenv_path)
else:
    logger.error(f'Not found .env file in {os.path.dirname(__file__)}')
    raise FileNotFoundError(f'Not found .env file in {os.path.dirname(__file__)}')

TOKEN = os.getenv('TOKEN')
ADMINS_ID = os.getenv('ADMINS_ID').split(':')
