import asyncio
import logging
import sys
from os import environ
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from Handlers.handlers import router




load_dotenv(".env")

TOKEN = environ.get("BOT_TOKEN")

dp = Dispatcher()


async def main() -> None:
    
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_routers(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    print("ok")
    asyncio.run(main())