from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Text, Command
from aiogram import F
from setup import user_router
from src.telegram.handlers.fsm_h.add_word import AddWord


@user_router.message(Command(commands='start'))
async def test(message: Message):
    await message.answer("bot works")


@user_router.message(F.text == 'test')
async def test(message: Message):
    await message.answer("bot works")


@user_router.message(Command(commands='add_new_word'))
async def test(message: Message, state: FSMContext):
    await message.delete()
    msg = await message.answer("First side 🀄️")
    await state.set_state(AddWord.first)
    await state.update_data(bot_msg=msg)

