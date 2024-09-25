from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

one_klava = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Я олух", callback_data='one'),
            InlineKeyboardButton(text="Я лох", callback_data='too'),
            InlineKeyboardButton(text="Я просто пенсил", callback_data='three'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)