from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Text, Command
from aiogram import F
from setup import admin_router
from src.telegram.handlers.fsm_h.block_user import BlockUser, UnblockUser


@admin_router.message(Command(commands='admin'))
async def test(message: Message):
    await message.answer("You are admin!")


@admin_router.message(Command(commands='block_user'))
async def test(message: Message, state: FSMContext):
    await message.answer("Send username you want to block 🧸")
    await state.set_state(BlockUser.username)


@admin_router.message(Command(commands='unblock_user'))
async def test(message: Message, state: FSMContext):
    await message.answer("Send username you want to unblock 🧸")
    await state.set_state(UnblockUser.username)