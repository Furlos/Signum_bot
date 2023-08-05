import asyncio
from aiogram import Bot, Dispatcher
from aiogram.exceptions import TelegramNetworkError
from aiogram.filters import Command

from signum_bot.bot.settings import settings
from signum_bot.bot.core.handlers.basic import *


async def on_statr_up(bot: Bot):
    for tg_id in settings.bot.admins_id:
        await bot.send_message(tg_id, text='Бот запущен!')


async def on_shutdown(bot: Bot):
    for tg_id in settings.bot.admins_id:
        await bot.send_message(tg_id, text='Бот остановлен!')


@logger.catch
async def main():
    bot = Bot(token=settings.bot.token, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(on_statr_up)
    dp.message.register(start_cmd, Command(commands=['start']))
    dp.message.register(help_cmd, Command(commands=['help']))
    dp.message.register(echo)
    dp.shutdown.register(on_shutdown)

    try:
        logger.info('Запуск процесса поллинга новых апдейтов')
        await dp.start_polling(bot)
    except TelegramNetworkError as e:
        logger.error(e)
    finally:
        logger.info("Бот остановлен")
        await bot.session.close()


if __name__ == "__main__":
    logger.info("Запуск бота")
    asyncio.run(main())
    logger.info('Конец работы программы')
