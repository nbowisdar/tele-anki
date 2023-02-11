from src.database.models import User, UserModel
from loguru import logger


async def get_or_create_user(user: UserModel) -> User:
    user_db, created = await User.get_or_create(**user)
    if created:
        logger.info(f"New user - {user['username']}!")
    return user_db
