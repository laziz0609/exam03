import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from ImloBot.handlers import router as handler
dp = Dispatcher(storage=MemoryStorage())

async def main():
    load_dotenv()
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    BOT = Bot(token=BOT_TOKEN)

    # faqat yangi Router obyektlarini qo‘shish
    dp.include_router(handler)

    await dp.start_polling(BOT)

if __name__ == "__main__":
    asyncio.run(main())
