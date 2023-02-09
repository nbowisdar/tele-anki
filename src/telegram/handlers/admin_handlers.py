from aiogram.types import Message
from aiogram.filters import Text, Command
from aiogram import F
from setup import admin_router

@admin_router.message(Command(commands='admin'))
async def test(message: Message):
    await message.answer("You are admin!")