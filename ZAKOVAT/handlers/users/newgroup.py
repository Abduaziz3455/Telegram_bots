import sqlite3

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import Message, ChatActions

from data.config import ADMINS
from filters.private_chat import IsPrivate
from loader import dp, bot, db
from states.new import gruppa


@dp.message_handler(IsPrivate(), CommandStart())
async def new(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    name = msg.from_user.full_name

    await msg.answer(
        f"Assalomu alaykum {msg.from_user.get_mention()}. Zakovat savollari botiga xush kelipsiz!\nJamoangiz nomini kiriting:")
    if not db.select_user(id=user_id):
        try:
            db.add_user(id=user_id, name=name, type=1)
            # Adminga xabar beramiz
            count = db.count_users()[0]
            msg = f"{msg.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
            await bot.send_message(chat_id=ADMINS[0], text=msg)
        except sqlite3.IntegrityError or sqlite3.OperationalError as err:
            await bot.send_message(chat_id=ADMINS[0], text=err)

    await gruppa.yangi.set()


@dp.message_handler(IsPrivate(), content_types='text', state=gruppa.yangi)
async def nom(msg: Message, state: FSMContext):
    await ChatActions.typing()
    if not db.select_group_user(id=msg.from_user.id):
        if not db.select_group_user(g_name=msg.text):
            try:
                db.add_user(id=msg.from_user.id, name=msg.text, type=2)
                await msg.answer(f"Tabriklaymiz, siz {msg.text} guruh nomi bilan ro'yxatdan o'tdingiz")
                await state.finish()
                await bot.send_message(chat_id=1556455886,
                                       text=f"Yangi jamoa qo'shildi. Jamoa nomi --  <b>{msg.text}</b>\n"
                                            f"Jamoa sardori - {msg.from_user.get_mention(as_html=True)}")
            except sqlite3.IntegrityError as err:
                await bot.send_message(chat_id=ADMINS[0], text=err)
        else:
            await msg.answer("Bu nom avval ro'yxatdan o'tgan. Boshqa nom tanlang!")
    else:
        await msg.answer(f"{msg.from_user.get_mention(as_html=True)} siz avval ro'yxatdan o'tgansiz")
        await state.finish()
