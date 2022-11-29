import logging

from aiogram.types import Message
from aiogram.dispatcher.filters import CommandStart, Command

from data.config import SUPERUSERS
from filters.private_chat import IsPrivate
from loader import dp, bot
from aiogram.dispatcher import filters, FSMContext

from states.new import gruppa


@dp.message_handler(IsPrivate(), CommandStart())
async def new(msg: Message, state: FSMContext):
    await msg.answer("Jamoangiz nomini kiriting:")
    await gruppa.yangi.set()


data = {}


@dp.message_handler(IsPrivate(), state=gruppa.yangi)
async def nom(msg: Message, state: FSMContext):
    global data

    if not data:
        await msg.answer(f"Tabriklaymiz, siz {msg.text.title()} guruh nomi bilan ro'yxatdan o'tdingiz")
        data[f"{msg.from_user.id}"] = msg.text
        await state.finish()
        await bot.send_message(chat_id=1556455886,
                               text=f"Yangi jamoa qo'shildi. Jamoa nomi --  <b>{msg.text.title()}</b>\n"
                                    f"Jamoa sardori - {msg.from_user.get_mention(as_html=True)}")
    else:
        for key, value in data.items():
            if msg.from_user.id != int(key):
                if value == msg.text:
                    await msg.answer("Bu nom avval ro'yxatdan o'tgan. Boshqa nom tanlang:")
                    return
                else:
                    await msg.answer(f"Tabriklaymiz, siz <b>{msg.text.title()}</b> guruh nomi bilan ro'yxatdan o'tdingiz")
                    data[f"{msg.from_user.id}"] = msg.text
                    await state.finish()
                    await bot.send_message(chat_id=1556455886,
                                           text=f"Yangi jamoa qo'shildi. Jamoa nomi --  <b>{msg.text.title()}</b>\n"
                                                f"Jamoa sardori - {msg.from_user.get_mention(as_html=True)}")
            else:
                await msg.answer(
                    f"{msg.from_user.get_mention(as_html=True)} avval ro'yxatdan o'tgansiz! Jamoangiz nomi - <b>{value}</b>")
                await state.finish()


@dp.message_handler(Command("stop", prefixes="!/"), filters.IDFilter(chat_id=SUPERUSERS))
async def teams(msg: Message, state: FSMContext):
    team = ",   ".join(data.values())
    await msg.answer(f"Barcha ro'yxatdan o'tgan jamoalar: <b>{team}</b>")
