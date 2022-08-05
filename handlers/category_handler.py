from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from database import category_db, expense_db
from aiogram.dispatcher.filters import Text
class CreateCategoryFSM(StatesGroup):
    category_name = State()


async def start_create_category(msg: types.Message):
    await CreateCategoryFSM.category_name.set()
    await msg.reply("Enter category name:")


async def create_category(msg: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        state_data["category_name"] = msg.text
    data = await state.get_data()
    await state.finish()
    category_db.add(
        {"category_name": data["category_name"]}
    )
    await msg.reply("Created!")

async def get_report(callback: types.CallbackQuery):
    category_id = int(callback.data[9:])
    category_charges = expense_db.get_by_query(
        {"category_id": category_id}
    )
    result = ""
    total = 0
    for charge in category_charges:
        s = f"\nDescription: {charge['description']}\n" \
            + f"Amount: {charge['amount']}"
        result += s
        total += charge["amount"]
    result += "\n----------------------------"
    result += f"\nTotal expenses: {total} kgs"
    await callback.message.answer(result)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_create_category, commands=["create_category"])
    dp.register_message_handler(create_category, state=CreateCategoryFSM.category_name)
    dp.register_callback_query_handler(get_report, Text(startswith="category_"))