from aiogram.types import Message
from loguru import logger


async def start_cmd(message: Message):
    logger.info(f'{message.from_user.id} вызвал "/start"')
    await message.answer(f"Hello, {message.from_user.username}!")


async def help_cmd(message: Message):
    logger.info(f'{message.from_user.id} вызвал "/help"')
    text = ("<strong>/help</strong> - выводит список команд\n"
            "<strong>/start</strong> - приветствие пользователя\n")
    await message.answer(text)


async def echo(message: Message):
    logger.info(f'Пользователь -> {message.from_user.id} написал белиберду')
    await message.answer("Я не понимаю ...")
