from peewee import *
from db import pg_db
from playhouse.postgres_ext import DateTimeTZField, ArrayField


class BaseModel(Model):
    class Meta:
        database = pg_db

class User(Model):
    id = AutoField()
    name = CharField(max_length=255)
    email = CharField(unique=True, max_length=255)
    password = CharField(max_length=255)
    card_number = CharField(max_length=16, null=True)
    created_at = DateTimeTZField(column_name="created_at")

    class Meta:
        table_name = 'user'
