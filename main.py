from aiogram import Bot, Dispatcher
import asyncio
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import logging

from config import BOT_TOKEN


from handlers.start import router as start_router
from handlers.echo import router as echo_router
from handlers.audio import router as audio_router

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(audio_router)
    dp.include_router(echo_router)
    

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Бот остановлен")