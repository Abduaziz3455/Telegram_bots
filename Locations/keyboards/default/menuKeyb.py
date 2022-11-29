from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="🗺 Sightseeing"),
            KeyboardButton(text="🏨 Hotel")
        ],
        [
            KeyboardButton(text="🛒 Supermarket 🛒")
        ],
        [
            KeyboardButton(text="⚕️ Pharmacy ⚕️"),
            KeyboardButton(text="🍲 Cafe 🍲")
        ]
    ], resize_keyboard=True
)