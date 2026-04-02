from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_subjects_inline_keybord():
    buttons = [
        [
            InlineKeyboardButton(text="🇬🇧 Английский язык", callback_data="sub_eng"),
            InlineKeyboardButton(text="📐 Математика", callback_data="sub_math")
        ],
        [
            InlineKeyboardButton(text="💻 Информатика", callback_data="sub_it"),
            InlineKeyboardButton(text="🛡️ ОБиЗР", callback_data="sub_obizr")
        ],
        [
            InlineKeyboardButton(text="🧲 Физика", callback_data="sub_phys"),
            InlineKeyboardButton(text="🧬 Биология", callback_data="sub_bio")
        ],
        [
            InlineKeyboardButton(text="📜 История", callback_data="sub_hist"),
            InlineKeyboardButton(text="📚 Литература", callback_data="sub_lit")
        ],
        [
            InlineKeyboardButton(text="🌍 География", callback_data="sub_geo"),
            InlineKeyboardButton(text="💡 ИП (Проект)", callback_data="sub_project")
        ],
        [
            InlineKeyboardButton(text="🏃 Физ-ра", callback_data="sub_pe"),
            InlineKeyboardButton(text="⚖️ Обществознание", callback_data="sub_soc")
        ],
        [
            InlineKeyboardButton(text="🧪 Химия", callback_data="sub_chem"),
            InlineKeyboardButton(text="🇷🇺 Русский язык", callback_data="sub_rus")
        ],
        [
            InlineKeyboardButton(text="📁 Другое", callback_data="sub_other")
        ],
        [
            InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_subjects")
        ]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
