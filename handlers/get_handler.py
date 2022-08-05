from aiogram import types, Dispatcher
from database import category_db
from buttons.buttons import get_categories_inline_keyboard

async def get_categories(msg: types.Message):
    all_categoires = category_db.get_all()
    await msg.reply("Your categories!", reply_markup=get_categories_inline_keyboard(all_categoires))


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(get_categories, commands=["get_categories"])