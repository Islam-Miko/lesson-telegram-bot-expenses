
from aiogram import types, Dispatcher
from buttons.buttons import get_start_buttons


async def start_button(msg: types.Message):
    await msg.reply("Hello, Welcome!", reply_markup=get_start_buttons())


def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=["start"])