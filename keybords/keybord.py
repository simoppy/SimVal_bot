from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_start_rely_keybord():
    buttons = [
        [
            KeyboardButton(text="Добавить материал"),
            KeyboardButton(text="Просмотреть материал")
        ],
        [
            KeyboardButton(text="О боте")
        ]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    return keyboard