import os
from enum import Enum
from dataclasses import dataclass
from typing import List

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
                  "<cyan>{name}</cyan>:<cyan>{file}</cyan>.<cyan>{function}</cyan>:<cyan>{line}</cyan> "
                  "- <level>{message}</level>")


@dataclass
class MyBot:
    token: str
    admins_id: List[int]


@dataclass
class Settings:
    bot: MyBot

    @staticmethod
    def load_env_file(name: str):
        _dotenv_path = os.path.join(os.path.dirname(__file__), name)
        if os.path.exists(_dotenv_path):
            load_dotenv(_dotenv_path)
        else:
            logger.error(f'Not found {name} file in {os.path.dirname(__file__)}')
            raise FileNotFoundError(f'Not found {name} file in {os.path.dirname(__file__)}')

    @staticmethod
    def get(env_filename: str):
        Settings.load_env_file(env_filename)
        return Settings(
            MyBot(
                token=os.getenv('TOKEN'),
                admins_id=list(map(int, os.getenv('ADMINS_ID').split(':')))
            )
        )


settings = Settings.get('.env')
