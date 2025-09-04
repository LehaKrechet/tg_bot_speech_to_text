import whisper
import os
from config import VOICE_DIR

def file_worker():
    path = VOICE_DIR
    all_items = os.listdir(path)
    return all_items

def split_message(text, max_length=4096):
    """Разделяет текст на части не длиннее max_length"""
    parts = []
    while text:
        if len(text) <= max_length:
            parts.append(text)
            break
        else:
            # Ищем последний перенос строки или пробел в пределах лимита
            split_index = text.rfind('\n', 0, max_length)
            if split_index == -1:
                split_index = text.rfind(' ', 0, max_length)
            if split_index == -1:
                split_index = max_length
            
            parts.append(text[:split_index])
            text = text[split_index:].lstrip()
    
    return parts

def speech_to_text():
# Загружаем модель (чем больше модель, тем точнее, но медленнее)
# Доступные модели: tiny, base, small, medium, large
    model = whisper.load_model("medium") 

    for i in file_worker():

        try:
    # Преобразуем аудио в текст
            result = model.transcribe(f"{VOICE_DIR}{i}")
            flag = 1
        except:
            flag = 0
        if flag:
            os.remove(f"{VOICE_DIR}{i}")

    # Печатаем результат
    return(split_message(result["text"]))


