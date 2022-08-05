from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


def get_start_buttons():

    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    btn1 = KeyboardButton("/create_category")
    btn2 = KeyboardButton("/make_expense")
    btn3 = KeyboardButton("/get_categories")
    keyboard.row(btn1, btn2)
    keyboard.add(btn3)

    return keyboard


def get_categories_inline_keyboard(data: list[dict[str, str]]):
    keyboard = InlineKeyboardMarkup()
    for category in data:
        btn = InlineKeyboardButton(
            text=category["category_name"],
            callback_data=f"category_{category.get('id')}"
        )
        keyboard.add(btn)
    return keyboard