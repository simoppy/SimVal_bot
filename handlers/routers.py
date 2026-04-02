from aiogram import Router,F
from aiogram.filters import Command
from aiogram.types import Message

from keybords.keybord_replay import * 
from keybords.keybord_inline import *

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Hello wold",
        reply_markup=get_start_rely_keybord()
            )
@router.message(F.text.lower() == "добавить материал")
async def other(message: Message):
    await message.answer(
        "Выберите предмет из списка по которому хотите добавить материал:",
        reply_markup=get_subjects_inline_keybord()
        )

@router.message()
async def other(message: Message):
    await message.answer("Такой команды нет")