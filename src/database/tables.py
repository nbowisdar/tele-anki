from peewee import CharField, IntegerField, ForeignKeyField, FloatField,\
    Model, SqliteDatabase

from setup import ROOT_DIR

db = SqliteDatabase(ROOT_DIR / "app.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    age = IntegerField()


def create_tables():
    tables = [User, ]
    db.create_tables(tables)


if __name__ == '__main__':
    create_tables()