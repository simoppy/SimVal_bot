from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keybords.keybord import * 

router = Router()


@router.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "Hello wold",
        reply_markup=get_start_rely_keybord()
            )
@router.message()
async def other(message: Message):
    await message.answer("Такой команды нет")