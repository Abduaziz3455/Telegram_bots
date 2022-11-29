from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Farkhad"),
            KeyboardButton(text="Rabati Malik")
        ],
        [
            KeyboardButton(text="◀️ go back"),
            KeyboardButton(text="📍 Nearest place",
                           request_location=True)
        ]
    ], resize_keyboard=True
)