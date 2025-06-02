from aiogram import types
from aiogram.filters import CommandStart
from dispatcher import dp

@dp.message(CommandStart())
async def start_handler(msg: types.Message):
    await msg.answer(
        f"<b>Привет, {msg.from_user.first_name}\n\n"
        "Отправь /backup чтобы создать бэкап панели!</b>"
    )
