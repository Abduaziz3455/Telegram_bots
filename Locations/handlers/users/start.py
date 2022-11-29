from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.menuKeyb import menu
from loader import dp
from states.holat import holatlar


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Hello, {message.from_user.full_name}👋\n"
                         f"🌆 Welcome to Navoi!")
    await message.answer(f"Choose where do you want to go 🌍:", reply_markup=menu)
