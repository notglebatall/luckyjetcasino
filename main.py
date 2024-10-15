import os
import logging
import asyncio

from aiogram.client.default import DefaultBotProperties
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

load_dotenv()

from bot.handlers import router
from database.engine import create_db, session_maker
from middlewares.db import DataBaseSession


async def main():

    await create_db()
    bot = Bot(
        token=os.getenv('BOT_TOKEN'),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.include_router(router)
    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
