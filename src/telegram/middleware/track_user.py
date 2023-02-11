from src.database.models import UserModel
from src.database.query.user import get_or_create_user
from typing import Callable, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from src.config.config import admins_id


class TrackUser(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: dict[str, Any]
    ) -> Any:
        if event.from_user.id in admins_id:
            is_admin = True
        else:
            is_admin = False
        user = await get_or_create_user(
            UserModel(username=event.from_user.username,
                      user_id=event.from_user.id,
                      is_admin=is_admin))

        if not user.is_blocked:
            return await handler(event, data)
