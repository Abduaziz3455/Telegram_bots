import asyncio
import datetime
import logging
import re

from aiogram import types
from aiogram.dispatcher.filters import Command, Regexp, IsReplyFilter
from aiogram.dispatcher import filters, FSMContext
from aiogram.utils.exceptions import BadRequest

from data.config import SUPERUSERS
from handlers.users.newgroup import data
from keyboards.inline.answer_checker import check_ans
from loader import dp, bot

SAVOL = r"(!savol|/savol)?(\d+)? ?([\w+\D]+)?"
JAVOB = r"(!javob)?(\d+)? ?([\w+\D]+)?"


@dp.message_handler(Command("savol", prefixes="!/"), filters.IDFilter(chat_id=SUPERUSERS), Regexp(SAVOL))
async def savol(message: types.Message, state: FSMContext):
    # chat_id = message.chat.id #guruh yoki bot ID
    # async with state.proxy() as data:
    #     data['savol_n'] += 1
    command_parse = re.compile(r"(!savol|/savol) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    number = parsed.group(2)
    comment = parsed.group(3)
    await bot.send_message(chat_id=-1001613793305, text=f"📌Diqqat <b>{number}-savol!</b>📌\n{comment}")


@dp.message_handler(Command("javob", prefixes="!"), IsReplyFilter(True))
async def javob(message: types.Message):
    for key, value in data.items():
        if message.from_user.id == int(key):
            command_parse = re.compile(r"(!javob) ?(\d+)? ?([\w+\D]+)?")
            parsed = command_parse.match(message.text)
            number = parsed.group(2)
            comment = parsed.group(3)
            await message.reply(
                f"{message.from_user.get_mention(as_html=True)} ({value} guruhi sardori) javobingiz qabul qilindi!")
            await bot.send_message(chat_id=1556455886,
                                   text=f"<b>{value.title()}</b> guruhining {number}-savolga javobi quyidagicha:\n\n<u>{comment}</u>\n\nJavob to'g'rimi?",
                                   reply_markup=check_ans)
        else:
            await message.answer(
                "Siz botimizdan ro'yxatdan o'tmagansiz. Iltimos botga o'tib ro'yxatdan o'ting: @zakovat_navoiBot")


ball = {}


@dp.callback_query_handler(text="right")
async def right(call: types.CallbackQuery):
    global ball
    if not ball:
        for key, value in data.items():
            ball[value] = 0

    for kalit, qiymat in data.items():
        for k, v in ball.items():
            ball[k] += 1
            await call.answer(cache_time=30, text="1ball qo'shildi!", show_alert=False)
            await call.message.delete()
            await call.message.answer(f"{qiymat.title()} guruhi <i>{ball[k]} ball</i> yig'di!")


@dp.callback_query_handler(text='wrong')
async def wrong(call: types.CallbackQuery):
    await call.answer(text="xato javob!", show_alert=False)
    await call.message.delete()
