from aiogram.types import Message
from setup import admin_router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from src.database.query.block_user import unblock_user, block_user


class BlockUser(StatesGroup):
    username = State()


class UnblockUser(StatesGroup):
    username = State()


@admin_router.message(BlockUser.username)
async def block(message: Message, state: FSMContext):
    ok = await block_user(message.text)
    if ok:
        await message.reply("User was blocked 🦉")
    else:
        await message.reply("User not found 🙉")
    await state.clear()


@admin_router.message(UnblockUser.username)
async def unblock(message: Message, state: FSMContext):
    ok = await unblock_user(message.text)
    if ok:
        await message.reply("User was unblocked 👑")
    else:
        await message.reply("User not found 🙉")
    await state.clear()