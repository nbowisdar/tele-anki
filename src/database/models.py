from tortoise.models import Model
from tortoise import fields, Tortoise, run_async
from typing import TypedDict


class UserModel(TypedDict):
    user_id: int
    username: str
    is_admin: bool


class User(Model):
    user_id = fields.IntField(pk=True)
    username = fields.CharField(unique=True, max_length=100)
    is_admin = fields.BooleanField(default=False)
    is_blocked = fields.BooleanField(default=False)


async def init():
    await Tortoise.init(
        db_url='sqlite://app.db',
        modules={'models': ['src.database.models']}
    )
    await Tortoise.generate_schemas()


# async def add_user(username: str):
#     await Tournament.create(username=username)

