# from aiogram.dispatcher.filters import CommandStart
#
# from keyboards.default.menuKeyboard import menu
# from filters import IsPrivate
# import logging
#
# from aiogram import types
# from data.config import CHANNELS
# from keyboards.inline.subscription import check_button
# from loader import bot, dp
# from utils.misc import subscription
#
#
# @dp.message_handler(IsPrivate(), CommandStart())
# async def show_channels(message: types.Message):
#     channels_format = str()
#     for channel in CHANNELS:
#         chat = await bot.get_chat(channel)
#         invite_link = await chat.export_invite_link()
#         # logging.info(invite_link)
#         channels_format += f"👉 <a href='{invite_link}'>{chat.title}</a>\n"
#
#     await message.answer(f"Botdan foydalanish uchun, quyidagi kanallarga obuna bo'ling: \n"
#                          f"{channels_format}",
#                          reply_markup=check_button,
#                          disable_web_page_preview=True)
#
#
# @dp.callback_query_handler(text="check_subs")
# async def checker(call: types.CallbackQuery):
#     global status
#     await call.answer()
#     result = str()
#     for channel in CHANNELS:
#         status = await subscription.check(user_id=call.from_user.id,
#                                           channel=channel)
#         channel = await bot.get_chat(channel)
#         if status:
#             result += f"✅ <b>{channel.title}</b> kanaliga obuna bo'lgansiz!\n\n"
#         else:
#             invite_link = await channel.export_invite_link()
#             result += (f"❌ <b>{channel.title}</b> kanaliga obuna bo'lmagansiz. "
#                        f"<a href='{invite_link}'>Obuna bo'ling</a>\n\n")
#
#     await call.message.answer(result, disable_web_page_preview=True)
#     if status:
#         await call.message.answer(f"Assalomu alaykum, <b>{call.from_user.full_name}</b>.\n "
#                                   f"'Qur'on - qalblar shifosi' botiga xush kelibsiz!")
#         await call.message.answer('Botdan foydalanish uchun quyidagilardan birini tanlang:', reply_markup=menu)
