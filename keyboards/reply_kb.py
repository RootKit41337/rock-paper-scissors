from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from lexicon.lexicon import LEXICON_RU

yes_no_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = LEXICON_RU['yes_button'] ),
            KeyboardButton(text = LEXICON_RU['no_button'],)
        ]
    ],
    resize_keyboard = True,
    one_time_keyboard = True
)

suefa_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=LEXICON_RU['kamen'])
        ],
        [
            KeyboardButton(text=LEXICON_RU['nozni'])
        ],
        [
            KeyboardButton(text=LEXICON_RU['bumaga'])
        ]
    ],
    resize_keyboard=True
)