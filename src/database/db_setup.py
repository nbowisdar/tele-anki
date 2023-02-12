
db_url = 'sqlite://db.sqlite3'


TORTOISE_ORM = {
    "connections": {
         "default": db_url
    },
    "apps": {
        "models": {
            "models": ["aerich.models"],
            "default_connection": "default",
        },
    },
}


