from src.database.models import User
from loguru import logger


async def unblock_user(username: str) -> bool:
    res = await User.filter(username=username).update(is_blocked=False)
    if res:
        logger.info(f'User {username} unblocked')
        return True
    return False


async def block_user(username: str) -> bool:
    res = await User.filter(username=username).update(is_blocked=True)
    if res:
        logger.info(f'User {username} blocked')
        return True
    return False
