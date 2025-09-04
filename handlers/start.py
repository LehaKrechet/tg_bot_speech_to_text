from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я  бот который транскрибирует аудио в текст!\n\n"
        "Доступные команды:\n"
        "/start - начать работу\n"
        "/help - помощь"
    )

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("🤖 Это бот который транскрибирует аудио в текст, просто отправь аудио и получи текст!")