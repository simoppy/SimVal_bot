from aiogram import Router,F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.keyboard_replay import * 
from keyboards.keyboard_inline import *

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Hello wold",
        reply_markup=get_start_rely_keyboard()
            )
@router.message(F.text.lower() == "добавить материал")
async def other(message: Message):
    await message.answer(
        "Выберите предмет из списка по которому хотите добавить материал:",
        reply_markup=get_subjects_inline_keyboard()
        )
@router.callback_query(SubjectCallback.filter())
async def subject_choice(callback: types.CallbackQuery, callback_data: SubjectCallback):
    subject = callback_data.name

    match subject:
        case "eng":
            pass 
        case "math":
            pass 
        case "it":
            pass 
        case "obizr":
            pass
        case "phys":
            pass 
        case "bio":
            pass 
        case "hist":
            pass 
        case "lit":
            pass 
        case "geo":
            pass 
        case "project":
            pass 
        case "pe":
            pass 
        case "soc":
            pass 
        case "chem":
            pass 
        case "rus":
            pass 
        case "other":
            pass
        case "cancel":
            await callback.message.edit_text("Выбор отменен")
        
        case _:print(f"Неизвестный предмет: {subject}")
    await callback.answer()
    
@router.message()
async def other(message: Message):
    await message.answer("Такой команды нет")