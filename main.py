import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession 

from handlers.routers import router
from cfg.config_load import TOKEN,PROXY_URL
from memory.google_drive_uploader import upload_to_drive # загрузка на гугл диск

dp = Dispatcher()
dp.include_router(router)
session = AiohttpSession(proxy=PROXY_URL)

async def main():
    bot = Bot(token=TOKEN, session=session)
    print("Starting...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())