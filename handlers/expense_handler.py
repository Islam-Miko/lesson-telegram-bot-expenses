from aiogram import types, Dispatcher
from buttons.buttons import get_categories_inline_keyboard
from database import category_db
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from database import expense_db

class MakeExpenseFSM(StatesGroup):
    category = State()
    amount = State()
    description = State()



async def show_categories(msg: types.Message):
    await MakeExpenseFSM.category.set()
    all_category = category_db.get_all()
    await msg.reply("Choose category:", reply_markup=get_categories_inline_keyboard(all_category))


async def get_category(callback: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as state_data:
        state_data["category_id"] = int(callback.data[9:])
    await MakeExpenseFSM.next()
    await callback.message.reply("Enter amount:")

async def get_amount(msg: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        state_data["amount"] = int(msg.text)
    await MakeExpenseFSM.next()
    await msg.reply("Enter description:")

async def get_description(msg: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        state_data["description"] = msg.text
    data = await state.get_data()
    await state.finish()
    expense_db.add(data)
    await msg.reply("Successfully saved!")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(show_categories, commands=["make_expense"])
    dp.register_callback_query_handler(get_category, Text(startswith="category_"), state=MakeExpenseFSM.category)
    dp.register_message_handler(get_amount, state=MakeExpenseFSM.amount)
    dp.register_message_handler(get_description, state=MakeExpenseFSM.description)