from aiogram.types import Message
from setup import user_router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from src.database.query.words import add_new_word


class AddWord(StatesGroup):
    bot_msg: Message = State()
    first = State()
    second = State()


@user_router.message(AddWord.first)
async def first(message: Message, state: FSMContext):
    await state.update_data(first=message.text)
    await message.delete()
    data = await state.get_data()
    bot_msg = data['bot_msg']
    await bot_msg.edit_text("Second side 🃏")
    await state.set_state(AddWord.second)


@user_router.message(AddWord.second)
async def second(message: Message, state: FSMContext):
    await state.update_data(second=message.text)
    await message.delete()

    data = await state.get_data()
    bot_msg = data['bot_msg']
    await state.clear()
    await add_new_word(message.from_user.id, data['first'], data['second'])
    await bot_msg.edit_text("Word saved ✅")