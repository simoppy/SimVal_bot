from os import getenv
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession 
from dotenv import load_dotenv
from handlers.routers import router

load_dotenv()
TOKEN = getenv("BOT_TOKEN")
PROXY_URL = getenv("SOCKS5_PROXY")

dp = Dispatcher()
dp.include_router(router)
session = AiohttpSession(proxy=PROXY_URL)

async def main():
    bot = Bot(token=TOKEN, session=session)
    print("Starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())