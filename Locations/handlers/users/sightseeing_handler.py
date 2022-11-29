from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default.menuKeyb import menu
from states.holat import holatlar
from data.locations_navoi import sights
from utils.misc.get_distance import choose_shortest
from loader import dp


## FARKHAD
@dp.message_handler(text="Farkhad", state=holatlar.sight)
async def send_farkhad(msg: Message):
    for shop_name, shop_location in sights:
        if shop_name == "Farkhad":
            await msg.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])


@dp.message_handler(text="Rabati Malik", state=holatlar.sight)
async def send_rabat(msg: Message):
    for shop_name, shop_location in sights:
        if shop_name == "Rabati Malik Caravanserai Cistern":
            await msg.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])


@dp.message_handler(text_contains="back", state=holatlar.sight)
async def go_back(msg: Message, state: FSMContext):
    await msg.answer(f"Choose where do you want to go 🌍:", reply_markup=menu)
    await state.finish()


@dp.message_handler(content_types='location', state=holatlar.sight)
async def get_contact(message: Message):
    location = message.location
    # latitude = location.latitude
    # longitude = location.longitude
    closest_shops = choose_shortest(location)

    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\nDistance: {distance:.2f} km."
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"Thanks. \n\n"
                         f"{text}", disable_web_page_preview=True)

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
