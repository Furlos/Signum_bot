import asyncio
from os.path import dirname
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from loguru import logger

from config import TOKEN, LOGGER_LEVEL

logger.remove()
logger.add(dirname(__file__) + '/logs/logs_{time}.log', level=LOGGER_LEVEL, enqueue=True)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    logger.info(f'{message.from_user.username} called "/start"')
    await message.answer(f"Hello, {message.from_user.username}!")


@dp.message()
async def echo(message: types.Message):
    logger.info(f'{message.from_user.username} write to bot "{message.text}"')
    await message.answer(message.text)


@logger.catch
async def main():
    logger.info('Запуск процесса поллинга новых апдейтов')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
