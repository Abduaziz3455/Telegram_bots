import re

from aiogram import types
from aiogram.dispatcher import filters, FSMContext
from aiogram.dispatcher.filters import Command, Regexp

from data.config import SUPERUSERS
from keyboards.inline.answer_checker import check_ans
from loader import dp, bot, db

SAVOL = r"(!savol|/savol)?(\d+)? ?([\w+\D]+)?"
JAVOB = r"(!javob) ([\w+\D]+)"


@dp.message_handler(Command("savol", prefixes="!/"), filters.IDFilter(chat_id=SUPERUSERS), Regexp(SAVOL), state="*")
async def question(message: types.Message, state: FSMContext):
    if state:
        await state.finish()
    command_parse = re.compile(r"(!savol|/savol) ?(\d+)? ?([\w+\D]+)?")
    parsed = command_parse.match(message.text)
    number = parsed.group(2)
    comment = parsed.group(3)

    await bot.send_message(chat_id=-1001847076669, text=f"""📌Diqqat <b>{number}-savol!</b>📌\n{comment}\n\n""" +
                                                        f"""Ro'yhatdan o'tgan jamoalar javoblarni <a href="https://t.me/zakovat_navoiBot">botga</a> ga yuboring!!!""")
    # await bot.close_general_forum_topic(chat_id=-1001847076669)
    for i in db.select_all_group_users():
        await bot.send_message(chat_id=i[0], text=f"📌Diqqat <b>{number}-savol!</b>📌\n{comment}")


@dp.message_handler(Command("javob", prefixes="!"))
async def answer(message: types.Message, state: FSMContext):
    if db.select_group_user(id=message.from_user.id):
        command_parse = re.compile(JAVOB)
        parsed = command_parse.match(message.text)
        comment = parsed.group(2)
        guruh = db.select_group_user(id=message.from_user.id)[1]

        await message.reply(
            f"{message.from_user.get_mention(as_html=True)} ({guruh} guruhi sardori) javobingiz qabul qilindi!")
        await bot.send_message(chat_id=1556455886,
                               text=f"<b>{guruh}</b> guruhining bu savolga javobi quyidagicha:\n\n<b>{comment}</b>\n\nJavob to'g'rimi?",
                               reply_markup=check_ans)
    else:
        await message.answer(
            "Siz botimizdan ro'yxatdan o'tmagansiz. Iltimos botga o'tib ro'yxatdan o'ting: @zakovat_navoiBot")


@dp.callback_query_handler(text="right")
async def right(call: types.CallbackQuery):
    user_id = call.message.text
    a, *b = user_id.split()
    data = db.plus(nom=a)
    await call.answer(cache_time=2, text="1ball qo'shildi!", show_alert=False)
    await call.message.delete()
    await call.message.answer(f"{a.title()} guruhi <i>{data[0]} ball</i> yig'di!\nJavoblarni to'xtatish uchun /stop ni bosing!")


@dp.callback_query_handler(text='wrong')
async def wrong(call: types.CallbackQuery):
    await call.answer(text="Xato javob!", show_alert=False, cache_time=3)
    await call.message.delete()
