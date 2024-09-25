from aiogram import Router, F, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from lexicon.lexicon import LEXICON_RU
from keyboards.reply_kb import yes_no_kb, suefa_kb
from services.services import get_bot_choice, get_winner
from keyboards.inline_kb import one_klava

router = Router()

#Старт
@router.message(CommandStart())
async def start_message(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)

#Хелпа
@router.message(Command(commands='help'))
async def help_message(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)

#TODO: Согласие на начало игры
@router.message(F.text == LEXICON_RU['yes_button'])
async def start_game(message: Message):
    await message.answer(f'Приступим {message.from_user.first_name}\n\n делай выбор ⤵️', reply_markup=suefa_kb)

#TODO: Отказ играть
@router.message(F.text == LEXICON_RU['no_button'])
async def no_game(message: Message):
    await message.answer(text=LEXICON_RU['no'])

#TODO: Это логика которую я позаимствовал 
@router.message(F.text.in_([LEXICON_RU['bumaga'], LEXICON_RU['kamen'], LEXICON_RU['nozni']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f'{LEXICON_RU["bot_choice"]} '
                              f'- {LEXICON_RU[bot_choice]}')
    winner = get_winner(message.text, bot_choice)
    await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)


# Этот хэндлер будет срабатывать на команду "/delmenu"
# и удалять кнопку Menu c командами
@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')


#Срабатывает на команду /what
@router.message(Command(commands='what'))
async def what_message(message: Message):
    await message.answer(text=LEXICON_RU['/what'], reply_markup=one_klava)


#Срабатывает на колбек 
@router.callback_query(F.data == 'one')
async def knopki_inline_1(callback: CallbackQuery):
    await callback.answer(text='Ты олух', show_alert=True)



#Срабатывает на колбек 
@router.callback_query(F.data == 'too')
async def knopki_inline_2(callback: CallbackQuery):
    await callback.answer(text='Ты лох', show_alert=True)


#Срабатывает на колбек 
@router.callback_query(F.data == 'three')
async def knopki_inline_3(callback: CallbackQuery):
    await callback.answer(text='Ты просто пенсил', show_alert=True)


    

