import logging
import wikipedia
from googletrans import Translator
from aiogram import Bot, Dispatcher, executor, types

translator = Translator()
API_TOKEN = '5253417368:AAHPZJ45BxNdChsSSdX08Cgd50oqVfdny0c'


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f"Wikipedia Botiga Xush Kelibsiz!\n"
                        f"ingliz,rus yoki o'zbek tillarida so'z kiriting!")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Bu bot wikipedia.org saytidan sizga kerakli ma'lumotlarni uzatadi!")


@dp.message_handler()
async def sendWiki(message: types.Message):
    lang = translator.detect(message.text).lang
    if lang == 'uz':
        wikipedia.set_lang('uz')
    elif lang == 'en':
        wikipedia.set_lang('en')
    elif lang == 'ru':
        wikipedia.set_lang('ru')
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid maqola topilmadi")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)