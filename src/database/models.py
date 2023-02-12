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

    words = fields.ReverseRelation["Word"]


class Word(Model):
    first = fields.TextField()
    second = fields.TextField()
    repetition_counter = fields.IntField(default=0)
    is_learning = fields.BooleanField(default=True)

    user = fields.ForeignKeyField("models.User", related_name='words')


async def init():
    await Tortoise.init(
        db_url='sqlite://app.db',
        modules={'models': ['src.database.models']}
    )
    await Tortoise.generate_schemas()

