from aiogram import executor
from telegram_bot import dp
from handlers.start_handler import register_message_handlers
from handlers.category_handler import register_handlers
from handlers.get_handler import register_handlers as get_category_register
from handlers.expense_handler import register_handlers as expense_register
register_message_handlers(dp)
register_handlers(dp)
get_category_register(dp)
expense_register(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)