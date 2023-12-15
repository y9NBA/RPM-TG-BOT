from yaml import Loader, load
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

MENU = load(open(
    os.path.join(os.getcwd(), 'tb', 'management', 'commands', 'navigation.yml'),
    'r', encoding='utf-8'), Loader=Loader)

def get_static_buttons(context: dict):
    buttons = []
    state = context["new_state"]
    if 'static_buttons' not in MENU[state]:
        return buttons
    
    for button_text, params in MENU[state]["static_buttons"].items():
        callback_data = {'new_state': params['new_state']}
        buttons.append(InlineKeyboardButton(
            text=button_text,
            callback_data=str(callback_data)))
    
    return buttons

def get_reply_message(context: dict):
    inline_keyboard = []
    # row = []
    # for button in get_dynamic_buttons(context):
    #     row.append(button)
    #     if len(row) == 1:
    #         inline_keyboard.append(row)
    #         row = []
    # if len(row) > 0:
    #     inline_keyboard.append(row)

    # inline_keyboard.append(get_conditional_buttons(context))
    
    inline_keyboard.append(get_static_buttons(context))
    
    markup = InlineKeyboardMarkup(
        inline_keyboard=inline_keyboard)

    text = eval(MENU[context['new_state']]['message'].format(**context))
    return text, markup
