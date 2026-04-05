from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup


class SubjectCallback(CallbackData, prefix="sub"):
    name: str

def get_subjects_inline_keyboard():
    builder = InlineKeyboardBuilder()
    
  
    subjects = [
        ("🇬🇧 Английский", "eng"), ("📐 Математика", "math"),
        ("💻 Информатика", "it"), ("🛡️ ОБиЗР", "obizr"),
        ("🧲 Физика", "phys"), ("🧬 Биология", "bio"),
        ("📜 История", "hist"), ("📚 Литература", "lit"),
        ("🌍 География", "geo"), ("💡 ИП (Проект)", "project"),
        ("🏃 Физ-ра", "pe"), ("⚖️ Общество", "soc"),
        ("🧪 Химия", "chem"), ("🇷🇺 Русский", "rus"),
        ("📁 Другое", "other"), ("❌ Отмена", "cancel")
    ]

    for text, callback_val in subjects:
        builder.button(
            text=text, 
            callback_data=SubjectCallback(name=callback_val)
        )
    
    builder.adjust(2,2,2,2,2,2,2,1,1)
    return builder.as_markup()
 