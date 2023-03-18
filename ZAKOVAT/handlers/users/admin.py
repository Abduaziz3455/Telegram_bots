import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from loader import dp, db, bot
from states.new import gruppa


@dp.message_handler(commands="start", user_id=ADMINS, state="*")
async def create_table_users(message: types.Message, state: FSMContext):
    if state:
        await state.finish()
    await message.answer(f"Salom {message.from_user.get_mention(as_html=True)}")
    await message.answer(f"Commands: \n/all_users,  \n/reklama,  \n/clean_db,  \n/create_db, \n/stop")


@dp.message_handler(commands="create_db", user_id=ADMINS, state="*")
async def create_table_users(message: types.Message, state: FSMContext):
    if state:
        await state.finish()
    users = db.create_table_users()
    await message.answer("Baza yaratildi!!!")
    await message.answer(f"Commands: \n/all_users,  \n/reklama,  \n/clean_db,  \n/create_db, \n/stop")


@dp.message_handler(commands="all_users", user_id=ADMINS, state="*")
async def get_all_users(message: types.Message, state: FSMContext):
    if state:
        await state.finish()
    users = db.select_all_group_users()
    await message.answer(users)
    await message.answer(f"Commands: \n/all_users,  \n/reklama,  \n/clean_db,  \n/create_db, \n/stop")


@dp.message_handler(commands="reklama", user_id=ADMINS, state="*")
async def send_ad_to_all(message: types.Message):
    await message.answer("Reklamangizni tashlang: ")
    await gruppa.reklama.set()


@dp.message_handler(content_types='text', state=gruppa.reklama, user_id=ADMINS)
async def rek(message: types.Message, state: FSMContext):
    users = db.select_all_users()

    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=message.text)
        await asyncio.sleep(0.05)
    await message.reply("Reklama jo'natildi!")
    await state.finish()
    await message.answer(f"Commands: \n/all_users,  \n/reklama,  \n/clean_db,  \n/create_db, \n/stop")


@dp.message_handler(commands="clean_db", user_id=ADMINS, state="*")
async def get_all_users(message: types.Message, state: FSMContext):
    if state:
        await state.finish()
    db.delete_users()
    await message.answer("Baza tozalandi!")
    await message.answer(f"Commands: \n/all_users,  \n/reklama,  \n/clean_db,  \n/create_db, \n/stop")


@dp.message_handler(commands="stop", user_id=ADMINS, state="*")
async def teams(msg: types.Message, state: FSMContext):
    all = db.summary()
    groups = ""
    for i in all:
        groups += f"{i[0]} guruhi {i[1]} ball\n"
    await msg.answer(f"Jamoalar ballari bilan tanishing: <b>{groups}</b>")
    await msg.answer(f"Commands: \n/all_users,  \n/reklama,  \n/clean_db,  \n/create_db, \n/stop")
    db.default_state()
    await gruppa.savol.set()
