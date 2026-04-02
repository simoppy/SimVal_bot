import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession 

from handlers.routers import router
from cfg.config_load import TOKEN,PROXY_URL
from memory.google_drive_uploader import upload_to_drive # загрузка на гугл диск

# логи
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    filename="logs/bot.log",  
    filemode="a",
    encoding="utf-8"
)

dp = Dispatcher()
dp.include_router(router)
session = AiohttpSession(proxy=PROXY_URL)

async def main():
    bot = Bot(token=TOKEN, session=session)
    print("Starting...")
    await dp.start_polling(bot, drop_pending_updates=True)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Stopping...")