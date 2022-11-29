from aiogram.types import InputFile, Message
from aiogram import types

from keyboards.default.location_button import keyboard
from loader import dp, bot

# @dp.message_handler(content_types=types.ContentType.PHOTO)
# async def get_file_id(msg: Message):
#     await msg.reply(msg.photo[-1].file_id)
from states.holat import holatlar


@dp.message_handler(text_contains="Sightseeing")
async def send_sights(msg: Message):
    await holatlar.sight.set()
    ## FARKHAD
    album1 = types.MediaGroup()
    photo1 = "https://russianpoetry.ru/images/photos/medium/article92445.jpg"
    photo3 = "https://mapio.net/images-p/34343112.jpg"
    photo2 = "https://mapio.net/images-p/43069021.jpg"
    txt = "<b>'Farkhad'</b> palace of culture"
    txt1 = "<b>'Three sisters'</b> fountain"
    album1.attach_photo(photo=photo1, caption=txt)
    album1.attach_photo(photo=photo2)
    album1.attach_photo(photo=photo3, caption=txt1)
    await msg.answer_media_group(media=album1)
    await msg.answer(f"👆{txt}👆\n  and {txt1}")

    ## Raboti Malik
    album2 = types.MediaGroup()
    photo4 = "https://cdnn1.img.sputniknews-uz.com/img/07e4/09/02/14892398_0:0:3072:1930_1920x0_80_0_0_c84b55d5b3ed4e479858e7237641887c.jpg"
    photo5 = "https://silkadv.com/sites/default/files/Uzbekistan/Pamytniki/Navoiyskaya_obl/Rabat_i_Malik_car_ser/0_2_1-1-1-min.jpg"
    photo6 = "https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/dvortsa-rabat-malik-2011-0-0-0-0-1583236722.jpg"
    txt2 = "<b>'Rabati Malik'</b> Caravanserai Cistern"
    txt3 = "History of Rabati Malik"
    album2.attach_photo(photo=photo4, caption=txt2)
    album2.attach_photo(photo=photo5, caption=txt3)
    album2.attach_photo(photo=photo6)
    await msg.answer_media_group(media=album2)
    await msg.answer(f"👆{txt2}👆")
    await msg.answer("Do you wanna go anywhere?", reply_markup=keyboard)


@dp.message_handler(text_contains="Hotel")
async def send_hotels(msg: Message):
    pass
