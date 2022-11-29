from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

check_ans = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅", callback_data="right"),
        InlineKeyboardButton(text="❌", callback_data="wrong")
    ]]
)