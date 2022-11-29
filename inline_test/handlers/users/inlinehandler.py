from aiogram import types
from loader import dp


@dp.inline_handler(text_contains='sight')
async def empty(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id=query.id,
                title="Dasturlash asoslari. Python",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://mohirdev.uz/courses/python"
                )
            )
        ]
    )
