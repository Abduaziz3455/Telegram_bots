from aiogram import types
from data.config import SUPERUSERS


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushirish"),
            types.BotCommand("all_users", "Barcha foydalanuvchilar"),
            types.BotCommand("reklama", "Reklama yuborish"),
            types.BotCommand("clean_db", "Bazani tozalash"),
            types.BotCommand("create_db", "Baza yaratish"),
            types.BotCommand("stop", "Ballarni hisoblash"),

        ],
        scope=types.BotCommandScopeChat(chat_id='1556455886')
    )

    # await dp.bot.set_my_commands(
    #     [
    #         types.BotCommand("start", "Botni ishga tushurish"),
    #         types.BotCommand("help", "Yordam"),
    #         # types.BotCommand("set_photo", "Guruh rasmini o'zgartirish"),
    #         # types.BotCommand("set_title", "Guruh nomini o'zgartirish "),
    #         # types.BotCommand("set_description", "Guruh haqidagi ma'lumotni o'zgatirish"),
    #         # types.BotCommand("ro", "Foydalanuvchini Read Only (RO) rejimga o'tkazish"),
    #         # types.BotCommand("unro", "RO rejimdan chiqarish"),
    #         # types.BotCommand("ban", "Ban"),
    #         # types.BotCommand("unban", "Bandan chiqarish"),
    #     ]
    # )
