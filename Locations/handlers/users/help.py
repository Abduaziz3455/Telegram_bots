from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Commands: ",
            "/start - start bot",
            "/help - Any questions? You can contact with admin @abduaz1z")
    
    await message.answer("\n".join(text))