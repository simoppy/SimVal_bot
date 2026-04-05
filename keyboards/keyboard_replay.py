from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_start_rely_keyboard():
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