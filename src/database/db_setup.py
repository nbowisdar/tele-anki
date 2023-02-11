from tortoise.models import Model
from tortoise import fields
from tortoise import Tortoise, run_async

from src.database.models import test

db_url = 'sqlite://db.sqlite3'


TORTOISE_ORM = {
    "connections": {
         "default": db_url
    },
    "apps": {
        "contact": {
            "models": [
                 "models", "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}


test()