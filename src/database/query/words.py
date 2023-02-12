from src.database.models import Word, User
from loguru import logger


async def add_new_word(user_id: int, first: str, second: str):
    user = await User.filter(user_id=user_id).first()
    await Word.create(first=first, second=second, user=user)
