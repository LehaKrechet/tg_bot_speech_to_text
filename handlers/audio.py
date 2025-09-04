from aiogram import Router, types, F
from aiogram.types import FSInputFile
import os
from datetime import datetime
from config import VOICE_DIR
from speech_to_text import speech_to_text

router = Router()
DOWNLOAD_DIR = VOICE_DIR

# @router.message(F.audio)
# async def handle_audio(message: types.Message):
#     # Получаем информацию об аудиофайле
#     audio = message.audio
#     file_id = audio.file_id
#     file_size = audio.file_size
#     duration = audio.duration
#     title = audio.title or "Без названия"
#     performer = audio.performer or "Неизвестный исполнитель"
    
#     # Отправляем информацию об аудио
#     await message.answer(
#         f"🎵 Получено аудио!\n\n"
#         f"📝 Название: {title}\n"
#         f"🎤 Исполнитель: {performer}\n"
#         f"⏱ Длительность: {duration} секунд\n"
#         f"📊 Размер: {file_size} байт\n"
#         f"🆔 File ID: {file_id}"
#     )
    
#     # Скачиваем файл (опционально)
#     try:
#         bot = message.bot
#         file = await bot.get_file(file_id)
#         file_path = file.file_path

#         timestamp = datetime.now().strftime("%Y%m%d_%H%M")
#         filename = f"voice_{timestamp}.ogg"  # Голосовые сообщения обычно в .ogg
#         download_path = os.path.join(DOWNLOAD_DIR, filename)
        
#         # Скачиваем файл
#         await bot.download_file(file_path, download_path)
        
#         await message.answer("✅ Аудиофайл успешно сохранен!")
        
#     except Exception as e:
#         await message.answer(f"❌ Ошибка при скачивании: {e}")

@router.message(F.voice)
async def handle_voice(message: types.Message):
    # Обработка голосовых сообщений
    voice = message.voice
    duration = voice.duration
    file_size = voice.file_size
    file_id = voice.file_id
    
    await message.answer(
        f"🎤 Голосовое сообщение!\n\n"
        f"⏱ Длительность: {duration} секунд\n"
        f"📊 Размер: {file_size} байт\n"
    )

    try:
        bot = message.bot
        file = await bot.get_file(file_id)
        file_path = file.file_path

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"voice_{timestamp}.ogg"  # Голосовые сообщения обычно в .ogg
        download_path = os.path.join(DOWNLOAD_DIR, filename)
        
        # Скачиваем файл
        await bot.download_file(file_path, download_path)
        
        await message.answer("✅ Аудиофайл успешно сохранен!")

        for split in speech_to_text():

            await message.answer(split)
        
    except Exception as e:
        await message.answer(f"❌ Ошибка при скачивании: {e}")