import random

from lexicon.lexicon import LEXICON_RU

# Функция, возвращающая случайный выбор бота в игре
def get_bot_choice() -> str:
    return random.choice(['kamen', 'bumaga', 'nozni'])


# Функция, возвращающая случайный выбор игрока в игре
def get_user_answer(user_answer: str)-> str:
    for key in LEXICON_RU:
        if user_answer == LEXICON_RU[key]:
            break
    return key

#для определения победителя
def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = get_user_answer(user_choice)
    rules = {'kamen': 'nozni',
             'nozni': 'bumaga',
             'bumaga': 'kamen'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    return 'bot_won'
    
