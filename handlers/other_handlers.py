from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from lexicon.lexicon import LEXICON_RU

router = Router()

@router.message()
async def start(message: Message):
    await message.answer(f'{message.from_user.first_name}\n', text=LEXICON_RU['other_answer'])